"""Short scripts to help with actions in the game"""

from re import X
from emulator import emulator
from emulator import memory
from hmds import memory_addresses as ml


def move_char_diff_screen(
    emu: emulator.Emulator,
    mem: memory.Memory,
    hmds_mem: ml.MemoryAddresses,
    screen_loc: int,
    xpos: int,
    ypos: int,
):

    """Move the character anywhere in the game"""

    def force_location(
        mem: memory.Memory,
        hmds_mem: ml.MemoryAddresses,
        screen_loc: int,
        xpos: int,
        ypos: int,
    ):
        size, addr = hmds_mem.get_mem_addr("screen_loc")
        mem.write(addr, size, screen_loc)

        size, addr = hmds_mem.get_mem_addr("char_x_write")
        mem.write(addr, size, xpos * 256)

        size, addr = hmds_mem.get_mem_addr("char_y_write")
        mem.write(addr, size, ypos * 256)

    # Trigger screen transition
    def trigger_transition(mem: memory.Memory, hmds_mem: ml.MemoryAddresses):

        size, addr = hmds_mem.get_mem_addr("trigger_0")
        mem.write(addr, size, 0)

        size, addr = hmds_mem.get_mem_addr("trigger_1")
        mem.write(addr, size, 1)

    emu.add(
        "",
        1,
        run_function=trigger_transition,
        function_args={
            "mem": mem,
            "hmds_mem": hmds_mem,
        },
    )
    emu.add(
        "",
        31,
        run_function=force_location,
        function_args={
            "mem": mem,
            "hmds_mem": hmds_mem,
            "screen_loc": screen_loc,
            "xpos": xpos,
            "ypos": ypos,
        },
    )


def move_char_same_screen(
    emu: emulator.Emulator,
    mem: memory.Memory,
    hmds_mem: ml.MemoryAddresses,
    xpos: int,
    ypos: int,
):

    """Move the character anywhere in the game"""

    def force_location(
        mem: memory.Memory,
        hmds_mem: ml.MemoryAddresses,
        xpos: int,
        ypos: int,
    ):
        size, addr = hmds_mem.get_mem_addr("char_x_write")
        mem.write(addr, size, xpos * 256)

        size, addr = hmds_mem.get_mem_addr("char_y_write")
        mem.write(addr, size, ypos * 256)

    emu.add(
        "",
        1,
        run_function=force_location,
        function_args={
            "mem": mem,
            "hmds_mem": hmds_mem,
            "xpos": xpos,
            "ypos": ypos,
        },
    )
