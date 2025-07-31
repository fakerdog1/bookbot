from stats import get_word_count

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    
    return text
        

text = get_book_text('./books/frankenstein.txt')
count = get_word_count(text)
print(f'{count} words found in the document')