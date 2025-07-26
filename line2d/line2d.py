from point2d.point2d import Point2D
from typing import Self
try:
    from .version import __version__
except ImportError:
    __version__ = "unknown"
from math import pi, atan2, sqrt, fabs, cos, sin, degrees, radians

class Line2D:
    def __init__(self, *points):
        if len(points) == 0:
            self._pt1 = Point2D()
            self._pt2 = Point2D()
        elif len(points) == 1:
            if isinstance(points[0], Line2D):
                self._pt1 = points[0]._pt1
                self._pt2 = points[0]._pt2
            else:
                raise TypeError("Line2D.init(line: Expected a Line2D instance.")
        elif len(points) == 2:
            if not all(isinstance(pt, Point2D) for pt in points):
                raise TypeError("Line2D.init(points: Expected two Point2D instances.")
            self._pt1 = points[0]
            self._pt2 = points[1]
        elif len(points) == 4:
            if not all(isinstance(pt, (int, float)) for pt in points):
                raise TypeError("Line2D.init(points: Expected four numeric values.")
            x1 = points[0]
            y1 = points[1]
            x2 = points[2]
            y2 = points[3]
            self._pt1 = Point2D(x1, y1)
            self._pt2 = Point2D(x2, y2)
        else:
            raise ValueError("Too many points provided.")
    
    @property
    def sp(self) -> Point2D:
        """Get the start point of the line."""
        if not isinstance(self._pt1, Point2D):
            raise TypeError("Start point must be a Point2D instance.")
        return self._pt1
    @sp.setter
    def sp(self, point):
        """Set the start point of the line."""
        if isinstance(point, Point2D):
            self._pt1 = point
        elif isinstance(point, (tuple | list)) and len(point) == 2:
            if not all(isinstance(coord, (int, float)) for coord in point):
                raise TypeError("Coordinates must be numeric values.")
            self._pt1 = Point2D(point[0], point[1])
        else:
            raise TypeError("Start point must be a Point2D instance or a tuple/list of two coordinates.")
    
    @property
    def ep(self) -> Point2D:
        """Get the end point of the line."""
        if not isinstance(self._pt2, Point2D):
            raise TypeError("End point must be a Point2D instance.")
        return self._pt2
    @ep.setter
    def ep(self, point):
        """Set the end point of the line."""
        if isinstance(point, Point2D):
            self._pt2 = point
        elif isinstance(point, (tuple | list)) and len(point) == 2:
            if not all(isinstance(coord, (int, float)) for coord in point):
                raise TypeError("Coordinates must be numeric values.")
            self._pt2 = Point2D(point[0], point[1])
        else:
            raise TypeError("End point must be a Point2D instance or a tuple/list of two coordinates.")
    @property
    def points(self) -> tuple[Point2D, Point2D]:
        """Get the start and end points of the line."""
        if not all(isinstance(pt, Point2D) for pt in (self._pt1, self._pt2)):
            raise TypeError("Both points must be Point2D instances.")
        return self._pt1, self._pt2
    
    @points.setter
    def points(self, pts: tuple[Point2D, Point2D]) -> None:
        """Set the start and end points of the line."""
        if not isinstance(pts, tuple) or len(pts) != 2:
            raise TypeError("Points must be a tuple of two Point2D instances.")
        if not all(isinstance(pt, Point2D) for pt in pts):
            raise TypeError("Both points must be Point2D instances.")
        self._pt1 = pts[0]
        self._pt2 = pts[1]
    
    @property
    def sp_x(self) -> int | float:
        """Get the x-coordinate of the start point."""
        if not isinstance(self._pt1, Point2D):
            raise TypeError("Start point must be a Point2D instance.")
        return self._pt1.x
    @sp_x.setter
    def sp_x(self, x: int | float) -> None:
        """Set the x-coordinate of the start point."""
        if not isinstance(x, (int, float)):
            raise TypeError("X-coordinate must be a numeric value.")
        if not isinstance(self._pt1, Point2D):
            raise TypeError("Start point must be a Point2D instance.")
        self._pt1.x = x
    @property
    def sp_y(self) -> int | float:
        """Get the y-coordinate of the start point."""
        if not isinstance(self._pt1, Point2D):
            raise TypeError("Start point must be a Point2D instance.")
        return self._pt1.y
    @sp_y.setter
    def sp_y(self, y: int | float) -> None:
        """Set the y-coordinate of the start point."""
        if not isinstance(y, (int, float)):
            raise TypeError("Y-coordinate must be a numeric value.")
        if not isinstance(self._pt1, Point2D):
            raise TypeError("Start point must be a Point2D instance.")
        self._pt1.y = y
    @property
    def ep_x(self) -> int | float | None:
        """Get the x-coordinate of the end point."""
        if not isinstance(self._pt2, Point2D):
            raise TypeError("End point must be a Point2D instance.")
        return self._pt2.x
    @ep_x.setter
    def ep_x(self, x: int | float) -> None:
        """Set the x-coordinate of the end point."""
        if not isinstance(x, (int, float)):
            raise TypeError("X-coordinate must be a numeric value.")
        if not isinstance(self._pt2, Point2D):
            self._pt2 = Point2D()
        self._pt2.x = x

    @property
    def ep_y(self) -> int | float | None:
        """Get the y-coordinate of the end point."""
        if not isinstance(self._pt2, Point2D):
            raise TypeError("End point must be a Point2D instance.")
        return self._pt2.y
    @ep_y.setter
    def ep_y(self, y: int | float) -> None:
        """Set the y-coordinate of the end point."""
        if not isinstance(y, (int, float)):
            raise TypeError("Y-coordinate must be a numeric value.")
        if not isinstance(self._pt2, Point2D):
            self._pt2 = Point2D()
        self._pt2.y = y

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, Line2D):
            return NotImplemented
        return (self._pt1 == other._pt1 and self._pt2 == other._pt2) or \
               (self._pt1 == other._pt2 and self._pt2 == other._pt1)

    def __ne__(self, other: Self) -> bool:
        if not isinstance(other, Line2D):
            return NotImplemented
        return not self.__eq__(other)

    def __cmp__(self, other: Self) -> int:
        """Compare two lines based on their start and end points."""
        if not isinstance(other, Line2D):
            return NotImplemented
        if self == other:
            return 0
        if self._pt1 < other._pt1 or (self._pt1 == other._pt1 and self._pt2 < other._pt2):
            return -1
        return 1

    def __hash__(self) -> int:
        """Return a hash value for the line."""
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        return hash((self._pt1, self._pt2))
    
    def set_line(self, x1: int | float, y1: int | float, x2: int | float, y2: int | float) -> Self:
        """Set the line using coordinates."""
        if not all(isinstance(coord, (int, float)) for coord in (x1, y1, x2, y2)):
            raise TypeError("Coordinates must be numeric values.")
        self._pt1 = Point2D(x1, y1)
        self._pt2 = Point2D(x2, y2)
        return self
    
    def dx(self) -> int | float:
        """Get the x-coordinate difference between the start and end points."""
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        return self._pt2.x - self._pt1.x
    def dy(self) -> int | float:
        """Get the y-coordinate difference between the start and end points."""
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        return self._pt2.y - self._pt1.y
    
    def slope(self) -> float:
        """Calculate the slope of the line."""
        if self.dx() == 0:
            raise ZeroDivisionError("Slope is undefined for vertical lines.")
        return self.dy() / self.dx()
    
    def normal_vector(self) -> Self:
        """Get the normal vector of the line."""
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        if self.dx() == 0 and self.dy() == 0:
            raise ValueError("Normal vector cannot be zero.")
        normal_vector = Line2D(self._pt1, Point2D(self._pt1.x - self.dy(), self._pt1.y + self.dx()))
        if not isinstance(normal_vector, Line2D):
            raise TypeError("Normal vector must be a Line2D instance.")
        return normal_vector

    def unit_vector(self) -> Self:
        """Get the unit vector of the line."""
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        if self.length() == 0:
            raise ValueError("Cannot calculate unit vector for a zero-length line.")
        if self.dx() == 0 and self.dy() == 0:
            raise ValueError("Unit vector cannot be zero.")
        unit_vector = Line2D(self._pt1, Point2D(self._pt1.x + self.dx() / self.length(), self._pt1.y + self.dy() / self.length()))
        if not isinstance(unit_vector, Line2D):
            raise TypeError("Unit vector must be a Line2D instance.")
        if fabs(unit_vector.dx()) < 1e-9 and fabs(unit_vector.dy()) < 1e-9:
            raise ValueError("Unit vector cannot be zero.")
        return unit_vector

    def length(self) -> float:
        """Calculate the length of the line."""
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        return sqrt(self.dx() * self.dx() + self.dy() * self.dy())
    def set_length(self, length: float) -> Self:
        """Set the length of the line."""
        if length < 0:
           raise ValueError("Length cannot be negative.")
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        if not isinstance(length, (int, float)):
            raise TypeError("Length must be a numeric value.")
        if self.length() == 0:
            raise ValueError("Cannot set length for a zero-length line.")
        unit_vector = self.unit_vector()
        if not isinstance(unit_vector, Line2D):
            raise TypeError("Unit vector must be a Line2D instance.")
        self._pt2 = Point2D(self._pt1.x + unit_vector.dx() * length, self._pt1.y + unit_vector.dy() * length)
        return self
    """
    def angle(self) -> float:
        # Calculate the angle of the line in radians.
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        #if self.dx() == 0:
        #    raise ZeroDivisionError("Slope is undefined for vertical lines.")
        angle_rad = atan2(-self.dy(), self.dx()) # -self.dy() to match the coordinate system where y increases upwards
        # Normalize angle to be in the range [0, 2*pi)
        return angle_rad if angle_rad >= 0 else angle_rad + 2 * pi
    """
    def angle(self) -> float:
        """
        Calculate the angle of the line in radians.
        Angles increase counterclockwise, with 0 corresponding to the positive x-axis.
        Returns angle in the range [0, 2π).
        """
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
            
        # atan2 naturally gives angles increasing counterclockwise with 0 at positive x-axis
        angle_rad = atan2(self.dy(), self.dx())
        # Normalize to [0, 2π)
        if angle_rad < 0:
            angle_rad += 2 * pi
        elif angle_rad >= 2 * pi:
            angle_rad -= 2 * pi
        return angle_rad

    def angle_deg(self) -> float:
        """Calculate the angle of the line in degrees."""
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        return degrees(self.angle())
   
    def set_angle(self, angle: float) -> Self:
        """
        Set the angle of the line in radians.
        
        Angles increase counterclockwise, with 0 corresponding to the positive x-axis.
        Preserves the line length.
        
        Args:
            angle: The new angle in degrees
            
        Returns:
            Self for method chaining
        """
        if not isinstance(angle, (int, float)):
            raise TypeError("Angle must be a numeric value.")
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        if self.length() == 0:
            raise ValueError("Cannot set angle for a zero-length line.")
        if angle < 0:
            angle += 2 * pi
        elif angle >= 2 * pi:
            angle -= 2 * pi
        # Convert angle to radians
        length = self.length()
        self._pt2.x = self._pt1.x + length * cos(angle)
        self._pt2.y = self._pt1.y + length * sin(angle)
        return self

    def set_angle_deg(self, angle: float) -> Self:
        """Set the angle of the line in degrees."""
        if not isinstance(angle, (int, float)):
            raise TypeError("Angle must be a numeric value.")
        if angle < 0:
            angle += 360
        elif angle >= 360:
            angle -= 360
        return self.set_angle(radians(angle))

    def angle_to_line(self, other: Self) -> tuple[float, bool]:
        """Calculate the angle between this line and another line in radians."""
        if not isinstance(other, Line2D):
            raise TypeError("Argument must be a Line2D instance.")
        is_clockwise = False
        if self._pt1 is None or self._pt2 is None or other._pt1 is None or other._pt2 is None:
            raise ValueError("Start or end point is not defined for one of the lines.")
        angle_diff =  other.angle() - self.angle()
        if angle_diff > 0:
            is_clockwise = False
            #angle_diff += 2 * pi
        elif angle_diff <= 0:
            is_clockwise = True
            #angle_diff += 2 * pi
        return fabs(angle_diff), is_clockwise

    def angle_to_line_deg(self, other: Self) -> float:
        """Calculate the angle between this line and another line in degrees."""
        if not isinstance(other, Line2D):
            raise TypeError("Argument must be a Line2D instance.")
        return degrees(self.angle_to_line(other))
    def is_vertical(self) -> bool:
        """Check if the line is vertical."""
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        return self.dx() == 0
    def is_horizontal(self) -> bool:
        """Check if the line is horizontal."""
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        return self.dy() == 0
    
    def get_polar_coordinates(self) -> tuple[float, float]:
        """Get the polar coordinates of the line."""
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        return self.length(), self.angle_deg()
    
    def set_polar_(self, length: float, angle: float) -> Self:
        """Set the polar coordinates of the line."""
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        if not isinstance(length, (int, float)) or not isinstance(angle, (int, float)):
            raise TypeError("Length and angle must be numeric values.")
        if length < 0:
            raise ValueError("Length cannot be negative.")
        self._pt2 = Point2D(self._pt1.x + length * cos(angle), self._pt1.y + length * sin(angle))
        return self
        
    def set_polar_deg(self, length: float, angle: float) -> Self:
        """Set the line using polar coordinates (degrees)."""
        if not isinstance(pt1, Point2D) or not isinstance(pt2, Point2D):
            raise TypeError("Points must be Point2D instances.")
        if not isinstance(length, (int, float)) or not isinstance(angle, (int, float)):
            raise TypeError("Length and angle must be numeric values.")
        if length < 0:
            raise ValueError("Length cannot be negative.")
        angle_rad = radians(angle)
        self.set_polar_(length, angle_rad)
        return self

    def set_cartesian_coordinates(self, x: int | float, y: int | float) -> Self:
        """Set the line using Cartesian coordinates."""
        if not all(isinstance(coord, (int, float)) for coord in (x, y)):
            raise TypeError("Coordinates must be numeric values.")
        dx = x - self._pt1.x
        dy = y - self._pt1.y
        self._pt2 = Point2D(self._pt1.x + dx, self._pt1.y + dy)
        return self
    
    def reverse(self) -> Self:
        """Reverse the direction of the line."""
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        self._pt1, self._pt2 = self._pt2, self._pt1
        return self
    def is_valid(self) -> bool:
        """Check if the line is valid (both points are defined)."""
        return self._pt1 is not None and self._pt2 is not None
    def is_null(self) -> bool:
        """Check if the line is null (both points are the same)."""
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        return self._pt1 == self._pt2
    def translate_pt(self, pt: Self) -> None:
        """Translate the line by a point."""
        if not isinstance(pt, Point2D):
            raise TypeError("Argument must be a Point2D instance.")
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        self._pt1 += pt
        self._pt2 += pt
    
    def translate_dxdy(self, dx: int | float, dy: int | float) -> None:
        """Translate the line by dx and dy."""
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise TypeError("Translation values must be numeric.")
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        self.translate_pt(Point2D(dx, dy))
    
    def rotate(self, angle: float) -> None:
        """
        Rotate the line around its start point by a given angle in degrees.
        Positive angles rotate counterclockwise.
        Args:
            angle: Rotation angle in degrees (counterclockwise)
        """
        if not isinstance(angle, (int, float)):
            raise TypeError("Angle must be a numeric value.")
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        
        # Convert to radians for counterclockwise rotation
        angle_rad = radians(angle)
        cos_angle = cos(angle_rad)
        sin_angle = sin(angle_rad)
        
        # Translate end point to origin
        translated_x = self.dx()
        translated_y = self.dy()

        # Rotate around origin (counterclockwise)
        rotated_x = translated_x * cos_angle - translated_y * sin_angle
        rotated_y = translated_x * sin_angle + translated_y * cos_angle
        
        # Translate back to original position
        self._pt2.x = self._pt1.x + rotated_x
        self._pt2.y = self._pt1.y + rotated_y
    
    def interpolate(self, t: float) -> Point2D:
        """Interpolate a point on the line at parameter t (0 <= t <= 1)."""
        if not isinstance(t, (int, float)):
            raise TypeError("Parameter t must be a numeric value.")
        if not (0 <= t <= 1):
            raise ValueError("Parameter t must be in the range [0, 1].")
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        x = self._pt1.x + t * self.dx()
        y = self._pt1.y + t * self.dy()
        return Point2D(x, y)

    def point_at_length(self, length: float) -> Point2D:
        """Get a point on the line at a specific length from the start point."""
        if not isinstance(length, (int, float)):
            raise TypeError("Length must be a numeric value.")
        if length < 0:
            raise ValueError("Length cannot be negative.")
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        if self.length() == 0:
            raise ValueError("Cannot get point at length for a zero-length line.")
        unit_vector = self.unit_vector()
        return Point2D(self._pt1.x + unit_vector.dx() * length, self._pt1.y + unit_vector.dy() * length)
    
    def distance_to_point(self, pt: Point2D) -> float:
        """Calculate the distance from a point to the line."""
        if not isinstance(pt, Point2D):
            raise TypeError("Argument must be a Point2D instance.")
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        # Using the formula for distance from a point to a line segment
        num = abs(self.dy() * pt.x - self.dx() * pt.y + self._pt2.x * self._pt1.y - self._pt2.y * self._pt1.x)
        denom = sqrt(self.dy() * self.dy() + self.dx() * self.dx())
        return num / denom if denom != 0 else float('inf')
    
    def is_point_on_line(self, pt: Point2D) -> bool:
        """Check if a point lies on the line."""
        if not isinstance(pt, Point2D):
            raise TypeError("Argument must be a Point2D instance.")
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        # Check if the point is within the bounding box of the line segment
        return (min(self._pt1.x, self._pt2.x) <= pt.x <= max(self._pt1.x, self._pt2.x) and
                min(self._pt1.y, self._pt2.y) <= pt.y <= max(self._pt1.y, self._pt2.y) and
                abs(self.distance_to_point(pt)) < 1e-9)
    
    def is_parallel(self, other: Self) -> bool:
        """Check if this line is parallel to another line."""
        if not isinstance(other, Line2D):
            raise TypeError("Argument must be a Line2D instance.")
        if self._pt1 is None or self._pt2 is None or other._pt1 is None or other._pt2 is None:
            raise ValueError("Start or end point is not defined for one of the lines.")
        return fabs(self.slope() - other.slope()) < 1e-9
    
    def is_perpendicular(self, other: Self) -> bool:
        """Check if this line is perpendicular to another line."""
        if not isinstance(other, Line2D):
            raise TypeError("Argument must be a Line2D instance.")
        if self._pt1 is None or self._pt2 is None or other._pt1 is None or other._pt2 is None:
            raise ValueError("Start or end point is not defined for one of the lines.")
        return fabs(self.slope() * other.slope() + 1) < 1e-9
    
    def coefficients(self) -> tuple[float, float, float]:
        """Get the coefficients of the line in the form Ax + By + C = 0."""
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        A = self.dy()
        B = -self.dx()
        C = -(A * self._pt1.x + B * self._pt1.y)
        return A, B, C
    
    def evaluate(self, *points: Point2D) -> int | float | None:
        """Evaluate the line at a given x-coordinate."""
        if not self.is_valid_line():
            raise ValueError("Line is not valid (degenerate or points not defined).")
        if len(points) == 0:
            return None
        elif len(points) == 1:
            if not isinstance(points[0], Point2D):
                raise TypeError("Argument must be a Point2D instance.")
            a, b, c = self.coefficients()
            return -(a * points[0].x + b * points[0].y + c) / b if b != 0 else None
        elif len(points) == 2:
            if not all(isinstance(pt, (int, float)) for pt in points):
                    raise TypeError("Both arguments must be numeric.")
            a, b, c = self.coefficients()
            return -(a * points[0].x + b * points[0].y + c) / b if b != 0 else None
        
    def evaluate_y(self, x: int | float) -> int | float | None:
        """Evaluate the line at a given x-coordinate."""
        if not self.is_valid_line():
            raise ValueError("Line is not valid (degenerate or points not defined).")
        if not isinstance(x, (int, float)):
            raise TypeError("Argument must be a numeric value.")
        a, b, c = self.coefficients()
        return -(a * x + c) / b if b != 0 else None

    def evaluate_x(self, y: int | float) -> int | float | None:
        """Evaluate the line at a given y-coordinate."""
        if not self.is_valid_line():
            raise ValueError("Line is not valid (degenerate or points not defined).")
        if not isinstance(y, (int, float)):
            raise TypeError("Argument must be a numeric value.")
        a, b, c = self.coefficients()
        return -(b * y + c) / a if a != 0 else None

    def is_degenerate(self) -> bool:
        """Check if the line is degenerate (both points are the same)."""
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        a, b, c = self.coefficients()
        return a == 0 and b == 0
    
    def is_valid_line(self) -> bool:
        """Check if the line is valid (not degenerate and both points are defined)."""
        if self._pt1 is None or self._pt2 is None:
            return False
        return not self.is_degenerate()
    def intersection_with(self, other: Self) -> tuple[bool, Point2D]:
        """Check if this line intersects with another line."""
        if not isinstance(other, Line2D):
            raise TypeError("Argument must be a Line2D instance.")
        if self._pt1 is None or self._pt2 is None or other._pt1 is None or other._pt2 is None:
            raise ValueError("Start or end point is not defined for one of the lines.")
        if self.is_degenerate() or other.is_degenerate():
            return False, Point2D(0, 0) # Degenerate lines cannot intersect meaningfully
        # Check if the lines are parallel
        #if self.is_parallel(other):
        #    return False, Point2D(0, 0) # Lines are parallel, no intersection
        
        # Calculate intersection point using line equations
        A1, B1, C1 = self.coefficients()
        A2, B2, C2 = other.coefficients()
        
        det = A1 * B2 - A2 * B1
        if det == 0:
            return False, Point2D(0, 0)  # Lines are parallel or coincident
        x = (B1 * C2 - B2 * C1) / det
        y = (A2 * C1 - A1 * C2) / det
        return True, Point2D(x, y)
    
    def intersection_with_line(self, other: Self) -> tuple[int, Point2D]:
        """
        Check if this line intersects with another line segment.
        
        Returns:
            tuple: (status, intersection_point) where status is:
                0 = no intersection (parallel or coincident)
                1 = intersection within both segments
                2 = intersection outside one or both segments
        """
        if not isinstance(other, Line2D):
            raise TypeError("Argument must be a Line2D instance.")
        if self._pt1 is None or self._pt2 is None or other._pt1 is None or other._pt2 is None:
            raise ValueError("Start or end point is not defined for one of the lines.")
        
        A = self._pt2 - self._pt1
        B = other._pt1 - other._pt2
        C = self._pt1 - other._pt1
        denominator = A.y * B.x - A.x * B.y
        
        # Check if lines are parallel or coincident
        if abs(denominator) < 1e-10:
            # Lines are parallel or coincident
            return 0, Point2D(0, 0)  # No intersection
        
        # Calculate intersection parameters
        reciprocal_denominator = 1 / denominator
        na = (B.y * C.x - B.x * C.y) * reciprocal_denominator
        nb = (A.x * C.y - A.y * C.x) * reciprocal_denominator
        
        # Calculate intersection point
        inter_point = self._pt1 + A * na
        
        # Check if intersection is within both segments
        if 0 <= na <= 1 and 0 <= nb <= 1:
            return 1, inter_point  # Intersection within both segments
        else:
            return 2, inter_point  # Intersection outside at least one segment

    def __repr__(self) -> str:
        """Return a string representation of the line."""
        return f"Line2D(%s %s)" % (repr(self._pt1), repr(self._pt2))

    def __str__(self) -> str:
        """Return a user-friendly string representation of the line."""
        return f"(x1: %g, y1: %g, x2: %g, y2: %g)"\
             % tuple(map(float, [self._pt1.x, self._pt1.y, self._pt2.x, self._pt2.y]))
    def to_string(self) -> str:
        """Return a string representation of the line."""
        return "(" + self._pt1.to_string() + ", " + self._pt2.to_string() + ")"
    def to_list(self) -> list[float]:
        """Return the line as a list of coordinates."""
        return [self._pt1.x, self._pt1.y, self._pt2.x, self._pt2.y]
    def to_tuple(self) -> tuple[float, float, float, float]:
        """Return the line as a tuple of coordinates."""
        return (self._pt1.x, self._pt1.y, self._pt2.x, self._pt2.y)
