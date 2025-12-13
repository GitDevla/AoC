import importlib
from utils.utils import benchmark, read_file


def run_day_part(day, part):
    d = importlib.import_module(f"day{day:02d}.run")
    input = read_file(d.FILE)
    ans, time = 0, 0
    if hasattr(d, "parse"):
        input = d.parse(input)
    if part == 1:
        time, ans = benchmark(lambda: d.task1(input), True)
    elif part == 2:
        time, ans = benchmark(lambda: d.task2(input), True)
    return ans, time


days = {}
for i in range(1, 13):
    for j in range(1, 3):
        try:
            ans, time = run_day_part(i, j)
            if i not in days:
                days[i] = []
            days[i].append(ans)
            days[i].append(time)
        except:
            raise Exception(f"Error in day {i} part {j}")


def generate_markdown_table(headers, rows):
    markdown_table = "| " + " | ".join(headers) + " |\n"
    markdown_table += "| " + " | ".join(["---"] * len(headers)) + " |\n"
    for row in rows:
        markdown_table += "| " + " | ".join(map(str, row)) + " |\n"
    return markdown_table


# Example usage
headers = ["Day", "Part 1 Answer", "Part 1 Runtime", "Part 2 Answer", "Part 2 Runtime"]
rows = []
for day, values in days.items():
    values[1] = f"{values[1]:.3f}s"
    values[3] = f"{values[3]:.3f}s"
    rows.append([day, *values])

markdown_table = generate_markdown_table(headers, rows)
print(markdown_table)
