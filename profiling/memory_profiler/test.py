from memory_profiler import profile


# precision: 메모리를 소수점 몇 번째 자리까지 출력할 것인지
@profile(precision=3)
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


if __name__ == '__main__':
    my_func()
