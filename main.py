# python3

import heapq

def parallel_processing(n, m, data):
    output = []
    threads = [(0, i) for i in range(n)]
    heapq.heapify(threads)

    for i in range(m):
        ti = data[i]
        start_time, thread_idx = heapq.heappop(threads)
        output.append((thread_idx, start_time))
        heapq.heappush(threads, (start_time + ti, thread_idx))

    return output

def print_grid(n, m, result):
    grid = [[' ' for j in range(m)] for i in range(n)]
    for i in range(m):
        thread_idx, start_time = result[i]
        grid[thread_idx][i] = '*'
    for j in range(m):
        print('--', end='')
    print('-')
    for i in range(n):
        for j in range(m):
            print(f'|{grid[i][j]}', end='')
        print('|')
        for j in range(m):
            print('--', end='')
        print('-')

def main():
    n, m = 3, 6 # Hard-coded input values
    data = [2, 4, 3, 2, 1, 3] # Hard-coded input values

    result = parallel_processing(n, m, data)

    for i, j in result:
        print(i,j)

if __name__ == "__main__":
    main()