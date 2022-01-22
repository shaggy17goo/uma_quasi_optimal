from test_utilities import *
from file_utiities import *
from aq_utilities import *
from rule import *
import time

### Global parameters
debug_on = False
custom_neg_seed = True
best_complexes_param = 5
minimize_rules_cnt_param = 0
train_and_wal_size = 700

if __name__ == "__main__":
    start_time = time.time()

    ### wygenerowanie jendego zestawu reguł i przeprowadzenie predykcji na jego podstawie (krótki czas testu)
    test_one_rule_generate()

    print("--- Generation time: %s seconds ---\n\n\n\n" % (time.time() - start_time))

    ### Test wyboru najlepszej wartości podziału zborow trenujacego, walidacyjnego, testujacego (bardzo długi czas testu)
    # test_diff_sets_size()

    ### Test wyboru najlepszej wartości parametru best_complexes_param (bardzo długi czas testu)
    # test_diff_best_complexes_param()

    ### generowanie dzestawu reguł i predykcja na podstawie głosowania (bardzo długi czas testu)
    # test_generate_and_test_x_rules_sets_voting(100, "test100")

    ### przygotowany zestawy reguł do przetestowania głosowania, wynik poprzedniego testu (krótki czas testu)
    test_rules_sets_with_voting("../data/test100/rules", "../data/test100/car.data.test")


