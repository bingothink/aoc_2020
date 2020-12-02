"""
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

Your puzzle answer was 447.

--- Part Two ---
While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?

Your puzzle answer was 249.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

INPUT = "day2_input.txt"

# get input in format:
# 1-3 a: abcde     => ['1', '3', 'a', 'abcde']
# 1-3 b: cdefg     => ['1', '3', 'b', 'cdefg']
# 2-9 c: ccccccccc => ['2', '9', 'c', 'ccccccccc']
inp = []
for l in open(INPUT).readlines():
    # strip, remove colon, replace dash with space, and split on spaces
    inp.append(l.strip().replace(':','').replace('-', ' ').split(' '))

# part 1 validation
def ValidateP1(i):
    # i[0]: first index
    # i[1]: second index
    # i[2]: letter
    # i[3]: password

    # count number of letter (i[2]) occurrences in string (i[3])
    cnt = i[3].count(i[2])
    # ensure count is within i[0] and i[1] bounds
    if cnt < int(i[0]) or cnt > int(i[1]):
        return 0
    else:
        return 1

def Part1():
    # init valid count
    valid = 0
    for i in inp:
        # ValidateP1 will return 1 or 0 if valid or not, respectively. Just add them up. 
        valid += ValidateP1(i)
    return valid
    

def Part2():
    # i[0]: first index
    # i[1]: second index
    # i[2]: letter
    # i[3]: password
    valid = 0
    for i in inp:
        # "one or the other but not both" == XOR
        # i[3] string index at i[0]-1 (1-based) is equal to the letter XOR
        # i[3] string index at i[1]-1 (1-based) is equal to the letter
        if (i[3][int(i[0])-1] == i[2]) ^ (i[3][int(i[1])-1] == i[2]):
            valid += 1
    return valid

# execute part 1
print("Part 1: ", Part1())
# execute part 2
print("Part 2: ", Part2())
