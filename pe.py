from pefile import PE


def get_export_func_rva(pe: PE, func_name: str) -> int:
    if hasattr(pe, "DIRECTORY_ENTRY_EXPORT"):
        for i in getattr(pe, "DIRECTORY_ENTRY_EXPORT").symbols:
            if func_name == i.name.decode():
                return i.address
    return 0
