def read_file(path: str):
    f = open(path, "r")
    lines = f.readlines()
    lines = [x.strip() for x in lines]
    return lines


def read_file_raw(path: str):
    f = open(path, "r")
    lines = f.readlines()
    lines = [x for x in lines]
    return lines


def read_test(string: str):
    lines = string.splitlines()
    lines = [x for x in lines]
    return lines


def test(output, expected):
    from colorama import Fore

    if output != expected:
        raise Exception(
            f"{Fore.RED}Error: got {Fore.WHITE}{output}{Fore.RED}, expected {Fore.WHITE}{expected}"
        )


def benchmark(fn, silent=False):
    from timeit import default_timer

    start_time = default_timer()
    ans = fn()
    elapsed = default_timer() - start_time
    if not silent:
        print(f"Elapsed: {format(elapsed, '.4f')}s")
    return elapsed, ans
