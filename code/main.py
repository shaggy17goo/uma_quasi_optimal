from test_utilities import *
from file_utiities import *
from aq_utilities import *
from rule import *





if __name__ == "__main__":
    '''
    while 1:
        examples = read_examples("../v3/car.data.tren_wal")
        examples, T = get_rand_examples(examples, 500)
        examples, W = get_rand_examples(examples, 500)

        rules = generate_rules(T, W)
        save_rules(rules)
    '''
    #divide_file_randomly_on_two_parts("../data/car.data",1000)

#    '''
    test = read_examples("../v3/car.data.test")
    rules_sets = []
    for i in range(100):
        rules_sets.append(read_rules(f"../v3/rules/rules.{i + 1}.pkl"))

    shuffle(rules_sets)
    print(f"accuracy: {test_rules_sets_with_voting(rules_sets[0:150], test)}")
#'''