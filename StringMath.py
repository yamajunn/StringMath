import time

PLUS_DICT = {
    "0+0":"0", "0+1":"1", "0+2":"2", "0+3":"3", "0+4":"4", "0+5":"5", "0+6":"6", "0+7":"7", "0+8":"8", "0+9":"9",
    "1+0":"1", "1+1":"2", "1+2":"3", "1+3":"4", "1+4":"5", "1+5":"6", "1+6":"7", "1+7":"8", "1+8":"9", "1+9":"10",
    "2+0":"2", "2+1":"3", "2+2":"4", "2+3":"5", "2+4":"6", "2+5":"7", "2+6":"8", "2+7":"9", "2+8":"10", "2+9":"11",
    "3+0":"3", "3+1":"4", "3+2":"5", "3+3":"6", "3+4":"7", "3+5":"8", "3+6":"9", "3+7":"10", "3+8":"11", "3+9":"12",
    "4+0":"4", "4+1":"5", "4+2":"6", "4+3":"7", "4+4":"8", "4+5":"9", "4+6":"10", "4+7":"11", "4+8":"12", "4+9":"13",
    "5+0":"5", "5+1":"6", "5+2":"7", "5+3":"8", "5+4":"9", "5+5":"10", "5+6":"11", "5+7":"12", "5+8":"13", "5+9":"14",
    "6+0":"6", "6+1":"7", "6+2":"8", "6+3":"9", "6+4":"10", "6+5":"11", "6+6":"12", "6+7":"13", "6+8":"14", "6+9":"15",
    "7+0":"7", "7+1":"8", "7+2":"9", "7+3":"10", "7+4":"11", "7+5":"12", "7+6":"13", "7+7":"14", "7+8":"15", "7+9":"16",
    "8+0":"8", "8+1":"9", "8+2":"10", "8+3":"11", "8+4":"12", "8+5":"13", "8+6":"14", "8+7":"15", "8+8":"16", "8+9":"17",
    "9+0":"9", "9+1":"10", "9+2":"11", "9+3":"12", "9+4":"13", "9+5":"14", "9+6":"15", "9+7":"16", "9+8":"17", "9+9":"18",
}

def plus(a, b):
    max_int = max(len(a.split(".")[0]), len(b.split(".")[0]))
    if "." not in a:
        a += "."
    if "." not in b:
        b += "."
    max_few = max(len(a.split(".")[1]), len(b.split(".")[1]))
    a = ['0']*(max_int-len(a.split(".")[0])) + list(a) + [0]*(max_few-len(a.split(".")[1]))
    b = ['0']*(max_int-len(b.split(".")[0])) + list(b) + [0]*(max_few-len(b.split(".")[1]))
    a = [i for i in a if i != "."]
    b = [i for i in b if i != "."]
    print(a, b)
    max_len = max(len(a), len(b))
    answer = []
    add = "0"
    for i in range(max_len):
        cal = PLUS_DICT[f"{a[-i-1]}+{b[-i-1]}"]
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
        answer.insert(0, add)
    
    answer.insert(max_int, ".")
    if answer[-1] == ".":
        answer.pop()
    return "".join(answer)

def plus2(a, b):
    return a+b

print(plus("1", "9"))
# num = 1000
# for i in range(num):
#     for j in range(num):
#         if int(plus(str(i), str(j))) == i+j:
#             print(f"\r{i} + {j} = {i+j}",end="")
#         else:
#             print(f"Error: {i} + {j} = {i+j}, but {plus(str(i), str(j))}")
#             break

# num = 1000
# start = time.time()
# for i in range(num):
#     for j in range(num):
#         # plus2(i, j)
#         plus(str(i), str(j))
# print(f"Time: {time.time()-start}")