# reducer.py

import sys
from collections import defaultdict


def reduce_function():
    word_count = defaultdict(int)

    for line in sys.stdin:
        line = line.strip()
        word, count = line.split("\t")
        count = int(count)
        word_count[word] += count

    interval_counts = defaultdict(int)
    for count in word_count.values():
        interval = count // 10
        interval_counts[interval] += 1

    for interval, count in sorted(interval_counts.items()):
        print(f"I{interval} - {count}")


if __name__ == "__main__":
    reduce_function()
