text = input() # affective
if "f" not in text:
    print("-2")
elif text.count("f") == 1:
    print("-1")
else:
    print(text.find("f", text.find("f") + 1))


