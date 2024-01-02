from dumper import Dumper


if __name__ == '__main__':
    dumper = Dumper()
    if dumper.is_init_success():
        dumper.dump()
    dumper.close()
