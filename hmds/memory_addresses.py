"""Manage HMDS memory addresses"""


class MemoryAddresses:

    """Get the memory addresses by name of memory."""

    def __init__(self, version: str) -> None:

        # Verison NA 1.0 (aka "0561 - Harvest Moon DS (U)(Legacy)")
        if version == "ABCEN0J12" or version == "ABCEN0J20" or version == "ABCEN0J34":
            self.version = 0

        self.mem_loc: dict = {"rng": [0x02193010]}

    def get_mem_addr(self, mem_name: str) -> int:

        """Get the memory addresses, based on the name, for different versions."""

        return self.mem_loc[mem_name][self.version]
