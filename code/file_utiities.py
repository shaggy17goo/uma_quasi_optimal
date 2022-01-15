import os
import pickle
import re
from pathlib import Path
from random import randint
from example import *


def read_examples(path):
    examples = []
    file = open(path, "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        split_line = line.split(',')
        examples.append(
            Example(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4], split_line[5],
                    split_line[6][:-1]))
    return examples


def save_rules(rules):
    rules_dir = "../v3/rules/"
    Path(rules_dir).mkdir(parents=True, exist_ok=True)
    existing_rules_sets = os.listdir(rules_dir)
    if len(existing_rules_sets) == 0:
        rules_set_name = "rules.1.pkl"
    else:
        existing_rules_sets = sorted(existing_rules_sets, key=lambda x: (len(x), x))
        lastindex = re.search('\d+', existing_rules_sets[-1]).group(0)
        rules_set_name = "rules." + str(int(lastindex) + 1) + ".pkl"

    with open(rules_dir + rules_set_name, 'wb') as outp:
        pickle.dump(rules, outp, pickle.HIGHEST_PROTOCOL)


def read_rules(path):
    with open(path, 'rb') as inp:
        rules = pickle.load(inp)
    return rules


def divide_file_randomly_on_two_parts(path, cnt):
    file = open(path, "r")
    rest = file.readlines()
    file.close()
    extracted = []
    for i in range(0, cnt):
        extracted.append(rest.pop(randint(0, len(rest) - 1)))

    file = open(path + "extracted", "w")
    for element in extracted:
        file.write(element)
    file.close()

    file = open(path + "rest", "w")
    for element in rest:
        file.write(element)
    file.close()
