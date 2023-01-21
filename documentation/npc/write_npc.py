from emulator import emulator
from emulator import memory
from emulator import overlay
from hmds import movie_functions as mf
from hmds import memory_addresses as ml


def write_char(
    mem: memory.Memory,
    hmds_mem: ml.MemoryAddresses,
    npc_name: str,
    attribute: str,
    value: int,
):

    """Read the value of a character"""

    size, addr = hmds_mem.get_npc_addr(npc_name, attribute)
    mem.write(addr, size, value)


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

    npc = "Takakura"

    # mf.intro(emu)
    # emu.save("intro.ds0")

    emu.load("intro.ds0")

    emu.add(
        "",
        0,
        run_function=write_char,
        function_args={
            "mem": mem,
            "hmds_mem": hmds_mem,
            "npc_name": npc,
            "attribute": "fp",
            "value": 5,
        },
    )

    emu.run()

    del emu


if __name__ == "__main__":

    main()
