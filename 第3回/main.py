import sys

def main(lines):
    N = int(lines[0])
    A_list = list(map(int, lines[1].split()))

    res = DP(N, A_list)
    print(res)

def DP(N, A_list):
    K = int(((8*N+1)**0.5 - 1)/2)
    # 準備
    dp = [[0 for _ in range(N)] for _ in range(K)]
    for j in range(N):
        dp[0][j] = 1
    # 1皿だけ食べる時が場合の数の初期値
    total = N
    # 動的計画法
    for i in range(1, K): # 1 ~ K-1 # index基準
        comulative_sum = 0 # 累積和
        comulative_dict = {} # 寿司の種類ごとの累積パターン数
        first_j = int((i+1)*(i+2)/2 - 1) # 0じゃない最初のindex
        for j in range(first_j, N):
            comulative_sum += dp[i-1][j-(i+1)]
            if A_list[j-(i+1)] in comulative_dict:
                comulative_dict[A_list[j-(i+1)]] += dp[i-1][j-(i+1)]
            else:
                comulative_dict[A_list[j-(i+1)]] = dp[i-1][j-(i+1)]
            dp[i][j] = comulative_sum
            if A_list[j] in comulative_dict:
                dp[i][j] -= comulative_dict[A_list[j]] # 同じ寿司を連続して選ばない
            total += dp[i][j]

    return total % 998244353

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
