import time

def workload(n):
    s = 0.
    for a in range(n):
        s += 1./(a+1)
    return s

def main():
    count = 100000000
    start = time.perf_counter(), time.process_time()
    workload(count)
    stop = time.perf_counter(), time.process_time()
    print(f'cpu time = {stop[0] - start[0]}, world time = {stop[1]-start[1]}')

if __name__=='__main__':
    main()
