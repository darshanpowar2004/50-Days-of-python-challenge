def word_index(element : list):
    temp_dict = {}
    for i in range(len(element)):
        if len(element[i]) > len(element[i-1]):
            temp_dict[len(element[i])] = i

    if not temp_dict:
        return 0


    longest_len = max(temp_dict.keys())
    return temp_dict.get(longest_len)




if __name__ == '__main__':
    words1 = ["Hate", "remorse", "vengeance"]
    words2 = ["Love", "Hate"]
    print(word_index(words2))
    print(word_index(words1))
