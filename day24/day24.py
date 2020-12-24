"""
--- Day 24: Lobby Layout ---
Your raft makes it to the tropical island; it turns out that the small crab was an excellent navigator. You make your way to the resort.

As you enter the lobby, you discover a small problem: the floor is being renovated. You can't even reach the check-in desk until they've finished installing the new tile floor.

The tiles are all hexagonal; they need to be arranged in a hex grid with a very specific color pattern. Not in the mood to wait, you offer to help figure out the pattern.

The tiles are all white on one side and black on the other. They start with the white side facing up. The lobby is large enough to fit whatever pattern might need to appear there.

A member of the renovation crew gives you a list of the tiles that need to be flipped over (your puzzle input). Each line in the list identifies a single tile that needs to be flipped by giving a series of steps starting from a reference tile in the very center of the room. (Every line starts from the same reference tile.)

Because the tiles are hexagonal, every tile has six neighbors: east, southeast, southwest, west, northwest, and northeast. These directions are given in your list, respectively, as e, se, sw, w, nw, and ne. A tile is identified by a series of these directions with no delimiters; for example, esenee identifies the tile you land on if you start at the reference tile and then move one tile east, one tile southeast, one tile northeast, and one tile east.

Each time a tile is identified, it flips from white to black or from black to white. Tiles might be flipped more than once. For example, a line like esew flips a tile immediately adjacent to the reference tile, and a line like nwwswee flips the reference tile itself.

Here is a larger example:

sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
In the above example, 10 tiles are flipped once (to black), and 5 more are flipped twice (to black, then back to white). After all of these instructions have been followed, a total of 10 tiles are black.

Go through the renovation crew's list and determine which tiles they need to flip. After all of the instructions have been followed, how many tiles are left with the black side up?

Your puzzle answer was 230.

--- Part Two ---
The tile floor in the lobby is meant to be a living art exhibit. Every day, the tiles are all flipped according to the following rules:

Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
Here, tiles immediately adjacent means the six tiles directly touching the tile in question.

The rules are applied simultaneously to every tile; put another way, it is first determined which tiles need to be flipped, then they are all flipped at the same time.

In the above example, the number of black tiles that are facing up after the given number of days has passed is as follows:

Day 1: 15
Day 2: 12
Day 3: 25
Day 4: 14
Day 5: 23
Day 6: 28
Day 7: 41
Day 8: 37
Day 9: 49
Day 10: 37

Day 20: 132
Day 30: 259
Day 40: 406
Day 50: 566
Day 60: 788
Day 70: 1106
Day 80: 1373
Day 90: 1844
Day 100: 2208
After executing this process a total of 100 times, there would be 2208 black tiles facing up.

How many tiles will be black after 100 days?

Your puzzle answer was 3565.

Both parts of this puzzle are complete! They provide two gold stars: **
"""
import hexy as hx
from collections import defaultdict

INPUT = "day24_input.txt"
inp = open(INPUT).read().splitlines()

def splitline(l):
    i = 0
    dirs = []
    while i < len(l):
        if l[i] == 'n' or l[i] == 's':
            dirs.append(l[i].upper()+l[i+1].upper())
            i += 2
        else:
            dirs.append(l[i].upper())
            i += 1
    return dirs

lines = []
for line in inp:
    lines.append(splitline(line))

def Part1():
    tiles = defaultdict(bool)
    for l in lines:
        # start at reference tile
        curr = (0,0,0)
        for d in l:
            # get coords of new tile using hexy coords (hx.NE, hx.SW, etc)
            curr = tuple(curr + eval('hx.'+d))
        tiles[curr] = not tiles[curr]
    cnt = 0
    for t in tiles.values():
        if t:
            cnt += 1
    return cnt

def addNeighbors(tiles):
    keys = list(tiles.keys())
    for t in keys:
        for d in hx.ALL_DIRECTIONS:
            if tuple(t+d) not in tiles:
                tiles[tuple(t+d)] = False

def neighborColors(tiles, t):
    black = 0
    for d in hx.ALL_DIRECTIONS:
        if tiles[tuple(t+d)]:
            black += 1
    return black

def iterate(tiles):
    newtiles = tiles.copy()
    for t in newtiles:
        b = neighborColors(tiles, t)
        # if white and 2 black next to it
        if not tiles[t] and b == 2:
            newtiles[t] = True
        # if black and 0 or more than 2 black next to it
        elif tiles[t] and (b == 0 or b > 2):
            newtiles[t] = False
    return newtiles

def Part2():
    tiles = defaultdict(bool)
    for l in lines:
        # start at reference tile
        curr = (0,0,0)
        for d in l:
            # get coords of new tile using hexy coords (hx.NE, hx.SW, etc)
            curr = tuple(curr + eval('hx.'+d))
        tiles[curr] = not tiles[curr]
    # loop for the days
    for days in range(100):
        # add neighbor tiles of my tiles to collection for processing
        addNeighbors(tiles)
        # flip tiles
        tiles = iterate(tiles)
    cnt = 0
    for t in tiles.values():
        if t:
            cnt += 1
    return cnt

# execute Part 1
print("Part 1:", Part1())
# execute Part 2
print("Part 2:", Part2())
