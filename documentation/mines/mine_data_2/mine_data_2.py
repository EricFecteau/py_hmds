"""Collect all the data from each floor of the mine"""

import csv

from emulator import emulator
from emulator import memory

from hmds import movie_functions as mf  # pylint: disable=unused-import
from hmds import memory_addresses as ml
from hmds import memory_func

COL_NAMES = [
    "attempt",
    "mine_num",
    "floor_num",
    "no rock",
    "empty rock",
    "junk ore",
    "copper",
    "silver",
    "gold",
    "mystrile",
    "pink diamond",
    "alexandrite",
    "moon stone",
    "sand rose",
    "diamond",
    "emerald",
    "ruby",
    "topaz",
    "peridot",
    "fluorite",
    "agate",
    "amethyst",
    "spring sun",
    "summer sun",
    "fall sun",
    "winter sun",
    "mythic stone",
    "adamantite",
    "orichalc",
    "blue wonderful",
    "green wonderful",
    "red wonderful",
    "yellow wonderful",
    "orange wonderful",
    "purple wonderful",
    "indigo wonderful",
    "black wonderful",
    "white wonderful",
    "empty tile",
    "down stairs",
    "covered hole",
    "money bag",
    "black grass",
    "tiled square",
    "unearthed hole",
    "staircase up",
    "staircase down",
    "lithograph",
    "cursed tool",
    "cursed accessory",
    "bronze coin",
    "silver coin",
    "gold coin",
]


def min_move_to_mine(
    emu: emulator.Emulator,
    mem: memory.Memory,
    hmds_mem: ml.MemoryAddresses,
    screen_loc: int,
    xpos: int,
    ypos: int,
    min_frame: int,
) -> None:  # pylint: disable=too-many-arguments

    """Move the character anywhere in the game (minimum frames to have mine data)"""

    def force_location(
        mem: memory.Memory,
        hmds_mem: ml.MemoryAddresses,
        screen_loc: int,
        xpos: int,
        ypos: int,
    ):
        size, addr = hmds_mem.get_mem_addr("screen_loc")
        mem.write(addr, size, screen_loc)

        size, addr = hmds_mem.get_mem_addr("char_x_write")
        mem.write(addr, size, xpos * 256)

        size, addr = hmds_mem.get_mem_addr("char_y_write")
        mem.write(addr, size, ypos * 256)

    # Trigger screen transition
    def trigger_transition(mem: memory.Memory, hmds_mem: ml.MemoryAddresses):

        size, addr = hmds_mem.get_mem_addr("trigger_0")
        mem.write(addr, size, 0)

        size, addr = hmds_mem.get_mem_addr("trigger_1")
        mem.write(addr, size, 1)

    emu.add(
        "",
        1,
        run_function=trigger_transition,
        function_args={
            "mem": mem,
            "hmds_mem": hmds_mem,
        },
    )
    emu.add(
        "",
        min_frame,
        run_function=force_location,
        function_args={
            "mem": mem,
            "hmds_mem": hmds_mem,
            "screen_loc": screen_loc,
            "xpos": xpos,
            "ypos": ypos,
        },
    )


def ready_scene(
    mem: memory.Memory, hmds_mem: ml.MemoryAddresses, mine_num: int, floor_num: int
) -> None:

    """Get the scene ready (select mine number and floor number)"""

    size, addr = hmds_mem.get_mem_addr("mine_num")
    mem.write(addr, size, mine_num)

    size, addr = hmds_mem.get_mem_addr("mine_floor_num")
    mem.write(addr, size, floor_num)


def get_floor(
    mem: memory.Memory,
    hmds_mem: ml.MemoryAddresses,
    mine_items: list,
    attempt: int,
    mine_num: int,
    floor_num: int,
) -> None:  # pylint: disable=too-many-arguments

    """Get all the data from the floor the character is currently on"""

    mine_items.append(memory_func.summarize_mine_floor(mem, hmds_mem))
    mine_items[-1]["attempt"] = str(attempt)
    mine_items[-1]["mine_num"] = str(mine_num)
    mine_items[-1]["floor_num"] = str(floor_num)


def start_csv(mine_num: int):

    """Set up the CSV file"""

    with open(
        f"./documentation/mines/mine_data_{mine_num}/mine_data_{mine_num}.csv",
        "w",
        newline="",
        encoding="utf-8",
    ) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=COL_NAMES)
        writer.writeheader()


def send_to_csv(mine_num: int, mine_items: list):

    """Add data to CSV file"""

    with open(
        f"./documentation/mines/mine_data_{mine_num}/mine_data_{mine_num}.csv",
        "a+",
        newline="",
        encoding="utf-8",
    ) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=COL_NAMES)
        writer.writerows(mine_items)

    mine_items.clear()


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

    # mf.intro(emu)
    # emu.save("intro.ds0")

    emu.load("intro.ds0")

    emu.add("BU", 20)
    emu.add("A", 1)
    emu.add("", 24)

    emu.save("temp.ds0")

    emu.load("temp.ds0")

    mine_items: list[dict] = []
    mine_num = 2  # indexed to one
    max_floor = 255  # indexed to one
    attempts = 100  # per floor

    emu.add(
        "",
        0,
        run_function=start_csv,
        function_args={"mine_num": mine_num},
    )

    for floor in range(1, max_floor + 1):
        for attempt in range(0, attempts):

            emu.load("temp.ds0")

            # To speed up everything, so that we are not waiting forever when there are 1000 attempts
            if attempt % 25 == 0:
                emu.add("", 25)
                emu.save("temp.ds0")
            else:
                emu.add("", attempt % 25)

            emu.add(
                "",
                0,
                run_function=ready_scene,
                function_args={
                    "mem": mem,
                    "hmds_mem": hmds_mem,
                    "mine_num": mine_num - 1,
                    "floor_num": floor,
                },
            )

            min_move_to_mine(
                emu=emu,
                mem=mem,
                hmds_mem=hmds_mem,
                screen_loc=0x3F,
                xpos=130,
                ypos=205,
                min_frame=16,
            )

            emu.add(
                "",
                0,
                run_function=get_floor,
                function_args={
                    "mem": mem,
                    "hmds_mem": hmds_mem,
                    "mine_items": mine_items,
                    "mine_num": mine_num,
                    "floor_num": floor,
                    "attempt": attempt,
                },
            )

        emu.add(
            "",
            0,
            run_function=send_to_csv,
            function_args={
                "mine_items": mine_items,
                "mine_num": mine_num,
            },
        )

    emu.run()

    del emu


if __name__ == "__main__":

    main()
