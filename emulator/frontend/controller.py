# type: ignore
# pylint: skip-file

#  Copyright 2020 Marco Köpcke (Parakoopa)
#
#  This file is part of py-desmume.
#
#  py-desmume is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  py-desmume is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with py-desmume.  If not, see <https://www.gnu.org/licenses/>.

from ast import Call
import cairo
import gi

from abc import ABC, abstractmethod
from math import radians
from typing import Callable

from emulator.desmume.controls import Keys, load_configured_config
from emulator.desmume.emulator import (
    DeSmuME,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_PIXEL_SIZE,
)

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gdk

from gi.repository.Gtk import Builder, Window


TICKS_PER_FRAME = 17


class MainController:
    def __init__(self, builder: Builder, window: Window, emu: DeSmuME):
        self.builder = builder
        self.window = window
        self.emu = emu

        self.renderer = AbstractRenderer.impl(emu)
        self.renderer.init()

        self._keyboard_cfg, self._joystick_cfg = load_configured_config(emu)

        self.frame = 0

        self._current_screen_width = SCREEN_WIDTH
        self._current_screen_height = SCREEN_HEIGHT
        self._screen_gap = False
        self._screen_right = False
        self._screen_invert = False
        self._click = False
        self._screen_right_force = False
        self._screen_no_gap = False

        # Add items to screen and get events
        self._main_draw = builder.get_object("wDraw_Main")
        self._main_draw.set_events(Gdk.EventMask.ALL_EVENTS_MASK)
        self._main_draw.show()
        self._sub_draw = builder.get_object("wDraw_Sub")
        self._sub_draw.set_events(Gdk.EventMask.ALL_EVENTS_MASK)
        self._sub_draw.show()

        builder.connect_signals(self)

    def on_destroy(self, *args):
        self.emu.destroy()
        Gtk.main_quit()

    def gtk_main_quit(self, *args):
        self.emu.destroy()
        Gtk.main_quit()

    def gtk_widget_hide_on_delete(self, w: Gtk.Widget, *args):
        w.hide_on_delete()
        return True

    def gtk_widget_hide(self, w: Gtk.Widget, *args):
        w.hide()

    # INPUT BUTTONS / KEYBOARD
    def on_wMainW_key_press_event(self, widget: Gtk.Widget, event: Gdk.EventKey, *args):
        key = self.lookup_key(event.keyval)
        # shift,ctrl, both alts
        mask = (
            Gdk.ModifierType.SHIFT_MASK
            | Gdk.ModifierType.CONTROL_MASK
            | Gdk.ModifierType.MOD1_MASK
            | Gdk.ModifierType.MOD5_MASK
        )
        if event.state & mask == 0:
            if event.keyval == self._keyboard_cfg[Keys.KEY_BOOST - 1]:
                self._boost = not self._boost
                if self._boost:
                    self._save_fs = self._frameskip
                    self._frameskip = self._boost_fs
                else:
                    self._frameskip = self._save_fs
                return True
            elif key and self.emu.is_running():
                self.emu.input.keypad_add_key(key)
                return True
        return False

    def on_wMainW_key_release_event(
        self, widget: Gtk.Widget, event: Gdk.EventKey, *args
    ):
        key = self.lookup_key(event.keyval)
        if key and self.emu.is_running():
            self.emu.input.keypad_rm_key(key)

    # OUTPUT SCREENS
    def on_wDrawScreen_main_draw_event(
        self, widget: Gtk.DrawingArea, ctx: cairo.Context, *args
    ):
        return self.renderer.screen(
            self._current_screen_width,
            self._current_screen_height,
            ctx,
            0 if not self._screen_invert else 1,
        )

    def on_wDrawScreen_main_configure_event(self, widget: Gtk.DrawingArea, *args):
        self.renderer.reshape(widget, 0)
        return True

    def on_wDrawScreen_sub_draw_event(
        self, widget: Gtk.DrawingArea, ctx: cairo.Context, *args
    ):
        return self.renderer.screen(
            self._current_screen_width,
            self._current_screen_height,
            ctx,
            1 if not self._screen_invert else 0,
        )

    def on_wDrawScreen_sub_configure_event(self, widget: Gtk.DrawingArea, *args):
        self.renderer.reshape(widget, 1)
        return True

    # INPUT STYLUS / MOUSE
    def on_wDrawScreen_main_motion_notify_event(
        self, widget: Gtk.Widget, event: Gdk.EventMotion, *args
    ):
        return self.on_wDrawScreen_motion_notify_event(widget, event, 0)

    def on_wDrawScreen_main_button_release_event(
        self, widget: Gtk.Widget, event: Gdk.EventButton, *args
    ):
        return self.on_wDrawScreen_button_release_event(widget, event, 0)

    def on_wDrawScreen_main_button_press_event(
        self, widget: Gtk.Widget, event: Gdk.EventButton, *args
    ):
        return self.on_wDrawScreen_button_press_event(widget, event, 0)

    def on_wDrawScreen_sub_motion_notify_event(
        self, widget: Gtk.Widget, event: Gdk.EventMotion, *args
    ):
        return self.on_wDrawScreen_motion_notify_event(widget, event, 1)

    def on_wDrawScreen_sub_button_release_event(
        self, widget: Gtk.Widget, event: Gdk.EventButton, *args
    ):
        return self.on_wDrawScreen_button_release_event(widget, event, 1)

    def on_wDrawScreen_sub_button_press_event(
        self, widget: Gtk.Widget, event: Gdk.EventButton, *args
    ):
        return self.on_wDrawScreen_button_press_event(widget, event, 1)

    def on_wDrawScreen_motion_notify_event(
        self, widget: Gtk.Widget, event: Gdk.EventMotion, display_id: int
    ):
        if (display_id == 1 ^ self._screen_invert) and self._click:
            if event.is_hint:
                _, x, y, state = widget.get_window().get_pointer()
            else:
                x = event.x
                y = event.y
                state = event.state
            if state & Gdk.ModifierType.BUTTON1_MASK:
                self.set_touch_pos(x, y)

    def on_wDrawScreen_button_release_event(
        self, widget: Gtk.Widget, event: Gdk.EventButton, display_id: int
    ):
        if display_id == 1 ^ self._screen_invert and self._click:
            self._click = False
            self.emu.input.touch_release()
        return True

    def on_wDrawScreen_button_press_event(
        self, widget: Gtk.Widget, event: Gdk.EventButton, display_id: int
    ):
        if event.button == 1:
            if (display_id == 1 ^ self._screen_invert) and self.emu.is_running():
                self._click = True
                _, x, y, state = widget.get_window().get_pointer()
                if state & Gdk.ModifierType.BUTTON1_MASK:
                    self.set_touch_pos(x, y)
        elif event.button == 2:
            # filter out 2x / 3x clicks
            if event.type == Gdk.EventType.BUTTON_PRESS:
                self.rotate(self.renderer.get_screen_rotation() + 90)
        return True

    def on_wDrawScreen_scroll_event(self, widget: Gtk.Widget, event: Gdk.Event, *args):
        zoom_inc = 0.125
        zoom_min = 0.5
        zoom_max = 2.0

        scale = self.renderer.get_scale()
        if event.delta_y < 0:
            scale += zoom_inc
        elif event.delta_y > 0:
            scale -= zoom_inc

        if scale > zoom_max:
            scale = zoom_max
        elif scale < zoom_min:
            scale = zoom_min

        self.renderer.set_scale(scale)

        self.resize()

        return True

    def lookup_key(self, keyval):
        key = False

        if keyval == 65362:  # Up
            key = 64
        if keyval == 65364:  # Down
            key = 128
        if keyval == 65361:  # Left
            key = 32
        if keyval == 65363:  # Right
            key = 16
        if keyval == 65293:  # Start
            key = 8
        if keyval == 115:  # B
            key = 2
        if keyval == 100:  # B
            key = 1
        if keyval == 97:  # Y
            key = 2048
        if keyval == 119:  # Y
            key = 1024
        if keyval == 113:  # West (trigger)
            key = 512
        if keyval == 101:  # East (trigger)
            key = 256

        return key

    def set_touch_pos(self, x: int, y: int):
        scale = self.renderer.get_scale()
        rotation = self.renderer.get_screen_rotation()
        x /= scale
        y /= scale
        emu_x = x
        emu_y = y
        if rotation == 90 or rotation == 270:
            emu_x = 256 - y
            emu_y = x

        if emu_x < 0:
            emu_x = 0
        elif emu_x > SCREEN_WIDTH - 1:
            emu_x = SCREEN_WIDTH - 1

        if emu_y < 9:
            emu_y = 0
        elif emu_y > SCREEN_HEIGHT:
            emu_y = SCREEN_HEIGHT

        if self._screen_invert:
            emu_x = SCREEN_WIDTH - 1 - emu_x
            emu_y = SCREEN_HEIGHT - emu_y

        self.emu.input.touch_set_pos(int(emu_x), int(emu_y))

    def rightscreen(self, apply):
        table: Gtk.Table = self.builder.get_object("table_layout")
        chk = self.builder.get_object("wvb_2_Sub")
        self._screen_right = apply or self._screen_right_force
        if self._screen_right:
            gtk_table_reattach(table, self._sub_draw, 3, 4, 0, 1, 0, 0, 0, 0)
            gtk_table_reattach(table, chk, 4, 5, 0, 1, 0, 0, 0, 0)
        else:
            gtk_table_reattach(table, self._sub_draw, 1, 2, 2, 3, 0, 0, 0, 0)
            gtk_table_reattach(table, chk, 0, 1, 2, 3, 0, 0, 0, 0)

        table.queue_resize()
        self._mainwindow_resize()

    def resize(self):
        scale = self.renderer.get_scale()

        self._main_draw.set_size_request(
            self._current_screen_width * scale, self._current_screen_height * scale
        )
        self._sub_draw.set_size_request(
            self._current_screen_width * scale, self._current_screen_height * scale
        )

        self._mainwindow_resize()

    def _mainwindow_resize(self):
        spacer1: Gtk.Widget = self.builder.get_object("misc_sep3")
        spacer2: Gtk.Widget = self.builder.get_object("misc_sep4")

        current_rotation = self.renderer.get_screen_rotation()
        rotated = current_rotation == 90 or current_rotation == 270

        dim1 = dim2 = 66 * self.renderer.get_scale()
        if not self._screen_gap:
            dim1 = dim2 = -1

        if self._screen_right == rotated:
            if self._screen_right:
                dim2 = -1
            else:
                dim1 = -1

        self.window.resize(1, 1)


