def read_file(path: str):
    f = open(path, "r")
    lines = f.readlines()
    lines = [x.strip() for x in lines]
    return lines


def test(output, expected):
    from colorama import Fore

    if output != expected:
        raise Exception(
            f"{Fore.RED}Error: got {Fore.WHITE}{output}{Fore.RED}, expected {Fore.WHITE}{expected}"
        )


def benchmark(fn):
    from timeit import default_timer

    start_time = default_timer()
    fn()
    elapsed = default_timer() - start_time
    print(f'Elapsed: {format(elapsed,".4f")}s')
