from emulator import emulator
from emulator import memory
from emulator import overlay
from hmds import movie_functions as mf
from hmds import memory_addresses as ml


def read_char(
    screen: overlay.Overlay,
    mem: memory.Memory,
    hmds_mem: ml.MemoryAddresses,
    npc_name: str,
):

    """Read the value of a character"""

    size, addr = hmds_mem.get_npc_addr(npc_name, "fp")
    screen.write(
        xpos=0,
        ypos=8,
        string=f"FP = {mem.read(addr, size, False)}",
        display_id=1,
    )

    size, addr = hmds_mem.get_npc_addr(npc_name, "lp")
    screen.write(
        xpos=150,
        ypos=8,
        string=f"LP = {mem.read(addr, size, False)}",
        display_id=1,
    )

    size, addr = hmds_mem.get_npc_addr(npc_name, "interact")
    screen.write(
        xpos=0,
        ypos=18,
        string=f"Interact = {mem.read(addr, size, False)}",
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

    npc = "Takakura"

    # mf.intro(emu)
    # emu.save("intro.ds0")

    emu.load("intro.ds0")

    emu.run(
        continual_func=read_char,
        function_args={
            "screen": emu.overlay,
            "mem": mem,
            "hmds_mem": hmds_mem,
            "npc_name": npc,
        },
    )

    del emu


if __name__ == "__main__":

    main()
