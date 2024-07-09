import json
import random
import time

with open("Plus.json") as f:
    PLUS_DICT = json.load(f)

def plus(a, b):
    a, b = str(a), str(b)
    max_int = max(len(a.split(".")[0]), len(b.split(".")[0]))
    a += "." if "." not in a else ""
    b += "." if "." not in b else ""

    max_few = max(len(a.split(".")[1]), len(b.split(".")[1]))
    a_int, a_frac = a.split(".")
    b_int, b_frac = b.split(".")

    a_int, b_int = a_int.zfill(max_int), b_int.zfill(max_int)
    a_frac, b_frac = a_frac.ljust(max_few, '0'), b_frac.ljust(max_few, '0')

    a, b = a_int + a_frac, b_int + b_frac

    max_len = len(a)
    answer = []
    add = "0"

    for i in range(max_len - 1, -1, -1):
        cal = PLUS_DICT[f"{a[i]}+{b[i]}"]
        last_cal = cal[-1]
        last_cal = PLUS_DICT[f"{last_cal}+{add}"]
        if len(last_cal) > 1:
            add = PLUS_DICT[f"{cal[0]}+{last_cal[0]}"][0]
        elif len(cal) > 1:
            add = cal[0]
        else:
            add = "0"
        answer.insert(0, last_cal[-1])

    if add != "0":
        max_int += 1
        answer.insert(0, add)

    answer.insert(max_int, ".")
    
    while len(answer) > 1 and answer[0] == '0' and answer[1] != '.':
        answer.pop(0)
    if '.' in answer:
        while answer[-1] == '0':
            answer.pop()
        if answer[-1] == '.':
            answer.pop()
    
    return "".join(answer)

def plus_test(a, b):
    return a+b

a = random.random()
b = random.random()

print("String Math")
print(f"{a} + {b} = {plus(a, b)}")

print("Python Math")
print(f"{a} + {b} = {a + b}")

def plus(a, b):
    a, b = str(a), str(b)
    max_int = max(len(a.split(".")[0]), len(b.split(".")[0]))
    a += "." if "." not in a else ""
    b += "." if "." not in b else ""

    max_few = max(len(a.split(".")[1]), len(b.split(".")[1]))
    a_int, a_frac = a.split(".")
    b_int, b_frac = b.split(".")

    a_int, b_int = a_int.zfill(max_int), b_int.zfill(max_int)
    a_frac, b_frac = a_frac.ljust(max_few, '0'), b_frac.ljust(max_few, '0')

    a, b = a_int + a_frac, b_int + b_frac

    max_len = len(a)
    answer = []
    add = "0"

    for i in range(max_len - 1, -1, -1):
        cal = PLUS_DICT[f"{a[i]}+{b[i]}"]
        last_cal = cal[-1]
        last_cal = PLUS_DICT[f"{last_cal}+{add}"]
        if len(last_cal) > 1:
            add = PLUS_DICT[f"{cal[0]}+{last_cal[0]}"][0]
        elif len(cal) > 1:
            add = cal[0]
        else:
            add = "0"
        answer.insert(0, last_cal[-1])

    if add != "0":
        max_int += 1
        answer.insert(0, add)

    answer.insert(max_int, ".")
    
    while len(answer) > 1 and answer[0] == '0' and answer[1] != '.':
        answer.pop(0)
    if '.' in answer:
        while answer[-1] == '0':
            answer.pop()
        if answer[-1] == '.':
            answer.pop()
    
    return "".join(answer)