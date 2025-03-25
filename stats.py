def num_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    
    return count

def char_appear(text):
    small = text.lower()
    char_dict = {}

    for char in small:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict

def sort_on(dictionaire):
    return dictionaire["count"]

def listing_dict(dictionaire):
    ls = []

    for key, value in dictionaire.items():
        ls.append({"char": key, "count": value})

    ls.sort(reverse=True, key=sort_on)
    return ls

