if __name__ == '__main__':
    dic = []
    sr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dic.append([name, score])
        sr.append(score)

    dic.sort()
    sr = set(sr)
    low = secondLow = float('inf')
    for i in sr:
        if low >= i:
            secondLow, low = low, i
        elif secondLow >= i:
            secondLow = i

    for i in range(len(dic)):
        if dic[i][1] == secondLow:
            print(dic[i][0])