def gtk_table_reattach(
    table: Gtk.Table,
    w: Gtk.Widget,
    left_attach: int,
    right_attach: int,
    top_attach: int,
    bottom_attach: int,
    xoptions: int,
    yoptions: int,
    xpadding: int,
    ypadding: int,
):
    for child in table.get_children():
        if child == w:
            table.child_set_property(child, "left_attach", left_attach)
            table.child_set_property(child, "right_attach", right_attach)
            table.child_set_property(child, "top_attach", top_attach)
            table.child_set_property(child, "bottom_attach", bottom_attach)
            table.child_set_property(child, "x-options", xoptions)
            table.child_set_property(child, "x-padding", xpadding)
            table.child_set_property(child, "y-options", yoptions)
            table.child_set_property(child, "y-padding", ypadding)


class AbstractRenderer(ABC):
    def __init__(self, emu: DeSmuME):
        self._emu = emu
        self._screen_rotation_degrees = 0
        self._scale = 1.0

    @classmethod
    def impl(cls, emu: DeSmuME) -> "AbstractRenderer":

        return SoftwareRenderer(emu)

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def screen(self, base_w, base_h, ctx: cairo.Context, display_id: int):
        pass

    @abstractmethod
    def reshape(self, draw: Gtk.DrawingArea, display_id: int):
        pass

    @abstractmethod
    def add_overlay(self, overlay: Callable):
        pass

    def set_scale(self, value):
        self._scale = value

    def get_scale(self):
        return self._scale

    def get_screen_rotation(self):
        return self._screen_rotation_degrees

    def set_screen_rotation(self, value):
        self._screen_rotation_degrees = value


