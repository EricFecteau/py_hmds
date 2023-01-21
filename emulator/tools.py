import os


def add_keys(emu, keys):

    """Add keys to the emulator (have to re-write it because py-desmume has wrong mapping)"""

    if "R" in keys:
        emu.input.keypad_add_key(16)
    if "L" in keys:
        emu.input.keypad_add_key(32)
    if "D" in keys:
        emu.input.keypad_add_key(128)
    if "U" in keys:
        emu.input.keypad_add_key(64)
    if "T" in keys:
        emu.input.keypad_add_key(0)  # Unknown
    if "S" in keys:
        emu.input.keypad_add_key(8)
    if "B" in keys:
        emu.input.keypad_add_key(2)
    if "A" in keys:
        emu.input.keypad_add_key(1)
    if "Y" in keys:
        emu.input.keypad_add_key(2048)
    if "X" in keys:
        emu.input.keypad_add_key(1024)
    if "W" in keys:
        emu.input.keypad_add_key(512)
    if "E" in keys:
        emu.input.keypad_add_key(256)


def rm_keys(emu, keys):

    """Remove keys from the emulator (have to re-write it because py-desmume has wrong mapping)"""

    if "R" in keys:
        emu.input.keypad_rm_key(16)
    if "L" in keys:
        emu.input.keypad_rm_key(32)
    if "D" in keys:
        emu.input.keypad_rm_key(128)
    if "U" in keys:
        emu.input.keypad_rm_key(64)
    if "T" in keys:
        emu.input.keypad_rm_key(0)  # Unknown
    if "S" in keys:
        emu.input.keypad_rm_key(8)
    if "B" in keys:
        emu.input.keypad_rm_key(2)
    if "A" in keys:
        emu.input.keypad_rm_key(1)
    if "Y" in keys:
        emu.input.keypad_rm_key(2048)
    if "X" in keys:
        emu.input.keypad_rm_key(1024)
    if "W" in keys:
        emu.input.keypad_rm_key(512)
    if "E" in keys:
        emu.input.keypad_rm_key(256)


def suppress_output() -> tuple[int, int]:

    """Suppress the output of DESMUME"""

    save1 = os.dup(1)
    save2 = os.dup(2)
    devnull = os.open(os.devnull, os.O_RDWR)
    os.dup2(devnull, 1)
    os.dup2(devnull, 2)
    os.close(devnull)

    return (save1, save2)


def reset_output(save: tuple[int, int]) -> None:

    """Reset the output of DESMUME"""

    os.dup2(save[0], 1)
    os.dup2(save[1], 2)
    os.close(save[0])
    os.close(save[1])


def hex_list(list_to_hex: list[int], format_str: str = "") -> list[str]:

    """Convert all the numbers in a list to hex"""

    new_list: list[str] = []

    for item in list_to_hex:
        if format_str == "":
            new_list.append(hex(item))
        else:
            new_list.append(format_str.format(item))

    return new_list
