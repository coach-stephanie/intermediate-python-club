"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

class Classy(object):
    ITEM_TO_CLASSINESS = {"tophat": 2, "bowtie": 4, "monocle": 5}

    def __init__(self):
        self.items = []
        self.classiness = 0
    
    def add_item(self, s):
        self.items.append(s)
        self.update_classiness(s)
        
    def update_classiness(self, s):
        self.classiness += ITEM_TO_CLASSINESS.get(s, 0)
        
    def get_classiness(self):
        return self.classiness

# _ = private, pls don't use
# __ = private, not visible outside of class 
#instead of getters and setters, python uses the property decorator 

class Classy2:
    ITEM_TO_CLASSINESS = {"tophat": 2, "bowtie": 4, "monocle": 5}

    def __init__(self):
        self._items = []
        self._classiness = 0

    def add_item(self, item: str):
        self._items.append(item)
        self._classiness += ITEM_TO_CLASSINESS.get(item, 0)

    @property
    def classiness() -> int:
        return self._classiness


me2 = Classy2()
print(me.classiness)
me.add_item("tophat")
print(me.classiness)
        

# Test cases
me = Classy()

# Should be 0
print me.get_classiness()

me.add_item("tophat")
# Should be 2
print me.get_classiness()

me.add_item("bowtie")
me.add_item("jacket")
me.add_item("monocle")
# Should be 11
print me.get_classiness()

me.add_item("bowtie")
# Should be 15
print me.get_classiness()