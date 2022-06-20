#
# main.py
# @author yanchunhuo
# @description 
# @created 2022-06-20T16:47:17.702Z+08:00
# @last-modified 2022-06-20T17:55:49.973Z+08:00
# github https://github.com/yanchunhuo

from delete_logs import Delete_Logs
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--server', help='指定执行的主机', type=str)
    args = parser.parse_args()
    server=args.server
    delete_logs=Delete_Logs(specify_host=server)
    delete_logs.run()