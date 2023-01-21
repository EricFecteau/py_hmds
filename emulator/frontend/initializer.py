# type: ignore

import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, GLib
from emulator.frontend import controller


class GTKWindow:
    def __init__(self, emulator) -> None:

        self.emulator = emulator

        self.builder = None
        self.main_window = None
        self.controller = None

    def create_window(self):

        # Create Builder and import glade
        self.builder = Gtk.Builder()
        self.builder.add_from_file(".\\emulator\\frontend\\PyDeSmuMe.glade")

        # Create Window
        self.main_window: Window = self.builder.get_object("wMainW")
        self.main_window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.main_window.set_role("PyDeSmuME")
        GLib.set_application_name("PyDeSmuME")
        GLib.set_prgname("pydesmume")

        # Create controller
        self.controller = controller.MainController(
            self.builder, self.main_window, self.emulator
        )

    def set_options(self, scale=1, rightscreen=False):

        # Resize the window
        if scale != 1:
            self.controller.renderer.set_scale(scale)

        if rightscreen == True:
            self.controller.rightscreen(90)

        self.controller.resize()

    def run(self, program, data, continual_func, function_args):

        GLib.idle_add(program, data, continual_func, function_args)

        self.main_window.present()
        Gtk.main()
