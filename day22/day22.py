"""

"""

INPUT = "day22_input.txt"
#INPUT = "day22_example.txt"
inp = open(INPUT).read().split('\n\n')
player1 = list(map(int,inp[0].split('\n')[1:]))
player2 = list(map(int,inp[1].split('\n')[1:-1]))

def playCombat():
    # player two hand wins
    if player2[0] > player1[0]:
        player2.append(player2[0])
        player2.append(player1[0])
    # player one hand wins
    else:
        player1.append(player1[0])
        player1.append(player2[0])
    del player1[0]
    del player2[0]

def getScore(cards):
    return sum([i*c for i,c in enumerate(reversed(cards),1)])

def Part1():
    while len(player1) > 0 and len(player2) > 0:
        playCombat()
    if len(player1) > 0:
        return getScore(player1)
    else:
        return getScore(player2)

def Part2():
    return

# execute Part 1
print("Part 1:", Part1())
# execute Part 2
print("Part 2:", Part2())
