from pymem import Pymem
from pymem.process import module_from_name


class InstanceManager:
    def __init__(self, pymem: Pymem):
        self.pm = pymem
        self.libiworld = 0
        self.inst = {}

        self.init()

    def init(self):
        self.libiworld = module_from_name(self.pm.process_handle, "libiworld.dll").lpBaseOfDll

        # TODO: 自动寻找实例地址
        self.inst["RoleSkin"] = self.pm.read_int(self.libiworld + 0xB30420)

        # TODO: ItemDef, MonsterDef...

    def get(self, name) -> int:
        if name in self.inst:
            return self.inst.get(name)
        return 0
