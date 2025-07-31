def get_num_count(text):
    arr = text.split()
    return len(arr)

def get_word_count(text):
    arr = text.split()
    return_dict = {}
    for word in text:
        word_lower = word.lower()
        if word_lower not in return_dict:
            return_dict[word_lower] = 1
            continue
        
        return_dict[word_lower] += 1
    
    return return_dict

def sort_on(items):
    return items["num"]

def get_sorted_dict(dict):
    new_dict = []
    for key, value in dict.items():
        new_dict.append({
            "char": key,
            "num": value
        })

    new_dict.sort(reverse=True, key=sort_on)

    return_dict = {}
    for item in new_dict:
        return_dict[item["char"]] = item["num"]

    return return_dict