
import math

class IShape:
    """ Interface for Shape classes, defines the perimeter and area methods
    """
    
    def perimeter(self):
        """ returns the perimeter of the shape
        """
        return None
    
    def area(self):
        """ returns the area of the shape
        """
        return None
    
    
class Disk(IShape):
    """ Disk Shape class
    """
    
    def __init__(self, radius):
        self.radius = radius
        return
        
    def perimeter(self):
        return 2.*math.pi*self.radius
    
    def area(self):
        return math.pi*self.radius*self.radius
    
    
class Rectangle(IShape):
    """ Rectangle Shape class
    """
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        return
    
    def perimeter(self):
        return 2.*(self.width+self.height)
    
    def area(self):
        return self.width*self.height
    
    
class Square(Rectangle):
    """ Square Shape class
    """
    
    def __init__(self, size):
        Rectangle.__init__(self, size, size)
        return
    