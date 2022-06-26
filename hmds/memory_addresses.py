"""Manage HMDS memory addresses"""


class MemoryAddresses:

    """Get the memory addresses by name of memory."""

    def __init__(self, version: str) -> None:

        self.version = version

        self.mem_loc: dict = {
            # RNG
            "rng": [4, {"NA1.0": 0x02193010}],
            # Items and inventory
            "red_slot": [4, {"NA1.0": 0x023D6B10}],
            "green_slot": [4, {"NA1.0": 0x023D6B14}],
            "blue_slot": [4, {"NA1.0": 0x023D6B18}],
            "bag": [4, {"NA1.0": 0x023D6B28}],
            "item_price": [4, {"NA1.0": 0x0215AB28}],
            # Character location and screen
            "char_loc": [1, {"NA1.0": 0x023D7AD8, "NA1.1": 0x023D7AD4}],
            "screen_loc": [1, {"NA1.0": 0x023D3AC0, "NA1.1": 0x023D3AB0}],
            "screen_x0": [1, {"NA1.0": 0x023D3E71}],
            "screen_x1": [1, {"NA1.0": 0x023D3E72}],
            "screen_y0": [1, {"NA1.0": 0x023D3E75}],
            "screen_y1": [1, {"NA1.0": 0x023D3E76}],
            "char_x_read": [2, {"NA1.0": 0x023D7AD4}],
            "char_y_read": [2, {"NA1.0": 0x023D7AD6}],
            "char_x_write": [4, {"NA1.0": 0x23D37B8}],
            "char_y_write": [4, {"NA1.0": 0x23D37BC}],
            "trigger_0": [2, {"NA1.0": 0x23D31F0}],
            "trigger_1": [1, {"NA1.0": 0x23D31E8}],
            # Mines
            "mine_floor_num": [1, {"NA1.0": 0x023DBD2E, "NA1.1": 0x023DBD2A}],
            "floor_x_size": [1, {"NA1.0": 0x022C3EC4, "NA1.1": 0x022C6C84}],
            "floor_y_size": [1, {"NA1.0": 0x022C3EC5, "NA1.1": 0x022C6C86}],
            "floor_data_array": [1, {"NA1.0": 0x023DB964, "NA1.1": 0x023DB960}],
            # NPC
            "npc_info": [0, {"NA1.0": 0x023DBD30}],
            "npc_loc": [0, {"NA1.0": 0x023D7AE0}],
        }

        self.npc_table: dict = {
            "player_char": 0,
            "Celia": 1,
            "Muffy": 2,
            "Nami": 3,
            "Romana": 4,
            "Sebastian": 5,
            "Lumina": 6,
            "Wally": 7,
            "Chris": 8,
            "Grant": 9,
            "Kate": 10,
            "Hugh": 11,
            "Carter": 12,
            "Flora": 13,
            "Vesta": 14,
            "Marlin": 15,
            "Ruby": 16,
            "Rock": 17,
            "Dr. Hardy": 18,
            "Galen": 19,
            "Nina": 20,
            "Daryl": 21,
            "Cody": 22,
            "Gustafa": 23,
            "Griffin": 24,
            "Vans": 25,
            "Kassey": 26,
            "Patrick": 27,
            "Murrey": 28,
            "Takakura": 29,
            "Kai": 39,
            "Harvest Goddess": 44,
            "Thomas": 45,
            "Gotz": 46,
            "Leia": 48,
            "Keira": 49,
            "Witch Princess": 50,
        }

        self.npc_info: dict = {
            "loc": {"addr_add": 0, "addr_size": 1},
            "entrance_loc": {"addr_add": 1, "addr_size": 1},
            "prev_loc": {"addr_add": 2, "addr_size": 1},
            "exit_prev_loc": {"addr_add": 3, "addr_size": 1},
            "fp": {"addr_add": 4, "addr_size": 1},
            "interact": {"addr_add": 5, "addr_size": 2},
            "lp": {"addr_add": 9, "addr_size": 2},
            "path": {"addr_add": 20, "addr_size": 0},
            "path_timer": {"addr_add": 28, "addr_size": 2},
            "bump_timer": {"addr_add": 32, "addr_size": 2},
        }

    def get_mem_addr(self, mem_name: str) -> tuple[int, int]:

        """Get the memory addresses, based on the name, for different versions."""

        return (self.mem_loc[mem_name][0], self.mem_loc[mem_name][1][self.version])

    def get_npc_addr(self, npc_name: str, mem_name: str = "") -> tuple[int, int]:

        """Get the memory addresses of the npc, based on the name of the npc and memory name."""

        size, addr = self.get_mem_addr("npc_info")
        addr = addr + (self.npc_table[npc_name] * 40)

        if mem_name == "":
            return (size, addr)

        size, addr = (
            self.npc_info[mem_name]["addr_size"],
            addr + self.npc_info[mem_name]["addr_add"],
        )
        return (size, addr)
