
# Problem 1
def energy_on_nth_day(n):
    if n == 1 or n == 2:
        return 1
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(energy_on_nth_day(1))
print(energy_on_nth_day(2))
print(energy_on_nth_day(5))
print(energy_on_nth_day(7))

# Problem 2
def toph_training(cost):
    if not cost:
        return 0
    n = len(cost)
    if n == 1:
        return cost[0]
    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    return min(dp[-1], dp[-2])

print(toph_training([10, 15, 20]))
print(toph_training([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

# Problem 3
def aang_wins(n):
    if n == 1:
        return False
    dp = [False] * (n + 1)
    for i in range(2, n + 1):
        for x in range(1, i):
            if i % x == 0 and not dp[i - x]:
                dp[i] = True
                break
    return dp[n]

print(aang_wins(2))
print(aang_wins(3))

# Problem 4
def max_k_repeating(sequence, move):
    len_seq = len(sequence)
    len_move = len(move)
    if len_seq < len_move or len_move == 0:
        return 0
    dp = [0] * len_seq
    for i in range(len_move - 1, len_seq):
        if sequence[i - len_move + 1:i + 1] == move:
            if i - len_move >= 0:
                dp[i] = dp[i - len_move] + 1
            else:
                dp[i] = 1
    return max(dp) if dp else 0

print(max_k_repeating("airairwater", "air"))
print(max_k_repeating("fireearthfire", "fire"))
print(max_k_repeating("waterfire", "air"))

# Problem 5
def zuko_supply_mission(tokens, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for token in tokens:
            if token <= i:
                dp[i] = min(dp[i], dp[i - token] + 1)
    return dp[amount] if dp[amount] != amount + 1 else -1

print(zuko_supply_mission([1, 2, 5], 11))
print(zuko_supply_mission([2], 3))
print(zuko_supply_mission([1], 0))

# Problem 6
def training_synchronization(katara_moves, toph_moves):
    m = len(katara_moves)
    n = len(toph_moves)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if katara_moves[i-1] == toph_moves[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

print(training_synchronization("waterbend", "earthbend"))
print(training_synchronization("bend", "bend"))
print(training_synchronization("fire", "air"))