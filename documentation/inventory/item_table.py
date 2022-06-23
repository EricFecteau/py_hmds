from emulator import emulator
from emulator import memory
from emulator import overlay

from hmds import movie_functions as mf
from hmds import memory_addresses as ml


def item_table(
    screen: overlay.Overlay, mem: memory.Memory, hmds_mem: ml.MemoryAddresses, item: int
):

    """Read the value"""

    _, addr = hmds_mem.get_mem_addr("item_price")

    screen.write(
        xpos=0,
        ypos=8,
        string=f"Price = {mem.read(addr + (item * 12), 4, False)}",
        display_id=1,
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

    hmds_mem = ml.MemoryAddresses("NA1.0")

    # mf.intro(emu)
    # emu.save("intro.ds0")

    emu.load("intro.ds0")

    emu.run(
        continual_func=item_table,
        function_args={
            "screen": emu.overlay,
            "mem": mem,
            "hmds_mem": hmds_mem,
            "item": 0x0020,
        },
    )

    del emu


if __name__ == "__main__":

    main()
