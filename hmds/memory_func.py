"""Various memory functions (pull data from the game)"""

from emulator import memory
from emulator import tools

from hmds import memory_addresses as ml


def summarize_mine_floor(
    mem: memory.Memory, hmds_mem: ml.MemoryAddresses
) -> dict[str, int]:

    """Pull data from the mine floor"""

    mine_items = {
        "no rock": 0,
        "empty rock": 0,
        "junk ore": 0,
        "copper": 0,
        "silver": 0,
        "gold": 0,
        "mystrile": 0,
        "pink diamond": 0,
        "alexandrite": 0,
        "moon stone": 0,
        "sand rose": 0,
        "diamond": 0,
        "emerald": 0,
        "ruby": 0,
        "topaz": 0,
        "peridot": 0,
        "fluorite": 0,
        "agate": 0,
        "amethyst": 0,
        "spring sun": 0,
        "summer sun": 0,
        "fall sun": 0,
        "winter sun": 0,
        "mythic stone": 0,
        "adamantite": 0,
        "orichalc": 0,
        "blue wonderful": 0,
        "green wonderful": 0,
        "red wonderful": 0,
        "yellow wonderful": 0,
        "orange wonderful": 0,
        "purple wonderful": 0,
        "indigo wonderful": 0,
        "black wonderful": 0,
        "white wonderful": 0,
        "empty tile": 0,
        "down stairs": 0,
        "covered hole": 0,
        "money bag": 0,
        "black grass": 0,
        "tiled square": 0,
        "unearthed hole": 0,
        "staircase up": 0,
        "staircase down": 0,
        "lithograph": 0,
        "cursed tool": 0,
        "cursed accessory": 0,
        "bronze coin": 0,
        "silver coin": 0,
        "gold coin": 0,
    }

    size, addr = hmds_mem.get_mem_addr("floor_x_size")
    x_size = mem.read(addr, size, False)

    size, addr = hmds_mem.get_mem_addr("floor_y_size")
    y_size = mem.read(addr, size, False)

    size, addr = hmds_mem.get_mem_addr("mine_num")
    mine_num = mem.read(addr, size, False)

    size, addr = hmds_mem.get_mem_addr("floor_data_array")
    mine_array = [
        list(item)
        for item in tools.hex_list(
            mem.read_array(addr, x_size * y_size, size, False), "{:02x}"
        )
    ]

    for tiles in mine_array:
        rock = tiles[0]  # most significant bits
        tiled = tiles[1]  # least significant bits

        if rock == "0":
            mine_items["no rock"] += 1
        elif rock == "1":
            mine_items["empty rock"] += 1
        elif rock == "2":
            mine_items["junk ore"] += 1
        elif rock == "3" and (mine_num == 0 or mine_num == 2):
            mine_items["copper"] += 1
        elif rock == "4" and (mine_num == 0 or mine_num == 2):
            mine_items["silver"] += 1
        elif rock == "5" and (mine_num == 0 or mine_num == 2):
            mine_items["gold"] += 1
        elif rock == "6" and (mine_num == 0 or mine_num == 2):
            mine_items["mystrile"] += 1
        elif rock == "3" and mine_num == 1:
            mine_items["pink diamond"] += 1
        elif rock == "4" and mine_num == 1:
            mine_items["alexandrite"] += 1
        elif rock == "5" and mine_num == 1:
            mine_items["moon stone"] += 1
        elif rock == "6" and mine_num == 1:
            mine_items["sand rose"] += 1
        elif rock == "7" and mine_num == 1:
            mine_items["diamond"] += 1
        elif rock == "8" and mine_num == 1:
            mine_items["emerald"] += 1
        elif rock == "9" and mine_num == 1:
            mine_items["ruby"] += 1
        elif rock == "a" and mine_num == 1:
            mine_items["topaz"] += 1
        elif rock == "b" and mine_num == 1:
            mine_items["peridot"] += 1
        elif rock == "c" and mine_num == 1:
            mine_items["fluorite"] += 1
        elif rock == "d" and mine_num == 1:
            mine_items["agate"] += 1
        elif rock == "e" and mine_num == 1:
            mine_items["amethyst"] += 1
        elif rock == "7" and mine_num == 2:
            mine_items["spring sun"] += 1
        elif rock == "8" and mine_num == 2:
            mine_items["summer sun"] += 1
        elif rock == "9" and mine_num == 2:
            mine_items["fall sun"] += 1
        elif rock == "a" and mine_num == 2:
            mine_items["winter sun"] += 1
        elif rock == "b" and mine_num == 2:
            mine_items["mythic stone"] += 1
        elif rock == "c" and mine_num == 2:
            mine_items["adamantite"] += 1
        elif rock == "d" and mine_num == 2:
            mine_items["orichalc"] += 1
        elif rock == "3" and mine_num == 3:
            mine_items["blue wonderful"] += 1
        elif rock == "4" and mine_num == 3:
            mine_items["green wonderful"] += 1
        elif rock == "5" and mine_num == 3:
            mine_items["red wonderful"] += 1
        elif rock == "6" and mine_num == 3:
            mine_items["yellow wonderful"] += 1
        elif rock == "7" and mine_num == 3:
            mine_items["orange wonderful"] += 1
        elif rock == "8" and mine_num == 3:
            mine_items["purple wonderful"] += 1
        elif rock == "9" and mine_num == 3:
            mine_items["indigo wonderful"] += 1
        elif rock == "a" and mine_num == 3:
            mine_items["black wonderful"] += 1
        elif rock == "b" and mine_num == 3:
            mine_items["white wonderful"] += 1

        if tiled == "0":
            mine_items["empty tile"] += 1
        if tiled == "1":
            mine_items["down stairs"] += 1
        if tiled == "2":
            mine_items["covered hole"] += 1
        if tiled == "3":
            mine_items["money bag"] += 1
        if tiled == "4" and (mine_num in (0, 1, 2)):
            mine_items["black grass"] += 1
        if tiled == "5" and mine_num == 1:
            mine_items["lithograph"] += 1
        if tiled == "5" and mine_num == 2:
            mine_items["cursed tool"] += 1
        if tiled == "6" and mine_num == 2:
            mine_items["cursed accessory"] += 1
        if tiled == "4" and mine_num == 3:
            mine_items["bronze coin"] += 1
        if tiled == "5" and mine_num == 3:
            mine_items["silver coin"] += 1
        if tiled == "6" and mine_num == 3:
            mine_items["gold coin"] += 1
        if tiled == "7" and mine_num == 3:
            mine_items["black grass"] += 1
        if tiled == "8" and mine_num == 3:
            mine_items["lithograph"] += 1
        if tiled == "c":
            mine_items["tiled square"] += 1
        if tiled == "d":
            mine_items["unearthed hole"] += 1
        if tiled == "e":
            mine_items["staircase up"] += 1
        if tiled == "f":
            mine_items["staircase down"] += 1

    return mine_items
