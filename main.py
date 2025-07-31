import sys
if not len(sys.argv) == 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

path_to_book = sys.argv[1]

from stats import get_num_count, get_word_count, get_sorted_dict

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    
    return text
        

text = get_book_text(path_to_book)
count = get_num_count(text)
# print(f'{count} words found in the document')
word_count = get_word_count(text)
# print(word_count)
sorted_word_count = get_sorted_dict(word_count)

print('============ BOOKBOT ============')
print(f'Analyzing book found at {path_to_book}...')
print('----------- Word Count ----------')
print(f'Found {count} total words')
print('--------- Character Count -------')
for key, value in sorted_word_count.items():
    if not key.isalpha():
        continue
    print(f'{key}: {value}')