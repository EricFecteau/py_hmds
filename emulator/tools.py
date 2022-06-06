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


def suppress_output() -> tuple[tuple[int, int], list[int]]:

    """Suppress the output of DESMUME"""

    # open 2 fds
    null_fds = [os.open(os.devnull, os.O_RDWR) for x in range(0, 2)]
    # save the current file descriptors to a tuple
    save = os.dup(1), os.dup(2)
    # put /dev/null fds on 1 and 2
    os.dup2(null_fds[0], 1)
    os.dup2(null_fds[1], 2)
    return save, null_fds


def reset_output(save: tuple[int, int], null_fds: list[int]):

    """Restore the output, to print to the log"""

    # restore file descriptors so I can print the results
    os.dup2(save[0], 1)
    os.dup2(save[1], 2)
    # close the temporary fds
    os.close(null_fds[0])
    os.close(null_fds[1])
