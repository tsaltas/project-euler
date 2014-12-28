from __future__ import division
from collections import OrderedDict
import itertools


def maximum_consecutive_digits():
    return sorted([[find_longest_sequence(digits), digits] for digits in generate_sets()], reverse=True)[0]


# number of sets with 4 items such that a < b < c < d
def generate_sets():
    return list(itertools.combinations(range(1, 10), 4))


# find longest sequence of consecutive integers generated from set
# input is set of digits
def find_longest_sequence(digits):
    targets = get_sorted_targets(digits)
    if len(targets) == 0 or targets[0] != 1:
        return 0
    else:
        return reduce(lambda x, y: y if y == x + 1 else x, targets)


def get_sorted_targets(digits):
    return sorted(list(OrderedDict.fromkeys(filter(lambda x: isinstance(x, int) and x > 0, get_all_targets(digits)))))


# input is set of 4 digits in a list
# output is a list of all the targets, sorted
def get_all_targets(digits):
    return list(itertools.chain.from_iterable([evaluated_targets(x) for x in list(itertools.permutations(digits))]))


def evaluated_targets(digits):
    return [evaluate(x) for x in expressions_with_parentheses(digits)]


def evaluate(x):
    try:
        value = eval(x)
    except ZeroDivisionError:
        value = 0
    return value


def expressions_with_parentheses(digits):
    return list(itertools.chain.from_iterable(
        [add_parentheses(expressions) for expressions in expressions_with_operations(digits)]))


# input is single expression, in a string
# output is list of all parenthesized versions of the string
def add_parentheses(expression):
    return [
        # no parens
        expression,
        # (a+b)+c+d
        "(" + expression[0:3] + ")" + expression[3:],
        # a+(b+c)+d
        expression[0:2] + "(" + expression[2:5] + ")" + expression[5:],
        # a+b+(c+d)
        expression[0:4] + "(" + expression[4:] + ")",
        # (a+b) + (c+d)
        "(" + expression[0:3] + ")" + expression[3:4] + "(" + expression[4:] + ")",
        # ((a+b)+c) + d
        "((" + expression[0:3] + ")" + expression[3:5] + ")" + expression[5:],
        # (a + (b + c)) + d
        "(" + expression[0:2] + "(" + expression[2:5] + "))" + expression[5:],
        # a + (b + (c+d))
        expression[0:2] + "(" + expression[2:4] + "(" + expression[4:] + "))",
        # a + ((b + c ) + d)
        expression[0:2] + "((" + expression[2:5] + ")" + expression[5:] + ")"
    ]


def expressions_with_operations(digits):
    return [add_operations(digits, operation) for operation in all_operations()]


def add_operations(digits, operations):
    digit = [str(s) for s in digits]
    return digit[0] + operations[0] + digit[1] + operations[1] + digit[2] + operations[2] + digit[3]


def all_operations():
    op = ["+", "-", "*", "/"]
    return [x + y + z for x in op for y in op for z in op]


# Run Script
if __name__ == "__main__":
    print maximum_consecutive_digits()
