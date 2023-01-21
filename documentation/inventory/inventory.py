from emulator import emulator
from emulator import memory
from hmds import movie_functions as mf
from hmds import memory_addresses as ml


def red_slot(mem, hmds_mem, item, quantity, quality):

    """Force the value"""

    _, addr = hmds_mem.get_mem_addr("red_slot")
    mem.write(addr, 2, item)
    mem.write(addr + 2, 1, quality)
    mem.write(addr + 3, 1, quantity)


def green_slot(mem, hmds_mem, item, quantity, quality):

    """Force the value"""

    _, addr = hmds_mem.get_mem_addr("green_slot")
    mem.write(addr, 2, item)
    mem.write(addr + 2, 1, quality)
    mem.write(addr + 3, 1, quantity)


def blue_slot(mem, hmds_mem, item, quantity, quality):

    """Force the value"""

    _, addr = hmds_mem.get_mem_addr("blue_slot")
    mem.write(addr, 2, item)
    mem.write(addr + 2, 1, quality)
    mem.write(addr + 3, 1, quantity)


def bag(mem, hmds_mem, x_bag, y_bag, item, quantity, quality):

    """Force the value"""

    _, addr = hmds_mem.get_mem_addr("bag")
    mem.write(addr + (x_bag * 12) + (y_bag * 4), 2, item)
    mem.write(addr + (x_bag * 12) + (y_bag * 4) + 2, 1, quality)
    mem.write(addr + (x_bag * 12) + (y_bag * 4) + 3, 1, quantity)


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
    # Red slot
    emu.add(
        "",
        0,
        run_function=red_slot,
        function_args={
            "mem": mem,
            "hmds_mem": hmds_mem,
            "item": 0x0000,
            "quantity": 0x02,
            "quality": 0x07,
        },
    )
    # Green slot
    emu.add(
        "",
        0,
        run_function=green_slot,
        function_args={
            "mem": mem,
            "hmds_mem": hmds_mem,
            "item": 0x0047,
            "quantity": 0x21,
            "quality": 0x00,
        },
    )
    # Blue slot
    emu.add(
        "",
        0,
        run_function=blue_slot,
        function_args={
            "mem": mem,
            "hmds_mem": hmds_mem,
            "item": 0x0136,
            "quantity": 0x10,
            "quality": 0x01,
        },
    )
    # Bag
    emu.add(
        "",
        0,
        run_function=bag,
        function_args={
            "mem": mem,
            "hmds_mem": hmds_mem,
            "x_bag": 4,
            "y_bag": 2,
            "item": 0x00BE,
            "quantity": 0x10,
            "quality": 0x00,
        },
    )
    emu.add(
        "",
        0,
        run_function=bag,
        function_args={
            "mem": mem,
            "hmds_mem": hmds_mem,
            "x_bag": 1,
            "y_bag": 2,
            "item": 0x0035,
            "quantity": 0x50,
            "quality": 0x00,
        },
    )
    emu.add("", 10, xpos=10, ypos=115)
    emu.add("", 1)

    emu.run()

    del emu


if __name__ == "__main__":

    main()
