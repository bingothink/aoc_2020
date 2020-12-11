"""
--- Day 11: Seating System ---
Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
After a second round, the seats with four or more occupied adjacent seats become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?

Your puzzle answer was 2166.

--- Part Two ---
As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care about the first seat they can see in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions. For example, the empty seat below would see eight occupied seats:

.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....
The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones:

.............
.L.L.#.#.#.#.
.............
The empty seat below would see no occupied seats:

.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.
Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an occupied seat to become empty (rather than four or more from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.

Given the same starting layout as above, these new rules cause the seating area to shift around as follows:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#
#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs, you count 26 occupied seats.

Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, how many seats end up occupied?

Your puzzle answer was 1955.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

INPUT = "day11_input.txt"
inp = open(INPUT).read().splitlines()

EMPTY_SEAT = 'L'
OCCUPIED = '#'
minX = 0
minY = 0
maxX = len(inp[0])
maxY = len(inp)

def search(data, x, y, xStep=0, yStep=0):
    if xStep == 0 and yStep == 0 and y in range(minY,maxY) and x in range(minX,maxX):
        return (1 if data[y][x] == OCCUPIED else 0)
    else:
        while y in range(minY,maxY) and x in range(minX,maxX):
            if data[y][x] == OCCUPIED:
                return 1
            elif data[y][x] == EMPTY_SEAT:
                return 0
            x += xStep
            y += yStep
    return 0

def neighbors(data,x,y,extended):
    X_MOVE = 0
    Y_MOVE = 1
    #each direction includes (X_MOVE,Y_MOVE)
    dirs = {'up'        : ( 0,-1),
            'down'      : ( 0, 1),
            'left'      : (-1, 0),
            'right'     : ( 1, 0),
            'up-right'  : ( 1,-1),
            'down-right': ( 1, 1),
            'up-left'   : (-1,-1),
            'down-left' : (-1, 1)}
    cnt = 0
    for v in dirs.values():
        if extended:
            cnt += search(data, x+v[X_MOVE], y+v[Y_MOVE], v[X_MOVE], v[Y_MOVE])
        else:
            cnt += search(data, x+v[X_MOVE], y+v[Y_MOVE])
    return cnt

def iterate(data, extendedSearch, limit):
    outLine = []
    out = []
    for y,line in enumerate(data):
        outLine = ""
        for x,c in enumerate(line):
            n = neighbors(data,x,y,extendedSearch)
            if c == EMPTY_SEAT and n == 0:
                outLine += OCCUPIED
            elif c == OCCUPIED and n >= limit:
                outLine += EMPTY_SEAT
            else:
                outLine += c
        out.append(outLine)
    return out

def Part1():
    curr = inp.copy()
    prev = []
    # run iterations
    while prev != curr:
        prev = curr
        curr = iterate(curr, False, 4)
    # count seats
    cnt = 0
    for line in curr:
        for c in line:
            if c == OCCUPIED:
                cnt += 1
    return cnt

def Part2():
    curr = inp.copy()
    prev = []
    # run iterations
    while prev != curr:
        prev = curr
        curr = iterate(curr, True, 5)
    # count seats
    cnt = 0
    for line in curr:
        for c in line:
            if c == OCCUPIED:
                cnt += 1
    return cnt


# execute Part 1
print("Part 1:", Part1())
# execute Part 2
print("Part 2:", Part2())
