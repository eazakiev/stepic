text = input().split("-")
if "".join(text).isdigit():
    if text[0] == "7":
       del text[0]
    if len(text[0]) == 3 and len(text[1]) == 3 and len(text[2]) == 4:
        print("YES")
    else:
        print("NO")
else:
    print("NO")