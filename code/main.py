from test_utilities import *
from file_utiities import *
from aq_utilities import *
from rule import *

### Global parameters
debug_on = False
custom_neg_seed = True
best_complexes_param = 5
minimize_rules_cnt_param = 0
train_and_wal_size = 700



if __name__ == "__main__":
    #test_one_rule_generate()
    test_generate_and_test_x_rules_sets_voting(100, "testtt1")
    #test_diff_sets_size()
    #test_diff_best_complexes_param()
