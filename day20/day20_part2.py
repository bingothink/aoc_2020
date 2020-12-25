"""
--- Day 20: Jurassic Jigsaw ---
The high-speed train leaves the forest and quickly carries you south. You can even see a desert in the distance! Since you have some spare time, you might as well see if there was anything interesting in the image the Mythical Information Bureau satellite captured.

After decoding the satellite messages, you discover that the data actually contains many small images created by the satellite's camera array. The camera array consists of many cameras; rather than produce a single square image, they produce many smaller square image tiles that need to be reassembled back into a single image.

Each camera in the camera array returns a single monochrome image tile with a random unique ID number. The tiles (your puzzle input) arrived in a random order.

Worse yet, the camera array appears to be malfunctioning: each image tile has been rotated and flipped to a random orientation. Your first task is to reassemble the original image by orienting the tiles so they fit together.

To show how the tiles should be reassembled, each tile's image data includes a border that should line up exactly with its adjacent tiles. All tiles have this border, and the border lines up exactly when the tiles are both oriented correctly. Tiles at the edge of the image also have this border, but the outermost edges won't line up with any other tiles.

For example, suppose you have the following nine tiles:

Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
By rotating, flipping, and rearranging them, you can find a square arrangement that causes all adjacent borders to line up:

#...##.#.. ..###..### #.#.#####.
..#.#..#.# ###...#.#. .#..######
.###....#. ..#....#.. ..#.......
###.##.##. .#.#.#..## ######....
.###.##### ##...#.### ####.#..#.
.##.#....# ##.##.###. .#...#.##.
#...###### ####.#...# #.#####.##
.....#..## #...##..#. ..#.###...
#.####...# ##..#..... ..#.......
#.##...##. ..##.#..#. ..#.###...

#.##...##. ..##.#..#. ..#.###...
##..#.##.. ..#..###.# ##.##....#
##.####... .#.####.#. ..#.###..#
####.#.#.. ...#.##### ###.#..###
.#.####... ...##..##. .######.##
.##..##.#. ....#...## #.#.#.#...
....#..#.# #.#.#.##.# #.###.###.
..#.#..... .#.##.#..# #.###.##..
####.#.... .#..#.##.. .######...
...#.#.#.# ###.##.#.. .##...####

...#.#.#.# ###.##.#.. .##...####
..#.#.###. ..##.##.## #..#.##..#
..####.### ##.#...##. .#.#..#.##
#..#.#..#. ...#.#.#.. .####.###.
.#..####.# #..#.#.#.# ####.###..
.#####..## #####...#. .##....##.
##.##..#.. ..#...#... .####...#.
#.#.###... .##..##... .####.##.#
#...###... ..##...#.. ...#..####
..#.#....# ##.#.#.... ...##.....
For reference, the IDs of the above tiles are:

1951    2311    3079
2729    1427    2473
2971    1489    1171
To check that you've assembled the image correctly, multiply the IDs of the four corner tiles together. If you do this with the assembled tiles from the example above, you get 1951 * 3079 * 2971 * 1171 = 20899048083289.

Assemble the tiles into an image. What do you get if you multiply together the IDs of the four corner tiles?

Your puzzle answer was 45443966642567.

--- Part Two ---
Now, you're ready to check the image for sea monsters.

The borders of each tile are not part of the actual image; start by removing them.

In the example above, the tiles become:

.#.#..#. ##...#.# #..#####
###....# .#....#. .#......
##.##.## #.#.#..# #####...
###.#### #...#.## ###.#..#
##.#.... #.##.### #...#.##
...##### ###.#... .#####.#
....#..# ...##..# .#.###..
.####... #..#.... .#......

#..#.##. .#..###. #.##....
#.####.. #.####.# .#.###..
###.#.#. ..#.#### ##.#..##
#.####.. ..##..## ######.#
##..##.# ...#...# .#.#.#..
...#..#. .#.#.##. .###.###
.#.#.... #.##.#.. .###.##.
###.#... #..#.##. ######..

.#.#.### .##.##.# ..#.##..
.####.## #.#...## #.#..#.#
..#.#..# ..#.#.#. ####.###
#..####. ..#.#.#. ###.###.
#####..# ####...# ##....##
#.##..#. .#...#.. ####...#
.#.###.. ##..##.. ####.##.
...###.. .##...#. ..#..###
Remove the gaps to form the actual image:

.#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###
Now, you're ready to search for sea monsters! Because your image is monochrome, a sea monster will look like this:

                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
When looking for this pattern in the image, the spaces can be anything; only the # need to match. Also, you might need to rotate or flip your image before it's oriented correctly to find sea monsters. In the above image, after flipping and rotating it to the appropriate orientation, there are two sea monsters (marked with O):

.####...#####..#...###..
#####..#..#.#.####..#.#.
.#.#...#.###...#.##.O#..
#.O.##.OO#.#.OO.##.OOO##
..#O.#O#.O##O..O.#O##.##
...#.#..##.##...#..#..##
#.##.#..#.#..#..##.#.#..
.###.##.....#...###.#...
#.####.#.#....##.#..#.#.
##...#..#....#..#...####
..#.##...###..#.#####..#
....#.##.#.#####....#...
..##.##.###.....#.##..#.
#...#...###..####....##.
.#.##...#.##.#.#.###...#
#.###.#..####...##..#...
#.###...#.##...#.##O###.
.O##.#OO.###OO##..OOO##.
..O#.O..O..O.#O##O##.###
#.#..##.########..#..##.
#.#####..#.#...##..#....
#....##..#.#########..##
#...#.....#..##...###.##
#..###....##.#...##.##.#
Determine how rough the waters are in the sea monsters' habitat by counting the number of # that are not part of a sea monster. In the above example, the habitat's water roughness is 273.

How many # are not part of a sea monster?

Your puzzle answer was 1607.

Both parts of this puzzle are complete! They provide two gold stars: **
"""
import math
import re

