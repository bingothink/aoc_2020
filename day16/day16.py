"""
--- Day 16: Ticket Translation ---
As you're walking to yet another connecting flight, you realize that one of the legs of your re-routed trip coming up is on a high-speed train. However, the train ticket you were given is in a language you don't understand. You should probably figure out what it says before you get to the train station after the next flight.

Unfortunately, you can't actually read the words on the ticket. You can, however, read the numbers, and so you figure out the fields these tickets must have and the valid ranges for values in those fields.

You collect the rules for ticket fields, the numbers on your ticket, and the numbers on other nearby tickets for the same train service (via the airport security cameras) together into a single document you can reference (your puzzle input).

The rules for ticket fields specify a list of fields that exist somewhere on the ticket and the valid ranges of values for each field. For example, a rule like class: 1-3 or 5-7 means that one of the fields in every ticket is named class and can be any value in the ranges 1-3 or 5-7 (inclusive, such that 3 and 5 are both valid in this field, but 4 is not).

Each ticket is represented by a single line of comma-separated values. The values are the numbers on the ticket in the order they appear; every ticket has the same format. For example, consider this ticket:

.--------------------------------------------------------.
| ????: 101    ?????: 102   ??????????: 103     ???: 104 |
|                                                        |
| ??: 301  ??: 302             ???????: 303      ??????? |
| ??: 401  ??: 402           ???? ????: 403    ????????? |
'--------------------------------------------------------'
Here, ? represents text in a language you don't understand. This ticket might be represented as 101,102,103,104,301,302,303,401,402,403; of course, the actual train tickets you're looking at are much more complicated. In any case, you've extracted just the numbers in such a way that the first number is always the same specific field, the second number is always a different specific field, and so on - you just don't know what each position actually means!

Start by determining which tickets are completely invalid; these are tickets that contain values which aren't valid for any field. Ignore your ticket for now.

For example, suppose you have the following notes:

class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
It doesn't matter which position corresponds to which field; you can identify invalid nearby tickets by considering only whether tickets contain values that are not valid for any field. In this example, the values on the first nearby ticket are all valid for at least one field. This is not true of the other three nearby tickets: the values 4, 55, and 12 are are not valid for any field. Adding together all of the invalid values produces your ticket scanning error rate: 4 + 55 + 12 = 71.

Consider the validity of the nearby tickets you scanned. What is your ticket scanning error rate?

Your puzzle answer was 20975.

--- Part Two ---
Now that you've identified which tickets contain invalid values, discard those tickets entirely. Use the remaining valid tickets to determine which field is which.

Using the valid ranges for each field, determine what order the fields appear on the tickets. The order is consistent between all tickets: if seat is the third field, it is the third field on every ticket, including your ticket.

For example, suppose you have the following notes:

class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
Based on the nearby tickets in the above example, the first position must be row, the second position must be class, and the third position must be seat; you can conclude that in your ticket, class is 12, row is 11, and seat is 13.

Once you work out which field is which, look for the six fields on your ticket that start with the word departure. What do you get if you multiply those six values together?

Your puzzle answer was 910339449193.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

INPUT = "day16_input.txt"
inp = open(INPUT).read()

splitlines = inp.split('\n\n')
# parse rules
rules = dict()
for line in splitlines[0].split('\n'):
    rule = line.split(':')[0]
    ranges = list(map(int,line.split(':')[1].replace('-',' ').replace('or', '').split()))
    rules[rule] = [range(ranges[0],ranges[1]+1), range(ranges[2],ranges[3]+1)]
# parse my ticket
myTicket = list(map(int,splitlines[1].split('\n')[1].split(',')))
# parse nearby tickets
nearTickets = []
for line in splitlines[2].split('\n')[1:]:
    if line != '':
        nearTickets.append(list(map(int,line.split(','))))

# flatten list function
flatten = lambda t: [r for rules in t for r in rules]
# return False if not valid, True if valid
def testField(field):
    for r in flatten(rules.values()):
        if field in r:
            return True
    return False

##########
# PART 1 #
##########
def Part1():
    invalid = 0
    for t in nearTickets:
        for field in t:
            if not testField(field):
                invalid += field
    return invalid

##########
# PART 2 #
##########
def processTicket(potentials, ticket):
    for x,val in enumerate(ticket):
        # nothing more to reduce if this field is already only one option
        if len(potentials[x]) == 1:
            continue
        # copy array so we can modify potentials on the fly
        temp = potentials[x].copy()
        for field in temp:
            # if this value is not meeting the rules for this field
            if not (val in rules[field][0] or val in rules[field][1]):
                # remove this field from the potentials for this value
                potentials[x].remove(field)
    return potentials

# condenses the list of potential values until each field only has one possibility
def condense(potentials):
    # if the length is more than the number of fields on my ticket, there's more to do
    while len(flatten(potentials)) > len(myTicket):
        for x in range(len(potentials)):
            # if we found a field with length one, remove that option from all other fields
            if len(potentials[x]) == 1:
                for y in range(len(potentials)):
                    if y != x and potentials[x][0] in potentials[y]:
                        potentials[y].remove(potentials[x][0])

    return potentials

def Part2():
    # remove invalid tickets
    tickets = nearTickets.copy()
    # loop in reverse so we can delete by array index
    for x,t in reversed(list(enumerate(tickets))):
        for field in t:
            # if this field isn't valid, delete from good tickets
            if not testField(field):
                del nearTickets[x]
            continue
    # make a list of possible fields
    fieldlist = list(rules.keys())
    # all fields are potential at first, copy the field list into every possible location
    potentials = []
    for i in range(len(myTicket)):
        potentials.append(fieldlist.copy())
    # process tickets to eliminate options
    for t in nearTickets:
        potentials = processTicket(potentials, t)
    # remove duplicates
    potentials = flatten(condense(potentials))
    result = 1
    # multiply all fields that start with "departure" together and return
    for x,field in enumerate(potentials):
        if field.startswith('departure'):
            result *= myTicket[x]
    return result

# execute Part 1
print("Part 1:", Part1())
# execute Part 2
print("Part 2:", Part2())
