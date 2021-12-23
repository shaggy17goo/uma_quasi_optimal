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
        return 'Complex %s, %s, %s, %s, %s, %s' % (self.buying, self.maint, self.doors, self.persons, self.lug_boot, self.safety)

