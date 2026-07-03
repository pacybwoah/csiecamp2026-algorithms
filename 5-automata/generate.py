import random
while True:
    number = random.randint(0, 2 ** 12 - 1)
    arr = []
    for i in range(0, 12):
        if number % 2 == 1:
            arr.append(1)
        else:
            arr.append(0)
        number //= 2
    cnt = 0
    for i in range(0, 10):
        if arr[i] == 1 and arr[i + 1] == 0 and arr[i + 2] == 1:
            cnt += 1
    if cnt > 0:
        ret = ""
        for x in arr:
            if x == 1:
                ret += "紅"
            else:
                ret += "黑"
        print(ret)
        exit(0)