# In presentation we have mentioned something called inheritance.
# Check these two videos (or just google any  article yoou want) and try to learn the basics of Inheritance in Python.
# https://www.youtube.com/watch?v=RSl87lqOXDE
# https://www.youtube.com/watch?v=H2SQrZK2nvM

# As an assignment try to create parent/base class  called Triangle which would be instantiated with lengths of its
# sides. E.g. Triangle(a,b,c) Then crete subclasses of Triangle called EquilateralTriangle (all sides equal) and
# IsoscelesTriangle(two sides are equal) using the inheritance principle.
# For all three classes use their method to
# compute `area` of the shape. Hint: You can implement only 1 method `compute_area` to cover all three cases

class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def compute_area(self):
        import math
        s = (self.a + self.b + self.c)/2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

class EquilateralTriangle(Triangle):

    def __init__(self, a):
        self.a = a
        self.b = a
        self.c = a

class IsoscelesTriangle(Triangle):

    def __init__(self, a, b):
        self.a = a
        self.b = a
        self.c = b

triangle1 = Triangle(2,3,4)
triangle2 = EquilateralTriangle(4)
triangle3 = IsoscelesTriangle(5, 4)
area1 = triangle1.compute_area()
area2 = triangle2.compute_area()
area3 = triangle3.compute_area()
print(f"Calculated aeras: {area1:.2f}, {area2:.2f}, {area2:.2f}")
