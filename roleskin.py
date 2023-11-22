from dataclasses import dataclass

from pymem import Pymem


@dataclass
class RoleSkinDef:
    id_: int
    name_: str


class RoleSkin:
    def __init__(self, pymem: Pymem, inst: int):
        self.pm = pymem
        self.instance = inst

        self.first = self.pm.read_int(self.instance + 0x8)
        self.second = self.pm.read_int(self.instance + 0xC)

    def get_num(self) -> int:
        return (self.second - self.first) >> 2

    def get_by_index(self, index: int) -> RoleSkinDef:
        roleskindef = self.pm.read_int(self.first + index * 0x4)
        id_ = self.pm.read_int(roleskindef)
        name_ = self.pm.read_string(roleskindef + 0x4)
        return RoleSkinDef(id_, name_)
