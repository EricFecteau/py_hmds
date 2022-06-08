"""Script to extract lots of RNG values from HMDS"""


from emulator import emulator
from emulator import memory
from hmds import movie_functions as mf
from hmds import memory_addresses as ml


def print_random(mem, hmds_mem, data_list):
    data = mem.read(hmds_mem.get_mem_addr("rng"), 4, True)
    data_list.append(data)


def main() -> None:

    """Main function"""

    emu = emulator.Emulator(
        nds="./roms/HMDS/NA/0561 - Harvest Moon DS (U)(Legacy).nds",
        author="Eric Fecteau",
        movie="./movies/HMDS.dsm",
        save_path="./saves/",
        frontend=False,
    )

    emu.initialize_emulator(scale=2, rightscreen=False)
    mem = memory.Memory(emu)

    hmds_mem = ml.MemoryAddresses("ABCEN0J12")

    # mf.intro(emu)
    # emu.save("intro.ds0")

    emu.load("intro.ds0")

    data_list: list[int] = []

    emu.add("", 10)
    emu.add(
        "",
        1000,
        run_function=print_random,
        function_args={"mem": mem, "hmds_mem": hmds_mem, "data_list": data_list},
    )
    emu.add("", 10)

    emu.run()

    print(data_list)


if __name__ == "__main__":

    main()