class SoftwareRenderer(AbstractRenderer):
    def __init__(
        self,
        emu: DeSmuME,
        after_render_hook: Callable[[cairo.Context, int], None] = None,
    ):
        """The after rendering hook takes the ctx and display_id as params."""
        super().__init__(emu)
        self._upper_image = None
        self._lower_image = None
        self.overlay_call: Optional[Callable] = None
        self.decode_screen()

    def init(self):
        pass

    def screen(self, base_w, base_h, ctx: cairo.Context, display_id: int):
        if display_id == 0:
            self.decode_screen()

        ctx.translate(base_w * self._scale / 2, base_h * self._scale / 2)
        ctx.rotate(-radians(self._screen_rotation_degrees))
        if self._screen_rotation_degrees == 90 or self._screen_rotation_degrees == 270:
            ctx.translate(-base_h * self._scale / 2, -base_w * self._scale / 2)
        else:
            ctx.translate(-base_w * self._scale / 2, -base_h * self._scale / 2)
        ctx.scale(self._scale, self._scale)
        if display_id == 0:
            ctx.set_source_surface(self._upper_image)
        else:
            ctx.set_source_surface(self._lower_image)
        ctx.get_source().set_filter(cairo.Filter.NEAREST)

        ctx.paint()

        if self.overlay_call is not None:
            self.overlay_call(ctx, display_id)

    def reshape(self, draw: Gtk.DrawingArea, display_id: int):
        pass

    def add_overlay(self, overlay: Callable):
        self.overlay_call = overlay

    def decode_screen(self):
        gpu_framebuffer = self._emu.display_buffer_as_rgbx()

        self._upper_image = cairo.ImageSurface.create_for_data(
            gpu_framebuffer[: SCREEN_PIXEL_SIZE * 4],
            cairo.FORMAT_RGB24,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
        )

        self._lower_image = cairo.ImageSurface.create_for_data(
            gpu_framebuffer[SCREEN_PIXEL_SIZE * 4 :],
            cairo.FORMAT_RGB24,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
        )
