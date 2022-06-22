"""Add an overlay (text, boxes, etc) to the emulator"""

from typing import Callable

SCREEN_WIDTH: int = 256
SCREEN_HEIGHT: int = 192

# pylint: disable=too-many-instance-attributes
class Overlay:

    """CTX overlay on the emulator image"""

    def __init__(self, emu) -> None:

        self.emu = emu
        self.overlay_list_id0: list = []
        self.overlay_list_id1: list = []

        self.text_list0: list = []
        self.text_list1: list = []

    def write(self, xpos: int, ypos: int, string: str, display_id: int):

        """Queue text"""

        if display_id == 0:
            self.text_list0.append([xpos, ypos, string])
        else:
            self.text_list1.append([xpos, ypos, string])

    def display_text(self, ctx, display_id):

        """Write text on one of the displays"""

        ctx.set_source_rgb(0, 0, 0)
        ctx.select_font_face("courier new", 0, 0)
        ctx.set_font_size(8)
        ctx.set_tolerance(0.1)

        if display_id == 0:
            for string in self.text_list0:
                ctx.move_to(string[0], string[1])
                ctx.set_line_width(0.5)
                ctx.text_path(string[2])
            self.text_list0 = []
        else:
            for string in self.text_list1:
                ctx.move_to(string[0], string[1])
                ctx.set_line_width(0.5)
                ctx.text_path(string[2])
            self.text_list1 = []

    def default(self, ctx, display_id):

        """CTX overlay on the emulator image"""

        if display_id == 0:
            pass
            # ctx.set_source_rgba(1, 0, 0, 1)
            # ctx.rectangle(25, 25, 75, 75)
            # ctx.fill()
        else:
            # Cross hair
            if self.emu.xpos != 0 and self.emu.ypos != 0:

                # Small box over click
                ctx.set_line_width(0)
                ctx.set_source_rgba(1, 0, 0, 0.5)
                ctx.rectangle(self.emu.xpos - 1, self.emu.ypos - 1, 3, 3)

                # Lines accross the screen in cross hair
                ctx.set_line_width(1)
                ctx.move_to(self.emu.xpos + 0.5, 0)
                ctx.line_to(self.emu.xpos + 0.5, SCREEN_HEIGHT)
                ctx.move_to(0, self.emu.ypos + 0.5)
                ctx.line_to(SCREEN_WIDTH, self.emu.ypos + 0.5)

        ctx.stroke()

    def add_overlay(self, overlay: Callable, display_id: int):

        """Add a new custom overlay"""

        if display_id == 0:
            self.overlay_list_id0.append(overlay)
        else:
            self.overlay_list_id1.append(overlay)

    def display_overlay(self, ctx, display_id):

        """Display all of the overlay data, each frame"""

        # if display_id == 0:
        #     for _ in range(len(self.overlay_list_id0)):
        #         self.overlay_list_id0.pop()(ctx, display_id)
        # else:
        #     for _ in range(len(self.overlay_list_id1)):
        #         self.overlay_list_id1.pop()(ctx, display_id)

        self.display_text(ctx, display_id)

        self.default(ctx, display_id)
