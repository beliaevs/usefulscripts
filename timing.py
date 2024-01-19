import time

def workload(n):
    s = 0.
    for a in range(n):
        s += 1./(a+1)
    return s

def main():
    start = time.perf_counter()
    workload(10000000)
    stop = time.perf_counter()
    print(f'cpu time = {stop - start}')

if __name__=='__main__':
    main()
