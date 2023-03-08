li = ["20", "23", "40"]
for i, n in enumerate(li):
    if "23" in li:
        li.remove("23")
        li.insert(i-1, "40")
print(li)
