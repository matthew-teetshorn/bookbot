def get_num_words(data):
    data_list = data.split()
    return len(data_list)

def get_char_count(data):
    lower_data = data.lower()
    letter_count = {}

    for i in range(0, len(lower_data)):
        c = lower_data[i]
        if c in letter_count:
            letter_count[c] += 1
        else:
            letter_count[c] = 1
    
    return letter_count

def sort_dict_helper(items):
    return items["num"]

def sort_dict(dict):
    dict_list = []

    for key in dict:
        dict_list.append({"char": key, "num": dict[key]})

    dict_list.sort(reverse=True, key=sort_dict_helper)

    return dict_list