def operate_input(text):
    ans = ""
    for char in text:
        if char.isalpha():
            start = ord("a") if char.islower() else ord("A")
            new_char = chr((ord(char) - start + 3) % 26 + start)
            ans += new_char
        else:
            ans += char
    return ans


text = input()
print(operate_input(text))
