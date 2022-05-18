def func(arr, n):
    digits = [str(j) for j in range(n)]
    out = []
    for num in arr:
        for digit in digits:
            if "2" not in str(num) and digit in str(num):
                if num not in out:
                    out.append(num)
    return out

arr = [123451231235,12321,33341,331,65464234,12335,1255,133134,12351235,121212,15521,1,1,123]

print(func(arr, 5))

