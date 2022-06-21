"""Manage HMDS memory addresses"""


class MemoryAddresses:

    """Get the memory addresses by name of memory."""

    def __init__(self, version: str) -> None:

        self.version = version

        self.mem_loc: dict = {
            "rng": [4, {"NA1.0": 0x02193010}],
            "char_loc": [1, {"NA1.0": 0x023D7AD8, "NA1.1": 0x023D7AD4}],
            "screen_loc": [1, {"NA1.0": 0x023D3AC0, "NA1.1": 0x023D3AB0}],
            "char_x": [1, {"NA1.0": 0x023D3E71}],
            "char_y": [1, {"NA1.0": 0x023D3E75}],
            "screen_x": [1, {"NA1.0": 0x023D7AD4}],
            "screen_y": [1, {"NA1.0": 0x023D7AD6}],
        }

    def get_mem_addr(self, mem_name: str) -> tuple[int, int]:

        """Get the memory addresses, based on the name, for different versions."""

        return (self.mem_loc[mem_name][0], self.mem_loc[mem_name][1][self.version])
