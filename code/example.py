from complex import *


class Example:

    def __init__(self, buying, maint, doors, persons, lug_boot, safety, val):
        self.complex = Complex([buying], [maint], [doors], [persons], [lug_boot], [safety])
        self.value = val

    def __str__(self):
        return 'Complex %s, %s, %s, %s, %s, %s - class: %s' % (
            self.complex.buying,
            self.complex.maint,
            self.complex.doors,
            self.complex.persons,
            self.complex.lug_boot,
            self.complex.safety,
            self.value
        )


def get_distance_between_examples(e1, e2):
    score = 0
    if e1.complex.safety != e2.complex.safety:
        score += 1
    if e1.complex.buying != e2.complex.buying:
        score += 1
    if e1.complex.maint != e2.complex.maint:
        score += 1
    if e1.complex.lug_boot != e2.complex.lug_boot:
        score += 1
    if e1.complex.persons != e2.complex.persons:
        score += 1
    if e1.complex.doors != e2.complex.doors:
        score += 1
    return score
