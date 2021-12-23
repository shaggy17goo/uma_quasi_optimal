
from utilities import *
from rule import *


def aq_specialization(R, W):
    pass


def get_class(k, R):
    pass


if __name__ == "__main__":
    # com = Complex(['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c'])
    # pseed = Complex(['a'], ['b', 'c'], ['c'], ['a'], ['b', 'c'], ['c'])
    # nseed = Complex(['a', 'b', 'c'], ['b', 'c'], ['a', 'c'], ['b', 'c'], ['b', 'c'], ['c'])

    rules = []
    examples = read_examples("../data/car.data")
    examples, W = get_rand_examples(examples, 700)
    examples, T = get_rand_examples(examples, 700)
    R = deepcopy(T)

    while len(R) != 0:
        k = aq_specialization(R, W)
        d = get_class(k, R)
        rules.append(Rule(k, d))

