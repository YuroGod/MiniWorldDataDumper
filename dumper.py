from pymem import *
from pymem.process import module_from_name

from roleskin import RoleSkin
from manager import InstanceManager

from loguru import logger


class Dumper:
    def __init__(self):
        self.pm = None
        self.libiworld = None
        self.instanceMgr = None
        self.init_success = False

        self.proc_name = "MiniGameApp.exe"

        if self.init_process():
            self.init_success = True
            logger.success("初始化进程信息成功!")
        else:
            logger.error("初始化进程信息失败, 请检查错误信息, 如无法解决请前往GitHub提交Issue")

    @logger.catch
    def init_process(self) -> bool:
        try:
            self.pm = Pymem(self.proc_name)
        except pymem.exception.ProcessNotFound:
            logger.error(f"未找到进程<{self.proc_name}>, 请检查是否启动游戏!")
            return False

        self.libiworld = module_from_name(self.pm.process_handle, "libiworld.dll").lpBaseOfDll

        logger.info(f"PID: {self.pm.process_id} | HPROCESS: {self.pm.process_handle}")

        self.instanceMgr = InstanceManager(self.pm)

        return True

    def is_init_success(self):
        return self.init_success

    @logger.catch
    def dump(self):
        roleskin_instance = self.instanceMgr.get("RoleSkin")
        roleskin = RoleSkin(self.pm, roleskin_instance)
        roleskin.show_all_item()

    def close(self):
        if self.pm is not None:
            self.pm.close_process()
        logger.info("程序已退出!")
