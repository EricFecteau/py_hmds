from emulator import emulator
from emulator import memory
from hmds import movie_functions as mf
from hmds import memory_addresses as ml
from hmds import action


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

    emu.add("U", 20)
    emu.add("A", 1)
    emu.add("BU", 50)

    emu.add("", 500)

    action.move_char_diff_screen(emu, mem, hmds_mem, 0x07, 20, 150)
    emu.add("", 120)

    action.move_char_diff_screen(emu, mem, hmds_mem, 0x27, 100, 110)
    emu.add("", 60)

    for i in range(0, 5):
        action.move_char_same_screen(emu, mem, hmds_mem, 80, 130)
        emu.add("D", 1)
        emu.add("", 10)

        action.move_char_same_screen(emu, mem, hmds_mem, 65, 150)
        emu.add("R", 1)
        emu.add("", 10)

        action.move_char_same_screen(emu, mem, hmds_mem, 80, 170)
        emu.add("U", 1)
        emu.add("", 10)

        action.move_char_same_screen(emu, mem, hmds_mem, 95, 150)
        emu.add("L", 1)
        emu.add("", 10)

    action.move_char_diff_screen(emu, mem, hmds_mem, 0x2E, 95, 125)
    emu.add("D", 1)
    emu.add("", 60)

    action.move_char_same_screen(emu, mem, hmds_mem, 60, 220)
    emu.add("R", 1)
    emu.add("", 60)

    action.move_char_diff_screen(emu, mem, hmds_mem, 0x2B, 183, 171)
    emu.add("D", 1)
    for i in range(0, 40):
        action.move_char_same_screen(emu, mem, hmds_mem, 183 + i, 171)
        emu.add("", 5)
        action.move_char_same_screen(emu, mem, hmds_mem, 183 - i, 171)
        emu.add("", 5)
    action.move_char_same_screen(emu, mem, hmds_mem, 183, 171)
    emu.add("", 60)

    action.move_char_diff_screen(emu, mem, hmds_mem, 0x05, 150, 100)
    emu.add("D", 1)
    emu.add("", 60)

    emu.run()

    del emu


if __name__ == "__main__":

    main()
