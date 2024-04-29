import sys
from collections import defaultdict

def mapper(text):
    for word in text.split():
        yield (word, 1)

def reducer(mapped_values):
    reduction = defaultdict(int)
    for key, value in mapped_values:
        reduction[key] += value
    return reduction

def main():
    sys.argv.append('local_file.txt')

    if len(sys.argv) != 2:
        print("Usage: python local_word_count.py <file>")
        sys.exit(1)
        
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        text = file.read().lower()
    
    mapped_values = list(mapper(text))
    reduced_values = reducer(mapped_values)
    for word, count in sorted(reduced_values.items()):
        print(f'{word}: {count}')

if __name__ == '__main__':
    main()
