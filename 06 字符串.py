come_char = input()


# 判断字符串
def get_num_and_char(s):
    char_list = [i for i in s if not i.isdigit()]
    num_list = [i for i in s if i.isdigit()]
    return char_list + num_list


ans = get_num_and_char(come_char)
print("".join(ans))
