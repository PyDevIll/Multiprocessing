from multiprocessing import Process, Manager


def square_it(num, index, result):
    result[index] = num * num


def calculate_squares(num_list):
    with Manager() as manager:
        result = manager.list([None] * len(num_list))   # Создадим пустой список соотв. длины

        process_list = []
        # Передадим в каждый процесс еще и индекс, чтобы вычисленные значения были упорядочены
        for idx, num in enumerate(num_list):
            p = Process(target=square_it, args=(num, idx, result))
            process_list.append(p)
            p.start()

        for p in process_list:
            p.join()

        return list(result)


