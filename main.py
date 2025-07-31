from stats import get_num_count, get_word_count, get_sorted_dict

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    
    return text
        

text = get_book_text('books/frankenstein.txt')
count = get_num_count(text)
# print(f'{count} words found in the document')
word_count = get_word_count(text)
# print(word_count)
sorted_word_count = get_sorted_dict(word_count)

print('============ BOOKBOT ============')
print('Analyzing book found at books/frankenstein.txt...')
print('----------- Word Count ----------')
print(f'Found {count} total words')
print('--------- Character Count -------')
for key, value in sorted_word_count.items():
    if key.isalpha():
        print(f'{key}: {value}')