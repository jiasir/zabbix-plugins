__author__ = 'Taio'

import psutil
import datetime


def users():
    return psutil.users()


def boot_time():
    boot_time = psutil.boot_time()
    time_format = datetime.datetime.fromtimestamp(boot_time).strftime("%Y-%m-%d %H:%M:%S")
    return time_format


def main():
    print 'users: {}'.format(users())
    print 'boot time: {}'.format(boot_time())


if __name__ == '__main__':
    main()