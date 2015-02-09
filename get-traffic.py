__author__ = 'Taio'

import psutil


def net_io():
    return psutil.network_io_counters()


def main():
    print net_io()


if __name__ == '__main__':
    main()