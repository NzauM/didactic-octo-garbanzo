from shape import Shape
import ipdb
print("Hereee")
class Circle(Shape):
    def __init__(self, color_entered, added_by_entered, radius_entered):
        super().__init__(color_entered=color_entered, added_by_entered=added_by_entered)
        self.radius = radius_entered

    def report(self):
        return f"Reporting for Circle of color {self.color}"
    
    def area(self):
        super().area()
        return 3.142 * self.radius * self.radius
    pass


circle1 = Circle("Yellow", "Waeni", 24)
ipdb.set_trace()