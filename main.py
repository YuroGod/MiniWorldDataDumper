from roleskin import RoleSkin
from manager import InstanceManager

from pymem import Pymem

if __name__ == '__main__':
    pm = Pymem("MiniGameApp.exe")

    instanceMgr = InstanceManager(pm)

    roleskin = RoleSkin(pm, instanceMgr.get("RoleSkin"))

    num = roleskin.get_num()
    print(f"num: {num}")

    for i in range(num):
        id_ = roleskin.get_by_index(i).id_
        name_ = roleskin.get_by_index(i).name_
        print(f"id: {id_} | name: {name_}")

    pm.close_process()
