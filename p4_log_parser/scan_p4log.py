#!/tools/iccad/bin/python3.4
import argparse
import re
from collections import namedtuple

Lock = namedtuple("Lock",
        ("user", "command", "wait_read", "wait_write", "held_read",
            "held_write"))

class P4Info:
    """Represents p4.log file"""
    def __init__(self, p4_log):
        """Initialize by the entire parsing p4.log

        p4_log: path to p4.log
        """
        self.__db_locks = self.__get_db_locks(p4_log)

    def __get_db_locks(self, p4_log):
        """Return list of Lock

        p4_log: path to p4.log
        """
        #TODO
        # 1. Call __get_info_blocks(p4_log) to parse p4_log
        #    into list of info blocks
        # 2. For each info block, call __str2dblock(info_block)
        #    to convert str to Lock namedtuple
        # pass
        db_info_locks = []
        for i in self.get_info_blocks(p4_log):
            db_info_locks.append(self.__str2dblock(i))
        return db_info_locks

    def get_info_blocks(self, p4_log):
        """Return str block of Perforce server info

        p4_log: path to p4.log
        """
        #TODO
        # pass
        # lt = []
        with open(p4_log, 'r') as data:
            for line in data:
                if 'pid' in line:
                    yield line
        #             lt.append(line)
        # print(lt)

    def __str2dblock(self, info_block):
        """Convert str to Lock namedtuple
        
        info_block: p4 info block
        """
        #TODO
        pass

    def get_max_wait_read(self):
        """Return str of highest wait_read"""
        #TODO
        pass

    def get_max_wait_write(self):
        """Return str of highest wait_write"""
        #TODO

    def get_max_held_read(self):
        """Return str with highest held_read"""
        #TODO


    def get_max_held_write(self):
        """Return str with highest held_write"""
        #TODO


def main():
    parser = argparse.ArgumentParser(
            description="P4 log parser for Python Interview",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("p4log", type=str, help="p4.log file to parse")
    args = parser.parse_args()
    p4info = P4Info(args.p4log)
    # print(p4info.get_max_wait_read())
    # print(p4info.get_max_wait_write())
    # print(p4info.get_max_held_read())
    # print(p4info.get_max_held_write())

# if __name__ == "__main__": main()

P4Info("p4.log").get_info_blocks("p4.log")