INPUT = "day20_input.txt"
inp = open(INPUT).read().strip().split('\n\n')

TOP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3
ALL = 4
opposite = {TOP : BOTTOM,
            BOTTOM : TOP,
            LEFT : RIGHT,
            RIGHT : LEFT}

def invert(image):
    return image[::-1]

def rotate(image):
    # clockwise rotation
    d = zip(*image[::-1])
    return [''.join(list(i)) for i in d]

class Tile:
    def __init__(self, data):
        self.data = data
        # [top, right, bottom, left]
        self.neighbors = [None, None, None, None]
    def leftSide(self):
        res = ""
        for i in self.data:
            res += i[0]
        return res
    def rightSide(self):
        res = ""
        for i in self.data:
            res += i[-1]
        return res
    def topSide(self):
        return self.data[0]
    def bottomSide(self):
        return self.data[-1]
    def side(self,which):
        if which == TOP:
            return self.topSide()
        elif which == RIGHT:
            return self.rightSide()
        elif which == BOTTOM:
            return self.bottomSide()
        elif which == LEFT:
            return self.leftSide()
        else:
            return [self.topSide(), self.rightSide(), self.bottomSide(), self.leftSide()]
    def revert(self):
        # reverse the data 
        newdata = []
        for d in self.data:
            newdata.append(d[::-1])
        self.data = newdata.copy()
        # update neighbors
        temp = self.neighbors[RIGHT]
        self.neighbors[RIGHT] = self.neighbors[LEFT]
        self.neighbors[LEFT] = temp
    def invert(self):
        # reverse the data lines
        self.data = invert(self.data)
        # update neighbors
        temp = self.neighbors[TOP]
        self.neighbors[TOP] = self.neighbors[BOTTOM]
        self.neighbors[BOTTOM] = temp
    def rotate(self):
        # clockwise rotation
        self.data = rotate(self.data)
        # update neighbors
        self.neighbors.insert(0,self.neighbors[-1])
        del self.neighbors[-1]
    def trimEdges(self):
        self.data = [i[1:-1] for i in self.data[1:-1]]

tiles = dict()
for tile in inp:
    tilenum = int(tile.split('\n')[0].split(' ')[1][:-1])
    data = tile.split('\n')[1:]
    t = Tile(data)
    tiles[tilenum] = t

def numMatches(tile):
    edges = set(tiles[tile].side(ALL))
    res = []
    for t in tiles:
        if t != tile:
            # check all sides of this tile t (top bottom, left, right, and reversed for each)
            tEdges = set(tiles[t].side(ALL) + [x[::-1] for x in tiles[t].side(ALL)])
            if len(edges.intersection(tEdges)) > 0:
                res.append(t)
    return len(res)

