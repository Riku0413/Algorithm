def power(x, n, M):
    if n == 0: return 1
    
    tmp = power(x*x % M, n//2, M)
    if n%2: tmp = tmp*x % M

    return tmp

N = int(input())
list_ab = []
for n in range(1, N+1):
    list_ab.append(input().split())

Q = int(input())
list_lr = []
for q in range(1, Q+1):
    list_lr.append(list(map(int, input().split())))

M = 998244353

# 累積桁数　　　N + 1 の長さ
ruiseki_ketasu = [0]
count = 0
for data in list_ab:
    count += len(data[0]) + int(data[1])
    ruiseki_ketasu.append(count)

# 累積あまり　　　N + 1 の長さ
ruiseki_amari = [0]
for i in range(N):
    R = 0
    p = power(10, ruiseki_ketasu[i+1] - ruiseki_ketasu[i] - 1, M)
    R += (ruiseki_amari[i] * 10 + int(list_ab[i][0]))*p % M
    ruiseki_amari.append(R)

R = 0
for q in range(Q):
    l = list_lr[q][0]
    r = list_lr[q][1]
    R = ruiseki_amari[r]
    if l > 1:
        head = int(ruiseki_amari[l-1])
        order = power(10, ruiseki_ketasu[r] - ruiseki_ketasu[l-1], M)
        R -= head*order
        R = R % M
    print(R)