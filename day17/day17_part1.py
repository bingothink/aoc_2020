"""
--- Day 17: Conway Cubes ---
As your flight slowly drifts through the sky, the Elves at the Mythical Information Bureau at the North Pole contact you. They'd like some help debugging a malfunctioning experimental energy source aboard one of their super-secret imaging satellites.

The experimental energy source is based on cutting-edge technology: a set of Conway Cubes contained in a pocket dimension! When you hear it's having problems, you can't help but agree to take a look.

The pocket dimension contains an infinite 3-dimensional grid. At every integer 3-dimensional coordinate (x,y,z), there exists a single cube which is either active or inactive.

In the initial state of the pocket dimension, almost all cubes start inactive. The only exception to this is a small flat region of cubes (your puzzle input); the cubes in this region start in the specified active (#) or inactive (.) state.

The energy source then proceeds to boot up by executing six cycles.

Each cube only ever considers its neighbors: any of the 26 other cubes where any of their coordinates differ by at most 1. For example, given the cube at x=1,y=2,z=3, its neighbors include the cube at x=2,y=2,z=2, the cube at x=0,y=2,z=3, and so on.

During a cycle, all cubes simultaneously change their state according to the following rules:

If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
The engineers responsible for this experimental energy source would like you to simulate the pocket dimension and determine what the configuration of cubes should be at the end of the six-cycle boot process.

For example, consider the following initial state:

.#.
..#
###
Even though the pocket dimension is 3-dimensional, this initial state represents a small 2-dimensional slice of it. (In particular, this initial state defines a 3x3x1 region of the 3-dimensional space.)

Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle is shown layer-by-layer at each given z coordinate (and the frame of view follows the active cells in each cycle):

Before any cycles:

z=0
.#.
..#
###


After 1 cycle:

z=-1
#..
..#
.#.

z=0
#.#
.##
.#.

z=1
#..
..#
.#.


After 2 cycles:

z=-2
.....
.....
..#..
.....
.....

z=-1
..#..
.#..#
....#
.#...
.....

z=0
##...
##...
#....
....#
.###.

z=1
..#..
.#..#
....#
.#...
.....

z=2
.....
.....
..#..
.....
.....


After 3 cycles:

z=-2
.......
.......
..##...
..###..
.......
.......
.......

z=-1
..#....
...#...
#......
.....##
.#...#.
..#.#..
...#...

z=0
...#...
.......
#......
.......
.....##
.##.#..
...#...

z=1
..#....
...#...
#......
.....##
.#...#.
..#.#..
...#...

z=2
.......
.......
..##...
..###..
.......
.......
.......
After the full six-cycle boot process completes, 112 cubes are left in the active state.

Starting with your given initial configuration, simulate six cycles. How many cubes are left in the active state after the sixth cycle?

Your puzzle answer was 273.

The first half of this puzzle is complete! It provides one gold star: *
"""

INPUT = "day17_input.txt"
inp = open(INPUT).read().splitlines()

# generate coordinate deltas
deltas = [(x,y,z) for x in range(-1,2) for y in range(-1,2) for z in range(-1,2) if (x,y,z) != (0,0,0)]

def addNeighbors(nodes):
    newnodes = set()
    for i,j,k in nodes:
        for x,y,z in deltas:
            if (i+x,j+y,k+z) not in nodes:
                newnodes.add((i+x,j+y,k+z))
    for n in newnodes:
        nodes[n] = False
    return nodes

def activeNeighbors(nodes, n):
    active = 0
    i,j,k = n
    for x,y,z in deltas:
        if (i+x,j+y,k+z) in nodes and nodes[(i+x,j+y,k+z)]:
            active += 1
    return active

def Part1():
    nodes = dict()
    for y,line in enumerate(inp):
        for x,c in enumerate(line):
            nodes[(x,y,0)] = (True if c == '#' else False)
    for cycles in range(6):
        addNeighbors(nodes)
        newnodes = nodes.copy()
        for n in nodes:
            active = activeNeighbors(nodes, n)
            if nodes[n] and (active == 2 or active == 3):
                newnodes[n] = True
            elif not nodes[n] and (active == 3):
                newnodes[n] = True
            else:
                newnodes[n] = False
        nodes = newnodes
    active = 0
    for n in newnodes:
        if newnodes[n]:
            active += 1
    return active

# execute Part 1
print("Part 1:", Part1())