def findNeighbors(tile, searchList):
    myEdges = tiles[tile].side(ALL)
    for side,data in enumerate(myEdges):
        for t in tiles:
            if t != tile:
                # check if matching before we do anything else
                if tiles[t].side(opposite[side]) == data:
                    tiles[tile].neighbors[side] = t
                    tiles[t].neighbors[opposite[side]] = tile
                    if t not in searchList:
                        searchList.append(t)
                    break
                # rotate tile through all possible edges
                rotationsLeft = 3
                while rotationsLeft > 0:
                    tiles[t].rotate()
                    rotationsLeft -= 1
                    if tiles[t].side(opposite[side]) == data:
                        tiles[tile].neighbors[side] = t
                        if t not in searchList:
                            searchList.append(t)
                        break
                tiles[t].invert()
                if tiles[t].side(opposite[side]) == data:
                    tiles[tile].neighbors[side] = t
                    tiles[t].neighbors[opposite[side]] = tile
                    if t not in searchList:
                        searchList.append(t)
                    break
                rotationsLeft = 3
                while rotationsLeft > 0:
                    rotationsLeft -= 1
                    tiles[t].rotate()
                    if tiles[t].side(opposite[side]) == data:
                        tiles[tile].neighbors[side] = t
                        if t not in searchList:
                            searchList.append(t)
                        break

def updateOrientation(startingTile):
    startCol = startingTile
    while startCol != None:
        # assume top is good, line up column
        upperEdge = tiles[startCol].side(BOTTOM)
        curr = tiles[startCol].neighbors[BOTTOM]
        rotation = 0
        while curr != None:
            if tiles[curr].side(TOP) == upperEdge:
                rotation = 0
                upperEdge = tiles[curr].side(BOTTOM)
                curr = tiles[curr].neighbors[BOTTOM]
            else:
                if rotation % 4 == 0:
                    tiles[curr].invert()
                else:
                    tiles[curr].rotate()
                rotation += 1
        # move to next column
        leftEdge = tiles[startCol].side(RIGHT)
        startCol = tiles[startCol].neighbors[RIGHT]
        # line up left edge with previous colum starting tile
        if startCol != None:
            rotation = 0
            while tiles[startCol].side(LEFT) != leftEdge:
                if rotation % 4 == 0:
                    tiles[startCol].invert()
                else:
                    tiles[startCol].rotate()
                rotation += 1

def getTopLeft(corners):
    for t in corners:
        if tiles[t].neighbors[TOP] == None and tiles[t].neighbors[LEFT] == None:
            return t

def assembleImage(startingTile):
    # rows = square root of tiles (edge length of square canvas)
    #        multiplied by length of tile data minus 2 (trimmed edges)
    totalRows = int(math.sqrt(len(tiles)))*(len(tiles[startingTile].data)-2)
    image = ["" for r in range(totalRows)]
    startCol = startingTile
    while startCol != None:
        rowIdx = 0
        curr = startCol
        while curr != None:
            # trim edges off of this tile
            tiles[curr].trimEdges()
            # add tile data to image
            for d in tiles[curr].data:
                image[rowIdx] += d
                rowIdx += 1
            # move to next tile down
            curr = tiles[curr].neighbors[BOTTOM]
        # move to next column
        startCol = tiles[startCol].neighbors[RIGHT]
    return image

def findMonsters(image):
    mTop = "#"
    mMiddle = "#.{4}(?:##.{4}){2}#{3}"
    mBottom = "(?:#.{2}){5}#"
    lineLength = len(image[0])
    # chars between top and middle
    topToMiddleChars = str(lineLength-19)
    # chars between middle and bottom
    middleToBottomChars = str(lineLength-19)
    # build regex
    monsters = mTop + ".{"+topToMiddleChars+"}" + mMiddle + ".{"+middleToBottomChars+"}" + mBottom
    # flatten image and search
    flatImage = "".join(image)
    # count monsters
    cnt = 0
    for i in range(len(flatImage)):
        if re.match(monsters, flatImage[i:]) != None:
            cnt += 1
    return cnt

def Part2():
    corners = []
    # find the first corner we can
    for t in tiles:
        # corner pieces will have exactly two neighbors
        if numMatches(t) == 2:
            corners.append(t)
    # start neighbor search in first corner
    searchList = [corners[0]]
    idx = 0
    while idx < len(searchList):
        findNeighbors(searchList[idx], searchList)  
        idx += 1
    # update all orientations
    topLeft = getTopLeft(corners)
    updateOrientation(topLeft)
    # orientations in place, assemble image from top left
    image = assembleImage(topLeft)
    # find monsters 
    num = findMonsters(image)
    rotation = 0
    # while no monsters are found, keep flipping/rotating image
    while num == 0:
        if rotation % 4 == 0:
            image = invert(image)
        else:
            image = rotate(image)
        num = findMonsters(image)
        rotation += 1
    # count hashes in image
    cnt = 0
    for c in "".join(image):
        if c == "#":
            cnt += 1
    # subtract 15 hashes in each sea monster
    cnt -= (15 * num)
    return cnt

# execute Part 2
print("Part 2:", Part2())
