"""
--- Day 18: Operation Order ---
As you look out the window and notice a heavily-forested continent slowly appear over the horizon, you are interrupted by the child sitting next to you. They're curious if you could help them with their math homework.

Unfortunately, it seems like this "math" follows different rules than you remember.

The homework (your puzzle input) consists of a series of expressions that consist of addition (+), multiplication (*), and parentheses ((...)). Just like normal math, parentheses indicate that the expression inside must be evaluated before it can be used by the surrounding expression. Addition still finds the sum of the numbers on both sides of the operator, and multiplication still finds the product.

However, the rules of operator precedence have changed. Rather than evaluating multiplication before addition, the operators have the same precedence, and are evaluated left-to-right regardless of the order in which they appear.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
      9   + 4 * 5 + 6
         13   * 5 + 6
             65   + 6
                 71
Parentheses can override this order; for example, here is what happens if parentheses are added to form 1 + (2 * 3) + (4 * (5 + 6)):

1 + (2 * 3) + (4 * (5 + 6))
1 +    6    + (4 * (5 + 6))
     7      + (4 * (5 + 6))
     7      + (4 *   11   )
     7      +     44
            51
Here are a few more examples:

2 * 3 + (4 * 5) becomes 26.
5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.
Before you can help with the homework, you need to understand it yourself. Evaluate the expression on each line of the homework; what is the sum of the resulting values?

Your puzzle answer was 21993583522852.

--- Part Two ---
You manage to answer the child's questions and they finish part 1 of their homework, but get stuck when they reach the next section: advanced math.

Now, addition and multiplication have different precedence levels, but they're not the ones you're familiar with. Instead, addition is evaluated before multiplication.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are now as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
  3   *   7   * 5 + 6
  3   *   7   *  11
     21       *  11
         231
Here are the other examples from above:

1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
2 * 3 + (4 * 5) becomes 46.
5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.
What do you get if you add up the results of evaluating the homework problems using these new rules?

Your puzzle answer was 122438593522757.

Both parts of this puzzle are complete! They provide two gold stars: **
"""
import re

INPUT = "day18_input.txt"
inp = [l.replace(' ','') for l in open(INPUT).read().splitlines()]

def evaluateP1(exp):
    # all operations treated the same
    res = exp
    # find next operation (starting at beginning of string)
    m = re.match("[0-9]+[\+|\*][0-9]+",exp)
    while m:
        # evaluate the equation
        res = eval(m.group(0))
        # use this result plus the rest of the string
        exp = str(res)+exp[len(m.group(0)):]
        # try it again on the new string
        m = re.match("[0-9]+[\+|\*][0-9]+",exp)
    return res

def evaluateP2(exp):
    # additions evaluated first
    adds = re.findall("[0-9]+\+[0-9]+",exp)
    # while there are additions to be made
    while adds != []:
        # evaluation this equation
        e = adds[0]
        r = str(eval(e))
        # replace its location in the expression
        exp = exp.replace(e,r,1)
        # find the next addition to be made
        adds = re.findall("[0-9]+[\+][0-9]+",exp)
    # all that's left is multiplication, return evaluation of it
    return eval(exp)

def reduce(exp,evaluate):
    openloc = exp.find('(')
    # no parenthesis found, evaluate expression as-is
    if openloc == -1:
        return str(evaluate(exp))
    else:
        # find matching close
        opens = 1
        for x in range(openloc+1,len(exp)):
            if exp[x] == '(':
                opens += 1
            elif exp[x] == ')':
                opens -= 1
                if opens == 0:
                    # found the close, build new expression with everything before,
                    # everything after, and the new reduced expression in the middle
                    newstr = exp[0:openloc] + reduce(exp[openloc+1:x],evaluate) + exp[x+1:]
                    # reduce the reduced expression to the smallest form we can
                    return reduce(newstr,evaluate)
        
def Solve(evalFunc):
    res = 0
    for exp in inp:
        # reduce and evaluate all expressions, summing the result
        res += int(reduce(exp,evalFunc))
    return res

# execute Part 1 (use evaluateP1 function)
print("Part 1:", Solve(evaluateP1))
# execute Part 2 (use evaluateP2 function)
print("Part 2:", Solve(evaluateP2))
