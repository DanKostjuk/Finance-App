import bisect

f = open("word_frequency.txt", "r")
freq_words = f.readlines()
f.close()
hash_table = {}
for i in range(len(freq_words)):
    hash_table[freq_words[i]] = i


def sugessted_words(string_to_find: str, path_to_dictionary: str) -> list:
    """

    :param string_to_find:
    finding pprefix
    :param path_to_dictionary:
    :return:
    all words that starts with prefix string_to_find
    """
    string_to_find = string_to_find.lower()
    f = open(path_to_dictionary, "r")
    lines = f.readlines()
    f.close()
    lines.sort()
    string_to_find_len = len(string_to_find)
    left = bisect.bisect_left([x[:string_to_find_len] for x in lines], string_to_find)
    right = bisect.bisect_right([x[:string_to_find_len] for x in lines], string_to_find)

    ans = lines[left:right]
    ans.sort(key=lambda x: int(hash_table[x]))
    return ans

    # python moment xD
    # left, right = 0, len(lines)
    # while left < right:
    #     mid = (left + right) // 2
    #     if lines[mid][:string_to_find_len] < string_to_find:
    #         left = mid + 1
    #     else:
    #         right = mid
    #
    # first_id = left
    # left, right = 0, len(lines)
    # while left < right:
    #     mid = (left + right) // 2
    #     if lines[mid][:string_to_find_len] <= string_to_find:
    #         left = mid + 1
    #     else:
    #         right = mid
    #
    # second_id = left
    # return lines[first_id:second_id]

