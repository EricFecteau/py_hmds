"""Main entry point to exploring HMDS"""

from emulator import emulator
from hmds import movie_functions as mf
from hmds import memory_locations as ml


def main() -> None:

    """Main function"""

    emu = emulator.Emulator(
        nds="D:\\Dropbox\\Speed Run\\py_hmds\\roms\\HMDS\\NA\\0561 - Harvest Moon DS (U)(Legacy).nds",
        author="Eric Fecteau",
        movie="D:\\Dropbox\\Speed Run\\py_hmds\\movies\\HMDS.dsm",
        save_path="D:\\Dropbox\\Speed Run\\py_hmds\\saves\\",
        frontend=True,
    )

    emu.initialize_emulator(scale=2, rightscreen=False)

    mem = ml.MemoryLocations("ABCEN0J12")

    mem.get_mem_loc("rng")

    # mf.intro(emu)
    # emu.save("intro.ds0")

    # emu.load("intro.ds0")

    # emu.run()


if __name__ == "__main__":

    main()
