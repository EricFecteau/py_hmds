"""Various repeated actions"""

from emulator.emulator import Emulator


def dialog(emu: Emulator, frames: int) -> None:

    """Skip dialogue at the highest speed possible"""

    emu.add("B", frames - 1, xpos=244, ypos=49)
    emu.add("", 1)


def enter_name(emu: Emulator, xpos: int, ypos: int) -> None:

    """Enter name in intro"""

    emu.add("", 1, xpos, ypos)
    emu.add("", 1, 20, 180)
    emu.add("", 2)
    emu.add("", 1, 37, 34)
    emu.add("A", 1)


def enter_calendar(emu: Emulator) -> None:

    """Enter calendar in intro"""

    emu.add("", 1, 81, 81)
    emu.add("", 1)
    emu.add("", 1, 78, 47)
    emu.add("", 1)
    emu.add("", 1, 7, 184)
    emu.add("", 2)
    emu.add("", 1, 31, 28)
    emu.add("A", 1)


def new_game(emu: Emulator):

    """Get pas the main menu"""
    emu.add("", 440)
    emu.add("", 1, xpos=100, ypos=100)
    emu.add("", 120)
    emu.add("", 1, xpos=100, ypos=100)


def talk_to_thomas(emu: Emulator) -> None:

    """Skip the conversation with Thomas"""

    emu.add("BR", 10)
    emu.add("BD", 100)
    dialog(emu, 300)
    emu.add("D", 1)
    emu.add("A", 1)
    dialog(emu, 500)


def intro(emu: Emulator) -> None:

    """Automate the intro"""

    new_game(emu)
    dialog(emu, 230)
    enter_name(emu, 114, 47)  # "E is for Exadrid"
    dialog(emu, 160)
    enter_calendar(emu)
    dialog(emu, 180)
    enter_name(emu, 48, 63)  # "F is for Farm"
    dialog(emu, 165)
    enter_name(emu, 98, 49)  # "D is for Dog"
    dialog(emu, 165)
    enter_name(emu, 84, 49)  # "C is for Cat"
    dialog(emu, 16070)
    talk_to_thomas(emu)
