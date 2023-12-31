from dataclasses import dataclass

from pymem import Pymem

from loguru import logger

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

    def show_all_item(self):
        num = self.get_num()
        if num > 0:
            for i in range(num):
                id_ = self.get_by_index(i).id_
                name_ = self.get_by_index(i).name_

                logger.debug(f"id: {id_} | name: {name_}")
        else:
            logger.error("RoleSkin dump失败!")
