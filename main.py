# python3

def parallel_processing(n, m, data):
    output = []
    finish_time = [0] * n
    for i, job_time in enumerate(data):
        min_finish_time = min(finish_time)
        min_thread = finish_time.index(min_finish_time)
        output.append((min_thread, min_finish_time))
        finish_time[min_thread] += job_time
    return output

def main():
    n, m = 3, 6 
    data = [2, 4, 3, 2, 1, 3] 

    result = parallel_processing(n, m, data)

    for i, j in result:
        print(i,j)

if __name__ == "__main__":
    main()