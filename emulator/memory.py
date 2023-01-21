"""This module deals with reading and writing memory from DeSmuME"""

from emulator import tools


class Memory:

    """Read and write memory from DeSmuME"""

    def __init__(self, emulator) -> None:
        self.emu = emulator

        self.search_min = 0x02000000
        self.search_max = 0x023FFFFF

        self.search_list: list[list[int]] = []

    def read(self, address: int, size: int, signed: bool) -> int:

        """Read a 1, 2, 4 bytes from an address, signed or not"""

        return self.emu.emu.memory.read(address, address, size, signed)

    def read_array(
        self, address: int, array_size: int, size: int, signed: bool
    ) -> list[int]:

        """Read an array of 1, 2, 4 bytes from an array of data, signed or not"""

        array = list(
            self.emu.emu.memory.read(address, address + array_size, size, signed)
        )

        return array

    def write(self, address: int, size: int, val: int) -> None:

        """Write a 1, 2, 4 bytes to an address"""

        self.emu.emu.memory.write(address, address, size, [val])

    def return_search_list(self) -> list[str]:

        """Print the list as hex"""

        return tools.hex_list([x[0] for x in self.search_list])

    def mem_search(self, action: str, value: int, size: int, signed: bool):

        """Search the memory for a value"""

        if len(self.search_list) == 0 and action != "register":
            return False

        if action == "register":
            for mem in range(self.search_min, self.search_max, size):
                self.search_list.append([mem, self.read(mem, size, signed)])
            return False

        newlist: list[list[int]] = []
        for mem_list in self.search_list:
            new_value = self.read(mem_list[0], size, signed)
            if action == "==":
                if new_value == value:
                    newlist.append([mem_list[0], new_value])
            elif action == "+":
                if new_value == mem_list[1] + value:
                    newlist.append([mem_list[0], new_value])
            elif action == "-":
                if new_value == mem_list[1] - value:
                    newlist.append([mem_list[0], new_value])
            elif action == "!=":
                if new_value != mem_list[1]:
                    newlist.append([mem_list[0], new_value])

        self.search_list = newlist

        return False
