import text_helper


def input_with_help(description: str) -> str:
    word = input(description)
    suggested_words = text_helper.sugessted_words(word, "word_frequency.txt")
    # print(suggested_words)
    i = 0
    while i < len(suggested_words) and i < 5:
        print(suggested_words[i][:-1] + "[" + f"{i + 1}" + "]", end=" ")
        # print("["+f"{i+1}"+"]", end="\0")
        i += 1
    print("\n" + word, end="")
    num = input()
    if num.isdigit() and int(num) <= 5:
        return suggested_words[int(num) - 1]
    else:
        while len(suggested_words) > 1:
            # print(word, end="\0")
            word += num
            suggested_words = text_helper.sugessted_words(word, "word_frequency.txt")
            i = 0
            while i < len(suggested_words) and i < 5:
                print(suggested_words[i][:-1] + "[" + f"{i + 1}" + "]", end=" ")
                i += 1
            print("\n" + word, end="")
            num = input()
            if num.isdigit() and int(num) <= 5:
                return suggested_words[int(num) - 1]
