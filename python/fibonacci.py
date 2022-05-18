def fibonacci(n):
    seq = [0, 1]

    for i in range(2, n):
        seq.append(seq[i - 1] + seq[i - 2])
    print(str(seq) + "\nGolden ratio = " + str(seq[-1]/seq[-2]))

fibonacci(1000)