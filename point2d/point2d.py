from math import pi
from typing import Self

rad_to_deg = 180/pi # convert radians to degrees
deg_to_rad = pi/180 # convert degrees to radians
class Point2D:
    id = 0
    def __init__(self,  *position):
        """
        Initialize a 2D point with x and y coordinates.
        :param x: X-coordinate of the point (default is 0.0)
        :param y: Y-coordinate of the point (default is 0.0)
        """
        if len(position) == 0:
            self.x = self.y = 0.0
        elif len(position) == 1:
            if isinstance(position[0], Point2D):
                self.x = position[0].x
                self.y = position[0].y
            elif isinstance(position[0], (int, float)):
                self.x = position[0]
                self.y = 0.0
            elif isinstance(position[0], (list, tuple)) and len(position[0]) == 1:
                self.x = position[0][0]
                self.y = 0.0
            elif isinstance(position[0], (list, tuple)) and len(position[0]) == 2:
                self.x = position[0][0]
                self.y = position[0][1]
            else:
                raise TypeError('Point2d. Point2D(P). Illegal P argument type, must be Point2D, list, tuple, int, or float')
        elif len(position) == 2:
            if not all(isinstance(coord, (int, float)) for coord in position):
                raise TypeError('Point2d. Point2D(x, y). x and y must be int or float')

            self.x = position[0]
            self.y = position[1]
        else:
            raise TypeError('Point2d. Point2D(x, y). Illegal number of arguments, must be 0, 1 or 2')
        self.id = Point2D.id
        Point2D.id += 1 
    @property
    def x(self):
        """Get the x-coordinate of the point."""
        return self._x
    
    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the point.
        :param value: New x-coordinate (must be int or float)
        """
        if not isinstance(value, (int, float)):
            raise TypeError("x coordinate must be int or float")
        self._x = value
    @property
    def y(self):
        """Get the y-coordinate of the point."""
        return self._y
    
    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the point.
        :param value: New y-coordinate (must be int or float)
        """
        if not isinstance(value, (int, float)):
            raise TypeError("y coordinate must be int or float")
        self._y = value    
    @property
    def get_id(self):
        """
        Get the unique identifier of the Point2D instance.
        :return: Unique identifier as an integer.
        """
        return self.id
    def is_zero(self) -> bool:
        """
        Check if the point is at the origin (0, 0).
        :return: True if the point is at the origin, False otherwise.
        """
        return self.x == 0.0 and self.y == 0.0
    def non_zero(self) -> bool:
        """
        Check if the point is not at the origin (0, 0).
        :return: True if the point is not at the origin, False otherwise.
        """
        return not self.is_zero()
    
    def set_polar(self, radius: float, angle: float) -> None: 
        """
        Set the point's coordinates using polar coordinates.
        :param radius: Distance from the origin.
        :param angle: Angle in degrees.
        """
        if not isinstance(radius, (int, float)) or not isinstance(angle, (int, float)):
            raise TypeError("radius and angle must be int or float")
        from math import cos, sin
        if radius < 0:
            raise ValueError("radius must be non-negative")
        angle = angle * deg_to_rad
        self.x = radius * +cos(angle)
        self.y = radius * -sin(angle)      
    
    def get_polar(self) -> tuple:
        """
        Get the polar coordinates of the point.
        :return: A tuple (radius, angle) where radius is the distance from the origin and angle is in degrees.
        """
        from math import atan2, sqrt
        radius = sqrt(self.x ** 2 + self.y ** 2)
        
        # Handle the origin case (0,0) specially to avoid undefined angle
        if radius == 0:
            return (0.0, 0.0)
        
        angle = atan2(-self.y, self.x) * rad_to_deg
        
        # Normalize angle to the range [0, 360) for positive x-axis,
        # or [-180, 180) in general, matching the test's expectations
        if angle < 0:
            angle += 360
        return (radius, angle)

    def midpoint_to(self, other: Self) -> Self:
        """
        Calculate the midpoint between this point and another Point2D.
        :param other: Another Point2D instance.
        :return: A new Point2D instance representing the midpoint.
        """
        if not isinstance(other, Point2D):
            raise TypeError("Argument must be of type Point2D")
        mid_x = (self.x + other.x) / 2
        mid_y = (self.y + other.y) / 2
        return Point2D(mid_x, mid_y)

    def midpoint_to_xy(self, x: float, y: float) -> Self:
        """
        Calculate the midpoint between this point and a given (x, y) coordinate.
        :param x: X-coordinate of the other point.
        :param y: Y-coordinate of the other point.
        :return: A new Point2D instance representing the midpoint.
        """
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("x and y must be int or float")
        mid_x = (self.x + x) / 2
        mid_y = (self.y + y) / 2
        return Point2D(mid_x, mid_y)
    def midpoint_p1_p2(self, other: Self) -> Self:
        """
        Calculate the midpoint between this point and another Point2D.
        :param other: Another Point2D instance.
        :return: A new Point2D instance representing the midpoint.
        """
        if not isinstance(other, Point2D):
            raise TypeError("Argument must be of type Point2D")
        mid_x = (self.x + other.x) / 2
        mid_y = (self.y + other.y) / 2
        return Point2D(mid_x, mid_y)

    def __repr__(self):
        """
        Return a string representation of the Point2D instance.
        """
        return f"Point2D(x={self.x}, y={self.y})"

    def __eq__(self, other):
        """
        Check if two Point2D instances are equal.
        :param other: Another Point2D instance to compare with.
        """
        if isinstance(other, Point2D):
            return self.x == other.x and self.y == other.y
        return False

    def distance_to(self, other):
        """
        Calculate the Euclidean distance to another Point2D.
        :param other: Another Point2D instance.
        :return: Euclidean distance as a float.
        """
        if not isinstance(other, Point2D):
            raise TypeError("Argument must be of type Point2D")
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def normalize(self) -> bool:
        """
        Normalize the point to have a unit distance from the origin.
        If the point is at the origin, it remains unchanged.
        """
        if self.is_zero():
            return False
        distance = self.distance_to(Point2D(0, 0))
        if distance == 0:
            raise ValueError("Cannot normalize a point at the origin")
            return False
        elif distance < 0:
            raise ValueError("Distance must be non-negative")
            return False
        elif distance < 1:
            self.x *= distance
            self.y *= distance
            return True
        elif distance == 1:
            self.x = 1
            self.y = 0
            return True
        else:
            self.x /= distance
            self.y /= distance
            return True
