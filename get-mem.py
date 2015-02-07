#!/usr/local/env python
__author__ = 'Taio'


import psutil


def main():
    mem = psutil.virtual_memory()
    print('total:{}MB, used:{}MB').format(mem.total / 1000000, mem.used / 1000000)


if __name__ == '__main__':
    main()