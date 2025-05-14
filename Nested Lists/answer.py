if __name__ == '__main__':
    dic = []
    sr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dic.append([name, score])
        sr.append(score)

    rdic = dic[::-1]
    low = secondLow = float('inf')
    for i in sr:
        if low >= i:
            secondLow, low = low, i
        elif secondLow >= i:
            secondLow = i

    for i in range(len(rdic)):
        if rdic[i][1] == secondLow:
            print(rdic[i][0])