"""Manage HMDS memory locations"""


class MemoryLocations:

    """Get the memory location by name of memory."""

    def __init__(self, version) -> None:

        # Verison NA 1.0 (aka "0561 - Harvest Moon DS (U)(Legacy)")
        if version == "ABCEN0J12" or version == "ABCEN0J20" or version == "ABCEN0J34":
            self.version = 0

        self.mem_loc: dict = {"rng": [0x02193010]}

    def get_mem_loc(self, mem_name):

        """Get the memory location, based on the name, for different versions."""

        return self.mem_loc[mem_name][self.version]
