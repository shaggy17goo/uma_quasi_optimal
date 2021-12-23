from complex import *


class Rule:

    def __init__(self, com, val):
        self.complex = com
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
