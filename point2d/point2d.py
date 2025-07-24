from math import pi, sqrt, degrees, radians, atan2
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
    
    def radius(self) -> float:
        """
        Calculate the distance from the point to the origin (0, 0).
        :return: Distance as a float.
        """
        return (sqrt(self.x * self.x + self.y * self.y))

    def angle_rad(self) -> float:
        """
        Calculate the angle of the point in radians.
        :return: Angle in radians as a float.
        """
        from math import atan2
        return atan2(-self.y, self.x)

    def angle_deg(self) -> float:
        """
        Calculate the angle of the point in degrees.
        :return: Angle in degrees as a float.
        """
        angle = self.angle_rad() * rad_to_deg
        if angle < 0:
            angle += 360
        return angle

    def set_cartesian(self, x: float, y: float) -> None:
        """
        Set the point's coordinates using Cartesian coordinates.
        :param x: X-coordinate of the point.
        :param y: Y-coordinate of the point.
        """
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("x and y must be int or float")
        self.x = x
        self.y = y
            
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
        radius = sqrt(self.x * self.x + self.y * self.y)

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
        mid_x = 0.5 * (self.x + other.x)
        mid_y = 0.5 * (self.y + other.y)
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
        mid_x = 0.5 * (self.x + x)
        mid_y = 0.5 * (self.y + y)
        return Point2D(mid_x, mid_y)
    def midpoint_p1_p2(self, other: Self) -> Self:
        """
        Calculate the midpoint between this point and another Point2D.
        :param other: Another Point2D instance.
        :return: A new Point2D instance representing the midpoint.
        """
        if not isinstance(other, Point2D):
            raise TypeError("Argument must be of type Point2D")
        mid_x = 0.5 * (self.x + other.x)
        mid_y = 0.5 * (self.y + other.y)
        return Point2D(mid_x, mid_y)

    def __repr__(self):
        """
        Return a string representation of the Point2D instance.
        """
        return "Point2D(%g, %g)" % tuple(map(float, [self.x, self.y]))

    def __eq__(self, other):
        """
        Check if two Point2D instances are equal.
        :param other: Another Point2D instance to compare with.
        """
        if isinstance(other, Point2D):
            return self.x == other.x and self.y == other.y
        return False

    def __ne__(self, other):
        """
        Check if two Point2D instances are not equal.
        :param other: Another Point2D instance to compare with.
        """
        if isinstance(other, Point2D):
            return not self.__eq__(other)
        return True

    def __cmp__(self, other):
        """
        Compare two Point2D instances.
        :param other: Another Point2D instance to compare with.
        :return: -1 if self < other, 0 if self == other, 1 if self > other.
        """
        if not isinstance(other, Point2D):
            raise TypeError("Argument must be of type Point2D")
        if self.x < other.x or (self.x == other.x and self.y < other.y):
            return -1
        elif self.x == other.x and self.y == other.y:
            return 0
        else:
            return 1
    def __neg__(self):
        """
        Negate the point's coordinates.
        :return: A new Point2D instance with negated coordinates.
        """
        return Point2D(-self.x, -self.y)

    def __pos__(self):
        """
        Return a copy of the point with positive coordinates.
        :return: A new Point2D instance with positive coordinates.
        """
        return Point2D(abs(self.x), abs(self.y))
    
    def positive(self) -> Self:
        """
        Return a new Point2D instance with positive coordinates.
        :return: A new Point2D instance with positive coordinates.
        """
        return +self

    def negate(self) -> Self:
        """
        Negate the point's coordinates.
        :return: A new Point2D instance with negated coordinates.
        """
        return -self
    
    def swap(self) -> None:
        """
        Swap the x and y coordinates of the point.
        """
        self.x, self.y = self.y, self.x

    def swap_xy(self) -> Self:
        """
        Swap the x and y coordinates of the point.
        :return: A new Point2D instance with swapped coordinates.
        """
        return Point2D(self.y, self.x)

    def distance_to_squared(self, other):
        """
        Calculate the squared Euclidean distance to another Point2D.
        :param other: Another Point2D instance.
        :return: Squared Euclidean distance as a float.
        """
        if not isinstance(other, Point2D):
            raise TypeError("Argument must be of type Point2D")
        return (self.x - other.x) * (self.x - other.x) + (self.y - other.y) * (self.y - other.y)
    
    def distance_to(self, other: Self) -> float:
        """
        Calculate the Euclidean distance to another Point2D.
        :param other: Another Point2D instance.
        :return: Euclidean distance as a float.
        """
        if not isinstance(other, Point2D):
            raise TypeError("Argument must be of type Point2D")
        return sqrt(self.distance_to_squared(other))
    def angle_to_rad(self, other: Self) -> float:
        """
        Calculate the angle in radians from this point to another Point2D.
        :param other: Another Point2D instance.
        :return: Angle in radians as a float.
        """
        if not isinstance(other, Point2D):
            raise TypeError("Argument must be of type Point2D")
        from math import atan2
        angle_rad = atan2(-(other.y - self.y), other.x - self.x)
        return angle_rad if angle_rad >= 0 else angle_rad + 2 * pi

    def angle_to_deg(self, other: Self) -> float:
        """
        Calculate the angle in degrees from this point to another Point2D.
        :param other: Another Point2D instance.
        :return: Angle in degrees as a float.
        """
        if not isinstance(other, Point2D):
            raise TypeError("Argument must be of type Point2D")
        return degrees(self.angle_to_rad(other))
   
    def distance_to_xy(self, x: float, y: float) -> float:
        """
        Calculate the Euclidean distance to a given (x, y) coordinate.
        :param x: X-coordinate of the other point.
        :param y: Y-coordinate of the other point.
        :return: Euclidean distance as a float.
        """
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("x and y must be int or float")
        return sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

    def normalize(self) -> bool:
        """
        Normalize the point to have a unit distance from the origin.
        If the point is at the origin, it remains unchanged.
        """
        if self.is_zero():
            return False
        length = self.distance_to_squared(Point2D(0, 0))
        if length == 0:
            return False
        elif length == 1:
            return True
        else:
            self.x /= sqrt(length)
            self.y /= sqrt(length)
            return True

    def normalized(self) -> Self:
        """
        Return a new normalized instance of the point.
        """
        if self.is_zero():
            return Point2D(0, 0)
        length = self.distance_to_squared(Point2D(0, 0))
        if length == 0:
            return Point2D(0, 0)
        elif length == 1:
            return Point2D(self.x, self.y)
        else:
            return Point2D(self.x / sqrt(length), self.y / sqrt(length))

    def dot_product(self, other: Self) -> float:
        """
        Calculate the dot product with another Point2D.
        :param other: Another Point2D instance.
        :return: Dot product as a float.
        """
        if not isinstance(other, Point2D):
            raise TypeError("Argument must be of type Point2D")
        return self.x * other.x + self.y * other.y
    
    def cross_product(self, other: Self) -> float:
        """
        Calculate the cross product with another Point2D.
        :param other: Another Point2D instance.
        :return: Cross product as a float.
        """
        if not isinstance(other, Point2D):
            raise TypeError("Argument must be of type Point2D")
        return self.x * other.y - self.y * other.x

    def magnitude(self) -> float:
        """
        Calculate the magnitude (length) of the point vector.
        :return: Magnitude as a float.
        """
        # return sqrt(self.x * self.x + self.y * self.y)
        return sqrt(self.dot_product(self))
    
    def scale_factor(self, a: float | int, b: float | int) -> Self:
        """
        Scale the point by a factor of (a, b).
        :param a: Scaling factor for x-coordinate.
        :param b: Scaling factor for y-coordinate.
        :return: A new Point2D instance representing the scaled point.
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Scaling factors must be int or float")
        return Point2D(self.x * a, self.y * b)

    def scale(self, scalar: float | int) -> Self:
        """
        Scale the point by a scalar value.
        :param scalar: Scalar value to scale the point.
        :return: A new Point2D instance representing the scaled point.
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be int or float")
        return  self.scale_factor(scalar, scalar)
    
    def direction(self) -> Self:
        """
        Get the direction of the point vector.
        :return: A new Point2D instance representing the direction.
        """
        if self.is_zero():
            return Point2D(0, 0)
        length = self.magnitude()
        return Point2D(self.x / length, self.y / length)

    def distance_between(p1: Self, p2: Self) -> float:
        """
        Calculate the Euclidean distance between two Point2D instances.
        :param p1: The first Point2D instance.
        :param p2: The second Point2D instance.
        :return: Euclidean distance as a float.
        """
        if not isinstance(p1, Point2D) or not isinstance(p2, Point2D):
            raise TypeError("Both arguments must be of type Point2D")
        return p1.distance_to(p2)
    
    def distance_between_xy(p1: Self, x: float, y: float) -> float:
        """
        Calculate the Euclidean distance between a Point2D instance and a (x, y) coordinate.
        :param p1: The Point2D instance.
        :param x: The x-coordinate.
        :param y: The y-coordinate.
        :return: Euclidean distance as a float.
        """
        if not isinstance(p1, Point2D):
            raise TypeError("First argument must be of type Point2D")
        return p1.distance_to_xy(x, y) 
    
    def clone(self) -> Self:
        """
        Create a clone of the Point2D instance.
        :return: A new Point2D instance with the same coordinates.
        """
        return Point2D(self.x, self.y) 

    def __hash__(self):
        """
        Return a hash value for the Point2D instance.
        This allows Point2D instances to be used as keys in dictionaries or added to sets.
        :return: Hash value as an integer.
        """
        return hash((self.x, self.y))
    def __str__(self):
        """
        Return a string representation of the Point2D instance.
        :return: String representation as "(x, y)".
        """
        return "(x: %g, y:%g)" % tuple(map(float, [self.x, self.y]))

    def __bool__(self):
        """
        Check if the Point2D instance is non-zero.
        :return: True if the point is not at the origin (0, 0), False otherwise.
        """
        return not self.is_zero()

    def add_xy(self, x: int | float, y: int | float) -> Self:
        """
        Add a (x, y) coordinate to the current point.
        :param x: The x-coordinate to add.
        :param y: The y-coordinate to add.
        :return: The current Point2D instance after addition.
        """
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("x and y must be int or float")
        self.x += x
        self.y += y
        return self

    def add_point(self, other: Self) -> Self:
        """
        Add another Point2D instance to the current point.
        :param other: Another Point2D instance to add.
        :return: The current Point2D instance after addition.
        """
        if not isinstance(other, Point2D):
            raise TypeError("Argument must be of type Point2D")
        self.x += other.x
        self.y += other.y
        return self
    
    def __add__(self, other: Self) -> Self:
        """
        Add two Point2D instances.
        :param other: Another Point2D instance.
        :return: A new Point2D instance representing the sum.
        """
        if not isinstance(other, Point2D):
            raise TypeError("Argument must be of type Point2D")
        return Point2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: Self) -> Self:
        """
        In-place addition of two Point2D instances.
        :param other: Another Point2D instance.
        :return: The current Point2D instance after addition.
        """
        if not isinstance(other, Point2D):
            raise TypeError("Argument must be of type Point2D")
        self.x += other.x
        self.y += other.y
        return self
    def __radd__(self, other: Self) -> Self:
        """
        Right addition of two Point2D instances.
        :param other: Another Point2D instance.
        :return: A new Point2D instance representing the sum.
        """
        if not isinstance(other, Point2D):
            raise TypeError("Argument must be of type Point2D")
        return Point2D(other.x + self.x, other.y + self.y)
    
    def __sub__(self, other: Self) -> Self:
        """
        Subtract two Point2D instances.
        :param other: Another Point2D instance.
        :return: A new Point2D instance representing the difference.
        """
        if not isinstance(other, Point2D):
            raise TypeError("Argument must be of type Point2D")
        return Point2D(self.x - other.x, self.y - other.y)
    def __isub__(self, other: Self) -> Self:
        """
        In-place subtraction of two Point2D instances.
        :param other: Another Point2D instance.
        :return: The current Point2D instance after subtraction.
        """
        if not isinstance(other, Point2D):
            raise TypeError("Argument must be of type Point2D")
        self.x -= other.x
        self.y -= other.y
        return self
    def __rsub__(self, other: Self) -> Self:
        """
        Right subtraction of two Point2D instances.
        :param other: Another Point2D instance.
        :return: A new Point2D instance representing the difference.
        """
        if not isinstance(other, Point2D):
            raise TypeError("Argument must be of type Point2D")
        return Point2D(other.x - self.x, other.y - self.y)
    
    def __mul__(self, scalar: float | int) -> Self:
        """
        Multiply a Point2D instance by a scalar value.
        :param scalar: Scalar value to multiply the point.
        :return: A new Point2D instance representing the scaled point.
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be int or float")
        return Point2D(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar: float | int) -> Self:
        """
        Divide a Point2D instance by a scalar value.
        :param scalar: Scalar value to divide the point.
        :return: A new Point2D instance representing the scaled point.
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be int or float")
        if scalar == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return Point2D(self.x / scalar, self.y / scalar)
    def __floordiv__(self, scalar: float | int) -> Self:
        """
        Floor divide a Point2D instance by a scalar value.
        :param scalar: Scalar value to floor divide the point.
        :return: A new Point2D instance representing the floored point.
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be int or float")
        if scalar == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return Point2D(self.x // scalar, self.y // scalar)
    def __mod__(self, scalar: float | int) -> Self:
        """
        Modulo a Point2D instance by a scalar value.
        :param scalar: Scalar value to modulo the point.
        :return: A new Point2D instance representing the moduloed point.
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be int or float")
        if scalar == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return Point2D(self.x % scalar, self.y % scalar)
    def __pow__(self, exponent: float | int) -> Self:
        """
        Raise a Point2D instance to a scalar power.
        :param exponent: Scalar exponent to raise the point.
        :return: A new Point2D instance representing the point raised to the power.
        """
        if not isinstance(exponent, (int, float)):
            raise TypeError("Exponent must be int or float")
        return Point2D(self.x ** exponent, self.y ** exponent)
    def __abs__(self) -> Self:
        """
        Return the absolute value of a Point2D instance.
        :return: A new Point2D instance representing the absolute values.
        """
        return Point2D(abs(self.x), abs(self.y))
    def __bool__(self) -> bool:
        """
        Return the truth value of a Point2D instance.
        :return: True if either coordinate is non-zero, False otherwise.
        """
        return bool(self.x) or bool(self.y)
    def __getstate__(self):
        """
        Get the state of the Point2D instance for pickling.
        :return: A dictionary representation of the Point2D instance.
        """
        return {"x": self.x, "y": self.y}
    def __setstate__(self, state):
        """
        Set the state of the Point2D instance from a dictionary.
        :param state: A dictionary representation of the Point2D instance.
        """
        self.x = state["x"]
        self.y = state["y"]
    def __reduce__(self):
        """
        Reduce the Point2D instance for pickling.
        :return: A tuple containing the class name and the state dictionary.
        """
        return (self.__class__.__name__, self.__getstate__())
    
    def __clone__(self):
        """
        Create a clone of the Point2D instance.
        :return: A new Point2D instance with the same coordinates.
        """
        return Point2D(self.x, self.y) 
    def __copy__(self):
        """
        Create a shallow copy of the Point2D instance.
        :return: A new Point2D instance with the same coordinates.
        """
        return Point2D(self.x, self.y)
    def __deepcopy__(self, memo=None):
        """
        Create a deep copy of the Point2D instance.
        :param memo: A dictionary to keep track of copied objects.
        :return: A new Point2D instance with the same coordinates.
        """
        if memo is None:
            memo = {}
        if id(self) in memo:
            return memo[id(self)]
        copy = Point2D(self.x, self.y)
        memo[id(self)] = copy
        return copy
    def __format__(self, format_spec):
        """
        Format the Point2D instance for string representation.
        :param format_spec: The format specification.
        :return: A formatted string representation of the Point2D instance.
        """
        if format_spec == "polar":
            r = abs(self)
            theta = math.atan2(self.y, self.x)
            return f"({r}, {theta})"
        return f"({self.x}, {self.y})"
    def __dir__(self):
        """
        Get a list of valid attributes for the Point2D instance.
        :return: A list of attribute names.
        """
        return ["x", "y"]
    def __sizeof__(self):
        """
        Get the size of the Point2D instance.
        :return: The size of the Point2D instance in bytes.
        """
        return sys.getsizeof(self.x) + sys.getsizeof(self.y)
