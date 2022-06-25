from emulator import emulator
from emulator import memory
from hmds import movie_functions as mf
from hmds import memory_addresses as ml


def move_char(mem, hmds_mem, val):

    """Force the value"""

    size, addr = hmds_mem.get_mem_addr("screen_loc")
    mem.write(addr, size, val)


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
    emu.add("BU", 30)
    emu.add("A", 1)
    # Move to mine
    emu.add(
        "",
        25,
        run_function=move_char,
        function_args={
            "mem": mem,
            "hmds_mem": hmds_mem,
            "val": 0x3A,
        },
    )
    emu.add("", 1)

    emu.run()

    del emu


if __name__ == "__main__":

    main()
