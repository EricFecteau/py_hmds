"""Script to extract lots of RNG values from HMDS"""

from csv import writer

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


def store_list(data_list: list) -> None:

    """Store the data in the CSV"""

    with open(
        "./documentation/mechanics/rng/rng.csv", "a+", newline="", encoding="utf-8"
    ) as obj:
        csv_writer = writer(obj, delimiter="\n")
        csv_writer.writerow(data_list)


def main() -> None:

    """Main function"""

    emu = emulator.Emulator(
        nds="./roms/HMDS/NA/0561 - Harvest Moon DS (U)(Legacy).nds",
        author="Eric Fecteau",
        movie="./movies/HMDS.dsm",
        save_path="./saves/",
        frontend=False,
        date=(2000, 1, 1, 0, 0, 0, 0),
    )

    emu.initialize_emulator(scale=2, rightscreen=False)

    mem = memory.Memory(emu)

    hmds_mem = ml.MemoryAddresses("NA1.0")

    mf.new_game(emu)
    emu.add("", 100)

    data_list: list = ["RNG_Value"]
    store_list(data_list)

    for _ in range(int(1_000_000 / 10_000)):
        emu.add("", 0, run_function=clear_list, function_args={"data_list": data_list})
        emu.add(
            "",
            10_000,
            run_function=get_random,
            function_args={"mem": mem, "hmds_mem": hmds_mem, "data_list": data_list},
        )
        emu.add("", 0, run_function=store_list, function_args={"data_list": data_list})
        emu.save("rng.ds0")

    emu.run()

    del emu


if __name__ == "__main__":

    main()
