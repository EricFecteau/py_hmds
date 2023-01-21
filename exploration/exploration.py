from emulator import emulator
from emulator import memory
from emulator import overlay
from hmds import movie_functions as mf
from hmds import memory_addresses as ml


def ready_scene(mem: memory.Memory, hmds_mem: ml.MemoryAddresses):

    """Get the scene ready"""

    size, addr = hmds_mem.get_npc_addr("Carter", "fp")
    mem.write(addr, size, 5)


def move_char(mem: memory.Memory, hmds_mem: ml.MemoryAddresses):

    """Move the char to the correct location"""

    size, addr = hmds_mem.get_mem_addr("screen_loc")
    mem.write(addr, size, 0x07)

    size, addr = hmds_mem.get_mem_addr("char_x_write")
    mem.write(addr, size, 640 * 256)

    size, addr = hmds_mem.get_mem_addr("char_y_write")
    mem.write(addr, size, 125 * 256)

    size, addr = hmds_mem.get_mem_addr("trigger_0")
    mem.write(addr, size, 0)

    size, addr = hmds_mem.get_mem_addr("trigger_1")
    mem.write(addr, size, 1)


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

    # emu.add("BU", 20)
    emu.add("A", 1)
    emu.add(
        "",
        0,
        run_function=ready_scene,
        function_args={
            "mem": mem,
            "hmds_mem": hmds_mem,
        },
    )
    emu.add(
        "",
        1,
        run_function=move_char,
        function_args={"mem": mem, "hmds_mem": hmds_mem},
    )

    emu.run()

    del emu


if __name__ == "__main__":

    main()
