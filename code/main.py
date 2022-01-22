from test_utilities import *
from file_utiities import *
from aq_utilities import *
from rule import *
import time

### Global parameters
debug_on = False
custom_neg_seed = True
best_complexes_param = 5
train_and_wal_size = 700

if __name__ == "__main__":
    start_time = time.time()

    ### wygenerowanie jendego zestawu reguł i przeprowadzenie predykcji na jego podstawie (krótki czas testu)
    test_one_rule_generate()

    ### generowanie zestawów reguł i predykcja na podstawie głosowania (długi czas testu)
    test_generate_and_test_x_rules_sets_voting(5, "test5")

    ### przygotowany zestawy reguł do przetestowania głosowania, wynik poprzedniego testu (krótki czas testu)
    test_rules_sets_with_voting("../data/test100/rules", "../data/test100/car.data.test")

    ### Test wyboru najlepszej wartości podziału zborow trenujacego, walidacyjnego, testujacego (bardzo długi czas testu)
    # test_diff_sets_size()

    ### Test wyboru najlepszej wartości parametru best_complexes_param (bardzo długi czas testu)
    # test_diff_best_complexes_param()


