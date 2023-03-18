# python3

def parallel_processing(n, m, data):
    output = []
    threads = [(0, i) for i in range(n)]

    for i in range(m):
        task_time = data[i]
        start_time, thread_idx = threads[0]
        output.append((thread_idx, start_time))
        threads[0] = (start_time + task_time, thread_idx)

        j = 0
        while True:
            left_child = 2 * j + 1
            right_child = 2 * j + 2

            if left_child >= n:
                break

            min_child = left_child
            if right_child < n and threads[right_child][0] < threads[left_child][0]:
                min_child = right_child

            if threads[min_child][0] < threads[j][0]:
                threads[j], threads[min_child] = threads[min_child], threads[j]
                j = min_child
            else:
                break

        next_thread = min(threads)
        threads[next_thread[1]] = (next_thread[0] + task_time, next_thread[1])
        output.append((next_thread[1], next_thread[0]))

    return output


def print_grid(n, m, result):
    for j in range(m):
        for i in range(n):
            print(result[j * n + i][0], result[j * n + i][1])


def main():
    w, c = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(w, c, data)
    print_grid(w, c, result)


if __name__ == "__main__":
    main()