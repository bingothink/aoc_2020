"""
--- Day 21: Allergen Assessment ---
You reach the train's last stop and the closest you can get to your vacation island without getting wet. There aren't even any boats here, but nothing can stop you now: you build a raft. You just need a few days' worth of food for your journey.

You don't speak the local language, so you can't read any ingredients lists. However, sometimes, allergens are listed in a language you do understand. You should be able to use this information to determine which ingredient contains which allergen and work out which foods are safe to take with you on your trip.

You start by compiling a list of foods (your puzzle input), one food per line. Each line includes that food's ingredients list followed by some or all of the allergens the food contains.

Each allergen is found in exactly one ingredient. Each ingredient contains zero or one allergen. Allergens aren't always marked; when they're listed (as in (contains nuts, shellfish) after an ingredients list), the ingredient that contains each listed allergen will be somewhere in the corresponding ingredients list. However, even if an allergen isn't listed, the ingredient that contains that allergen could still be present: maybe they forgot to label it, or maybe it was labeled in a language you don't know.

For example, consider the following list of foods:

mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
The first food in the list has four ingredients (written in a language you don't understand): mxmxvkd, kfcds, sqjhc, and nhms. While the food might contain other allergens, a few allergens the food definitely contains are listed afterward: dairy and fish.

The first step is to determine which ingredients can't possibly contain any of the allergens in any food in your list. In the above example, none of the ingredients kfcds, nhms, sbzzf, or trh can contain an allergen. Counting the number of times any of these ingredients appear in any ingredients list produces 5: they all appear once each except sbzzf, which appears twice.

Determine which ingredients cannot possibly contain any of the allergens in your list. How many times do any of those ingredients appear?

Your puzzle answer was 2412.

--- Part Two ---
Now that you've isolated the inert ingredients, you should have enough information to figure out which ingredient contains which allergen.

In the above example:

mxmxvkd contains dairy.
sqjhc contains fish.
fvjkl contains soy.
Arrange the ingredients alphabetically by their allergen and separate them by commas to produce your canonical dangerous ingredient list. (There should not be any spaces in your canonical dangerous ingredient list.) In the above example, this would be mxmxvkd,sqjhc,fvjkl.

Time to stock your raft with supplies. What is your canonical dangerous ingredient list?

Your puzzle answer was mfp,mgvfmvp,nhdjth,hcdchl,dvkbjh,dcvrf,bcjz,mhnrqp.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

INPUT = "day21_input.txt"
inp = open(INPUT).read().splitlines()

allergens = dict()
def Part1():
    ingredients = dict()
    for line in inp:
        ingr, alrg = line.split(' (contains ')
        ingr = ingr.split(' ')
        alrg = alrg[:-1].split(', ')
        # loop through ingredients to count them
        for i in ingr:
            if i in ingredients:
                ingredients[i] += 1
            else:
                ingredients[i] = 1
        # loop through these allergens
        for a in alrg:
            # if we have seen this allergen before
            if a in allergens:
                # only keep ingredients we've seen before
                allergens[a] = list(set(allergens[a]).intersection(set(ingr)))
            # new allergen, add these ingredients as potential matches
            else:
                allergens[a] = ingr
    # list of potential ingredients that include allergens
    potentials = set()
    [potentials.update(x) for x in allergens.values()]
    # full set of ingredients minus potential allergen-containing ingredients
    res = set(ingredients.keys()) - potentials
    # count 'em up (we already tallied the uses above, just add together)
    cnt = 0
    for i in res:
        cnt += ingredients[i]
    return cnt

# counts how many ingredients are left in the allergen potential values
def count(alrg):
    cnt = 0
    for i in alrg.values():
        cnt += len(i)
    return cnt

def Part2():
    # reduce ingredients to one per allergen
    while count(allergens) > len(allergens):
        for a in allergens:
            # this is a single ingredient
            if len(allergens[a]) == 1:
                # remove it from all other allergen lists
                for b in allergens:
                    if b != a and allergens[a][0] in allergens[b]:
                        allergens[b].remove(allergens[a][0])
    # print ingredients from sorted allergen list
    res = ""
    for a in sorted(allergens):
        res += allergens[a][0]+','
    return res[:-1] #remove trailing comma

# execute Part 1
print("Part 1:", Part1())
# execute Part 2
print("Part 2:", Part2())
