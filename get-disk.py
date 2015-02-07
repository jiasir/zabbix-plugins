__author__ = 'Taio'

import psutil



def list_partitions(lst):
    for i in lst:
        for j in i:
            if not j.find('/'):
                part.append(j)
    return part


def usage(part):
    usage = psutil.disk_usage(part)
    return usage

def io(part):
    io = psutil.disk_io_counters(part)
    return io

part = []

def main():
    partitions = psutil.disk_partitions()
    lst = map(list, partitions)
    list_partitions(lst)
    
    for i in part:
        print i, ': ', usage(i), ',', io(i)
    


if __name__ == '__main__':
    main()