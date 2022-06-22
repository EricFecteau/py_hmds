"""Display XY when moving"""

import random

from emulator import emulator
from emulator import memory
from emulator import overlay

from hmds import movie_functions as mf
from hmds import memory_addresses as ma


def print_value(
    screen: overlay.Overlay, mem: memory.Memory, hmds_mem: ma.MemoryAddresses
):

    """Force the value (must have a screen transition for it to work)"""

    size, addr = hmds_mem.get_mem_addr("char_x")
    screen.write(
        xpos=0, ypos=8, string=f"x = {mem.read(addr, size, False)}", display_id=1
    )

    size, addr = hmds_mem.get_mem_addr("char_y")
    screen.write(
        xpos=0, ypos=16, string=f"y = {mem.read(addr, size, False)}", display_id=1
    )

    size, addr = hmds_mem.get_mem_addr("screen_x0")
    pixels = mem.read(addr, 1, False)
    size, addr = hmds_mem.get_mem_addr("screen_x1")
    steps = mem.read(addr, size, False)
    screen.write(
        xpos=50, ypos=8, string=f"x = {(steps*255)+pixels}", display_id=1
    )

    size, addr = hmds_mem.get_mem_addr("screen_y0")
    pixels = mem.read(addr, 1, False)
    size, addr = hmds_mem.get_mem_addr("screen_y1")
    steps = mem.read(addr, size, False)
    screen.write(
        xpos=50, ypos=16, string=f"x = {(steps*255)+pixels}", display_id=1
    )


def main() -> None:

    """Main function"""

    emu = emulator.Emulator(
        nds="./roms/HMDS/NA/0561 - Harvest Moon DS (U)(Legacy).nds",
        author="Eric Fecteau",
        movie="./movies/HMDS.dsm",
        save_path="./saves/",
        frontend=True,
        date=(2000, 1, 1, 0, 0, 0, 0),
    )

    emu.initialize_emulator(scale=2, rightscreen=False)

    mem = memory.Memory(emu)
    hmds_mem = ma.MemoryAddresses("NA1.0")

    # mf.intro(emu)
    # emu.save("intro.ds0")

    emu.load("intro.ds0")
    
    emu.run(
        continual_func=print_value,
        function_args={"screen": emu.overlay, "mem": mem, "hmds_mem": hmds_mem},
    )

    del emu


if __name__ == "__main__":

    main()
