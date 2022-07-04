"""This module controls DeSmuME and the Frontend"""

import time

from typing import Callable, Optional

from tqdm import tqdm

from emulator import tools
from emulator import overlay
from emulator.frontend import initializer
from emulator.desmume import emulator

SCREEN_WIDTH: int = 256
SCREEN_HEIGHT: int = 192

# pylint: disable=too-many-instance-attributes
class Emulator:

    """Control DeSmuMe using common tools for bug hunting and TASing"""

    def __init__(
        self,
        nds: str,
        movie: str = "",
        author: str = "",
        save_path: str = "",
        date: tuple[int, int, int, int, int, int, int] = (2000, 1, 1, 0, 0, 0, 0),
        frontend: bool = False,
    ) -> None:

        self.nds = nds
        self.movie = movie
        self.date = date
        self.author = author

        self.frontend = frontend

        self.gui = None
        self.emu = None

        self.frame = 0
        self.fps = 0
        self.second_timer = 0

        self.xpos = 0
        self.ypos = 0

        self.frame_list: list[dict] = []

        self.save_path = save_path

        self.overlay = overlay.Overlay(self)

    def __del__(self):
        self.emu.destroy()
        del self.emu

    def initialize_emulator(
        self, scale: float = 1.0, rightscreen: bool = False
    ) -> bool:

        """Initialize the emulator and frontend"""

        save = tools.suppress_output()

        # Load desmume
        self.emu = emulator.DeSmuME()  # type: ignore[attr-defined]

        if self.emu is None:
            return False

        self.emu.open(self.nds)

        # Options
        self.emu.volume_set(0)
        self.emu.set_savetype(4)

        self.emu.resume()

        # Init joysticks
        self.emu.input.joy_init()
        self.emu.input.keypad_update(0)

        # Record the movie
        if self.movie != "":
            self.emu.movie.record(
                self.movie,
                self.author,
                rtc_date=emulator.DeSmuME_Date(
                    self.date[0],
                    self.date[1],
                    self.date[2],
                    self.date[3],
                    self.date[4],
                    self.date[5],
                    self.date[6],
                ),
            )

        tools.reset_output(save)

        # Do you want a frontend?
        if self.frontend:

            # Initiate the gui
            self.gui = initializer.GTKWindow(emulator=self.emu)

            if self.gui is None:
                return False

            self.gui.create_window()
            self.gui.set_options(scale=scale, rightscreen=rightscreen)

        return True

    def load(self, file_name):

        """Load a dsX file (memory saved)"""

        def _load(file_name):

            save = tools.suppress_output()
            self.emu.savestate.load_file(f"{self.save_path}{file_name}")
            tools.reset_output(save)

            with open(
                f"{self.save_path}{file_name}.frame", "r", encoding="utf-8"
            ) as frame_file:
                self.frame = int(frame_file.read())

            self.emu.input.keypad_update(0)

        self.frame_list.append(
            {
                "function": _load,
                "function_args": {"file_name": file_name},
                "skip_frame": True,
            }
        )

    def save(self, file_name):

        """Save a dsX file (memory saved)"""

        def _save(file_name):

            save = tools.suppress_output()
            self.emu.savestate.save_file(f"{self.save_path}{file_name}")
            tools.reset_output(save)

            with open(
                f"{self.save_path}{file_name}.frame", "w", encoding="utf-8"
            ) as frame_file:
                frame_file.write(str(self.frame))

        self.frame_list.append(
            {
                "function": _save,
                "function_args": {"file_name": file_name},
                "skip_frame": True,
            }
        )

    # pylint: disable=too-many-arguments
    def add(
        self,
        button: str,
        frames: int,
        xpos: int = 0,
        ypos: int = 0,
        run_function: Optional[Callable] = None,
        function_args: Optional[dict] = None,
    ):

        """Add frames actions (button, screen, program) to the frame list"""

        for _ in range(frames):
            self.frame_list.append(
                {
                    "keys": button,
                    "xpos": xpos,
                    "ypos": ypos,
                    "function": run_function,
                    "function_args": function_args,
                    "skip_frame": False,
                }
            )

        if frames == 0:
            self.frame_list.append(
                {
                    "function": run_function,
                    "function_args": function_args,
                    "skip_frame": True,
                }
            )

    def emu_cycle(
        self,
        action: dict,
        continual_func: Optional[Callable] = None,
        function_args: Optional[dict] = None,
    ) -> bool:

        """Main loop for the emulator"""

        if self.emu is None:
            return False

        if not self.emu.is_running():
            return False

        frame_action = None
        if len(action) > 0:
            frame_action = action.pop(0)

            if frame_action["function"] is not None:

                # Provide the args as kargs
                if frame_action["function_args"] is not None:
                    frame_action["function"](**frame_action["function_args"])
                else:
                    frame_action["function"]()

            # Skip the frame (for functions like saving or memory management)
            if frame_action["skip_frame"] is True:
                return True

            self.xpos = frame_action["xpos"]
            self.ypos = frame_action["ypos"]

            if not (frame_action["xpos"] == 0 and frame_action["ypos"] == 0):
                self.emu.input.touch_set_pos(frame_action["xpos"], frame_action["ypos"])
            else:
                self.emu.input.touch_release()

            tools.add_keys(self.emu, frame_action["keys"])
        else:
            if continual_func is not None:

                # Provide the args as kargs
                if function_args is not None:
                    continual_func(**function_args)
                else:
                    continual_func()

        self.emu.cycle()

        if frame_action is not None:
            tools.rm_keys(self.emu, frame_action["keys"])

        self.frame += 1
        self.fps += 1

        if not self.frontend:
            return True

        self.gui.controller._main_draw.queue_draw()
        self.gui.controller._sub_draw.queue_draw()

        self.gui.controller.renderer.add_overlay(self.overlay.display_overlay)

        if self.second_timer == 0:
            self.second_timer = round(time.time() * 1000)
        if round(time.time() * 1000) - self.second_timer >= 1000:
            self.gui.main_window.set_title(f"PyDeSmuME - {self.fps}fps")
            self.fps = 0
            self.second_timer = 0

        return True

    def run(
        self,
        continual_func: Optional[Callable] = None,
        function_args: Optional[dict] = None,
    ):

        """Run the emulation"""

        if self.emu is not None:
            self.emu.input.keypad_update(0)

        if self.frontend:
            if self.gui is not None:
                self.gui.run(
                    program=self.emu_cycle,
                    data=self.frame_list,
                    continual_func=continual_func,
                    function_args=function_args,
                )
        else:
            for _ in tqdm(range(len(self.frame_list))):
                self.emu_cycle(self.frame_list)
