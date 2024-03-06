import ipdb
class Shape:
    def __init__(self,color_entered, added_by_entered):
        self.color = color_entered
        self.added_by = added_by_entered

    def area(self):
        print ("Area of Shape has been called")
    
    def report(self):
        return f"Reporting for shape of color {self.color}"
    
    def report_author(self):
        return f"This shape was authored by {self.added_by}"
        


shape1 = Shape(color_entered="red", added_by_entered="Mercy")
# ipdb.set_trace()