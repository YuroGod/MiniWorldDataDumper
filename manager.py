import pe

from pymem import Pymem
from pymem.process import module_from_name

from loguru import logger


class InstanceManager:
    def __init__(self, pymem: Pymem):
        self.pm = pymem
        self.libiworld = 0
        self.libiworld_path = ""
        self.inst = {}

        self.init()

    def init(self):
        self.libiworld = module_from_name(self.pm.process_handle, "libiworld.dll").lpBaseOfDll
        self.libiworld_path = module_from_name(self.pm.process_handle, "libiworld.dll").filename

        logger.info(f"解析PE中...")
        libiworld_pe = pe.PE(self.libiworld_path)  # 速度有点慢ahh
        logger.success(f"PE解析完成")

        # RoleSkinCsv::getInstance
        rva = pe.get_export_func_rva(libiworld_pe, "?getInstance@RoleSkinCsv@@SAPAV1@XZ")
        addr = self.pm.read_int(self.libiworld + rva + 1)
        self.inst["RoleSkin"] = self.pm.read_int(addr)

        # TODO: ItemDef, MonsterDef...

    def get(self, name) -> int:
        if name in self.inst:
            return self.inst.get(name)
        return 0
