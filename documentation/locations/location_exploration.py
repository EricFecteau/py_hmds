from emulator import emulator
from emulator import memory
from hmds import movie_functions as mf
from hmds import memory_addresses as ml


def get_random(mem, hmds_mem, data_list):

    """Get the data from the RNG value"""

    size, addr = hmds_mem.get_mem_addr("rng")

    data = mem.read(addr, size, True)
    data_list.append(data)


def clear_list(data_list: list) -> None:

    """Clear the data_list list"""

    del data_list[:]


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

    mf.intro(emu)

    emu.run()

    del emu


if __name__ == "__main__":

    main()
