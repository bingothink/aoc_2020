"""
--- Day 7: Handy Haversacks ---
You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

A bright white bag, which can hold your shiny gold bag directly.
A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)

Your puzzle answer was 233.

--- Part Two ---
It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

faded blue bags contain 0 other bags.
dotted black bags contain 0 other bags.
vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?

Your puzzle answer was 421550.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

INPUT = "day7_input.txt"

rules = dict()

inp = [l.strip() for l in open(INPUT).readlines()]
# format input
for line in inp:
    # clean up unecessary characters
    line = line.replace('bags', '').replace('bag', '').replace('.','')
    # container is first half of line before "contain" keyword
    container = line.split('contain')[0].strip()
    # what the container contains is after "contain" keyword
    contains = line.split('contain')[1].strip()
    # parse bags that are contained (comma separated list)
    baglist = []
    for bag in contains.split(','):
        if bag.strip() != "no other":
            # append (qty, color) tuple
            baglist.append((int(bag.strip()[0]),bag.strip()[2:]))
    rules[container] = baglist
    
# return list of bags that can contain requested bag
def Contains(bag):
    containers = set()
    # search all bags
    for rule in rules:
        # see what this bag contains
        for bags in rules[rule]:
            # if contents is my search term, keep this option
            if bags[1] == bag:
                containers.add(rule)
    # if we found bags that contain this bag
    if len(containers) > 0:
        # search for bags that contain these new bags
        newset = set()
        for c in containers:
            newset.update(Contains(c))
        # add containing bags as options as well
        containers.update(newset)
    return containers

def Part1():
    return len(Contains('shiny gold'))

# return count of bags inside given bag
def BagsInside(bag):
    # if this bag contains no bags
    if len(rules[bag]) == 0:
        return 0
    else:
        cnt = 0
        # search bags inside this bag
        for bags in rules[bag]:
            # add the count of this type of bag plus all bags that these bags contain
            cnt += bags[0] + (bags[0] * BagsInside(bags[1]))
        return cnt

def Part2():
    return BagsInside('shiny gold')


# execute part 1
print("Part 1: ", Part1())

# execute part 2
print("Part 2: ", Part2())
