from platform import architecture
from emulator import emulator
from emulator import memory
from hmds import movie_functions as mf
from hmds import memory_addresses as ml
from hmds import action


def test(mem: memory.Memory, hmds_mem: ml.MemoryAddresses):

    """Get the scene ready"""

    size, addr = hmds_mem.get_mem_addr("mine_floor_num")
    print(mem.read_array(addr - 10, 20, 1, False))


def ready_scene(mem: memory.Memory, hmds_mem: ml.MemoryAddresses):

    """Get the scene ready"""

    size, addr = hmds_mem.get_npc_addr("Carter", "interact")
    mem.write(addr, size, 5)

    size, addr = hmds_mem.get_mem_addr("mine_num")
    mem.write(addr, size, 3)

    size, addr = hmds_mem.get_mem_addr("mine_floor_num")
    mem.write(addr, size, 101)


def store(mem: memory.Memory):

    """Move the char to the correct location"""

    mem.mem_search("register", 0, 2, False)


def check_store(mem: memory.Memory):

    """Move the char to the correct location"""

    mem.mem_search("!=", 0, 2, False)
    print(mem.return_search_list())


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

    emu.add(
        "",
        0,
        run_function=ready_scene,
        function_args={"mem": mem, "hmds_mem": hmds_mem},
    )

    emu.add("BU", 20)
    emu.add("A", 1)
    emu.add("", 24)
    action.move_char_diff_screen(emu, mem, hmds_mem, 0x3A, 130, 205)

    emu.run()

    del emu


if __name__ == "__main__":

    main()
