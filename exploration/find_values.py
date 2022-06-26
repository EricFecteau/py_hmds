from emulator import emulator
from emulator import memory
from emulator import overlay
from hmds import movie_functions as mf
from hmds import memory_addresses as ml


def test(mem: memory.Memory, hmds_mem: ml.MemoryAddresses, val: str):

    print(val, end=" = ")
    for i in range(37564900, 37564920):
        print(mem.read(i, 1, False), end=" | ")
    print()


def store(emu: emulator.Emulator, mem: memory.Memory, hmds_mem: ml.MemoryAddresses):

    """Move the char to the correct location"""

    mem.mem_search("register", 0, 1, False)


def look_switch(
    emu: emulator.Emulator, mem: memory.Memory, hmds_mem: ml.MemoryAddresses
):

    """Move the char to the correct location"""

    mem.mem_search("!=", 0, 1, False)

    # print(mem.return_search_list())


def test_values(
    screen: overlay.Overlay, mem: memory.Memory, hmds_mem: ml.MemoryAddresses
):

    """Move the char to the correct location"""

    size_x, addr_x = hmds_mem.get_mem_addr("char_x_write")
    screen.write(
        xpos=0, ypos=8, string=f"X = {mem.read(addr_x, size_x, False)}", display_id=1
    )

    size_y, addr_y = hmds_mem.get_mem_addr("char_y_write")
    screen.write(
        xpos=0, ypos=16, string=f"Y = {mem.read(addr_y, size_y, False)}", display_id=1
    )

    size_x, addr_x = hmds_mem.get_mem_addr("char_x_read")
    screen.write(
        xpos=50, ypos=8, string=f"X = {mem.read(addr_x, size_x, False)}", display_id=1
    )

    size_y, addr_y = hmds_mem.get_mem_addr("char_y_read")
    screen.write(
        xpos=50, ypos=16, string=f"Y = {mem.read(addr_y, size_y, False)}", display_id=1
    )


def where(screen: overlay.Overlay, mem: memory.Memory, hmds_mem: ml.MemoryAddresses):

    size, addr = hmds_mem.get_mem_addr("screen_loc")
    mem.write(addr, size, 0x07)


def force_values(
    screen: overlay.Overlay, mem: memory.Memory, hmds_mem: ml.MemoryAddresses
):

    """Move the char to the correct location"""

    # X and Y values

    # mem.write(0x23D37B8, 4, 100 * 256)
    # mem.write(0x23D37B8 + 4, 4, 100 * 256)

    # size, addr = hmds_mem.get_mem_addr("screen_loc")
    # mem.write(addr, size, 0x07)

    # size, addr = hmds_mem.get_mem_addr("char_x_write")
    # mem.write(addr, size, 640 * 256)

    # size, addr = hmds_mem.get_mem_addr("char_y_write")
    # mem.write(addr, size, 125 * 256)

    mem.write(0x23D31E8, 1, 1)
    mem.write(0x23D31F0, 2, 0)

    # for mem_val in mem.return_search_list():
    #     print(f"mem.write({int(mem_val, base=16)}, 1, 1)")
    # mem.write(int(mem_val, base=16), 1, 1)


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
        "U",
        20,
        run_function=test,
        function_args={
            "mem": mem,
            "hmds_mem": hmds_mem,
            "val": "U",
        },
    )
    # emu.add(
    #     "",
    #     1,
    #     run_function=store,
    #     function_args={
    #         "emu": emu,
    #         "mem": mem,
    #         "hmds_mem": hmds_mem,
    #     },
    # )
    emu.add(
        "A",
        2,
        run_function=test,
        function_args={
            "mem": mem,
            "hmds_mem": hmds_mem,
            "val": "A",
        },
    )
    # emu.add(
    #     "",
    #     1,
    #     run_function=look_switch,
    #     function_args={
    #         "emu": emu,
    #         "mem": mem,
    #         "hmds_mem": hmds_mem,
    #     },
    # )
    emu.add(
        "U",
        50,
        run_function=test,
        function_args={
            "mem": mem,
            "hmds_mem": hmds_mem,
            "val": "B",
        },
    )
    emu.add(
        "A",
        1,
        run_function=force_values,
        function_args={
            "screen": emu.overlay,
            "mem": mem,
            "hmds_mem": hmds_mem,
        },
    )
    emu.add(
        "",
        50,
        run_function=where,
        function_args={
            "screen": emu.overlay,
            "mem": mem,
            "hmds_mem": hmds_mem,
        },
    )

    emu.run(
        # continual_func=test_values,
        # function_args={"screen": emu.overlay, "mem": mem, "hmds_mem": hmds_mem},
        # continual_func=force_values,
        # function_args={"screen": emu.overlay, "mem": mem},
    )

    del emu


if __name__ == "__main__":

    main()
