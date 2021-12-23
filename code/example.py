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
