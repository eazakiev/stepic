def is_pangram(text):
    text = set(text)
    counter = 0
    abc = "abcdefghijklmnopqrstuvwxyz"
    for letter in text:
        if letter in abc:
            counter += 1
    return counter == 26


txt = input().lower()
print(is_pangram(txt))

