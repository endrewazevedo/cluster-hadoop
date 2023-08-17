import sys
from collections import defaultdict

def reduce_function():
    current_word = None
    current_count = 0
    word_count = defaultdict(int)

    for line in sys.stdin:
        line = line.strip()
        word, count = line.split("\t")
        count = int(count)
        
        if current_word == word:
            current_count += count
        else:
            if current_word:
                word_count[current_word] += current_count
            current_word = word
            current_count = count
    
    if current_word:
        word_count[current_word] += current_count

    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    top_10 = sorted_word_count[:10]

    for word, count in top_10:
        print(f"{word}\t{count}")

if __name__ == "__main__":
    reduce_function()
