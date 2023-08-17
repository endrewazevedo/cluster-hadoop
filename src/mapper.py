import sys

def map_function():
    word_counts = {} 

    for line in sys.stdin:
        line = line.strip()
        words = line.split()
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    for word, count in word_counts.items():
        print(f"{word}\t{count}")

if __name__ == "__main__":
    map_function()
