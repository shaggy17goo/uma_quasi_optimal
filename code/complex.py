import collections


class Complex:
    buying = []
    maint = []
    doors = []
    persons = []
    lug_boot = []
    safety = []

    def __init__(self, buying, maint, doors, persons, lug_boot, safety):
        self.buying = buying
        self.maint = maint
        self.doors = doors
        self.persons = persons
        self.lug_boot = lug_boot
        self.safety = safety

    def __str__(self):
        return 'Complex %s, %s, %s, %s, %s, %s' % (
            self.buying, self.maint, self.doors, self.persons, self.lug_boot, self.safety)

    def __eq__(self, other):
        if not collections.Counter(self.buying) == collections.Counter(other.buying):
            return 0
        if not collections.Counter(self.maint) == collections.Counter(other.maint):
            return 0
        if not collections.Counter(self.doors) == collections.Counter(other.doors):
            return 0
        if not collections.Counter(self.persons) == collections.Counter(other.persons):
            return 0
        if not collections.Counter(self.lug_boot) == collections.Counter(other.lug_boot):
            return 0
        if not collections.Counter(self.safety) == collections.Counter(other.safety):
            return 0
        return 1

def get_full_complex():
    return Complex(["vhigh", "high", "med", "low"], ["vhigh", "high", "med", "low"], ["2", "3", "4", "5more"],
                   ["2", "4", "more"], ["small", "med", "big"], ["high", "med", "low"])
