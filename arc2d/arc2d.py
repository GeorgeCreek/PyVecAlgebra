from point2d.point2d import Point2D
from line2d.line2d import Line2D
from typing import Self, Union, Tuple, Optional

class Arc2D:
    def __init__(self, *points):
        """
        Initializes an Arc2D object with three points: start, center, and end.

        Parameters:
            *points: Variable length argument list. Accepts:
                - No arguments: Initializes all points to (0, 0).
                - Three Point2D instances.
                - Three lists or tuples, each representing (x, y) coordinates.

        Raises:
            TypeError: If the provided points are not all Point2D instances, lists, or tuples.
            ValueError: If the number of points provided is not exactly three.
        """
        if len(points) == 0:
            self._pt0 = Point2D(0, 0)
            self._pt1 = Point2D(0, 0)
            self._pt2 = Point2D(0, 0)
        elif len(points) == 3:
            if all(isinstance(pt, Point2D) for pt in points):
                self._pt0, self._pt1, self._pt2 = points[0], points[1], points[2]
            elif all(isinstance(pt, list) for pt in points):
                self._pt0 = Point2D(points[0][0], points[0][1])
                self._pt1 = Point2D(points[1][0], points[1][1])
                self._pt2 = Point2D(points[2][0], points[2][1])
            elif all(isinstance(pt, tuple) for pt in points):
                self._pt0 = Point2D(points[0][0], points[0][1])
                self._pt1 = Point2D(points[1][0], points[1][1])
                self._pt2 = Point2D(points[2][0], points[2][1])
            else:
                raise TypeError("Points must be Point2D instances, lists, or tuples.")
        else:
            raise ValueError("Arc2D requires exactly three points (start, center and end points on the arc).")
    
    @property
    def sp(self):
        """Start point of the arc."""
        if not isinstance(self._pt1, Point2D):
            raise TypeError("Start point must be a Point2D instance.")
        return self._pt1
    
    @sp.setter
    def sp(self, point):
        """Set the start point of the arc."""
        if isinstance(point, Point2D):
            self._pt1 = point
        elif isinstance(point, (tuple | list)) and len(point) == 2:
            if not all(isinstance(coord, (int, float)) for coord in point):
                raise TypeError("Coordinates must be numeric values.")
            self._pt1 = Point2D(point[0], point[1])
        else:
            raise TypeError("Start point must be a Point2D instance or a tuple/list of two coordinates.")

    @property
    def cp(self, *points):
        """Center point of the arc."""
        if not isinstance(self._pt0, Point2D):
            raise TypeError("Center point must be a Point2D instance.")
        return self._pt0

    @cp.setter
    def cp(self, point):
        if isinstance(point, Point2D):
            self._pt0 = point
        elif isinstance(point, (tuple | list)) and len(point) == 2:
            if not all(isinstance(coord, (int, float)) for coord in point):
                raise TypeError("Coordinates must be numeric values.")
            self._pt0 = Point2D(point[0], point[1])
        else:
            raise TypeError("Center point must be a Point2D instance or a tuple/list of two coordinates.")

    @property
    def ep(self):
        """End point of the arc."""
        if not isinstance(self._pt2, Point2D):
            raise TypeError("End point must be a Point2D instance.")
        return self._pt2

    @ep.setter
    def ep(self, point):
        if isinstance(point, Point2D):
            self._pt2 = point
        elif isinstance(point, (tuple | list)) and len(point) == 2:
            if not all(isinstance(coord, (int, float)) for coord in point):
                raise TypeError("Coordinates must be numeric values.")
            self._pt2 = Point2D(point[0], point[1])
        else:
            raise TypeError("End point must be a Point2D instance or a tuple/list of two coordinates.")

    def get_points(self) -> Tuple[Point2D, Point2D, Point2D]:
        """
        Returns the start, center, and end points of the arc as a tuple.
        Returns:
            Tuple[Point2D, Point2D, Point2D]: The start, center, and end points.
        """
        return self._pt0, self._pt1, self._pt2
    def set_points(self, pt0: Point2D, pt1: Point2D, pt2: Point2D) -> None:
        """
        Sets the start, center, and end points of the arc.
        Parameters:
            pt0 (Point2D): The new center point.
            pt1 (Point2D): The new start point.
            pt2 (Point2D): The new end point.
        
        Raises:
            TypeError: If any of the points are not Point2D instances.
        """
        if not all(isinstance(pt, Point2D) for pt in (pt0, pt1, pt2)):
            raise TypeError("All points must be Point2D instances.")
        self._pt0 = pt0
        self._pt1 = pt1
        self._pt2 = pt2
    def segment_cp_sp(self) -> Line2D:
        """
        Returns the line segment from the center point to the start point.
        Returns:
            Line2D: A Line2D object representing the segment from center to start.
        """
        return Line2D(self._pt0, self._pt1)
    def segment_cp_ep(self) -> Line2D:
        """
        Returns the line segment from the center point to the end point.
        Returns:
            Line2D: A Line2D object representing the segment from center to end.
        """
        return Line2D(self._pt0, self._pt2)
    def segment_sp_ep(self) -> Line2D:
        """
        Returns the line segment from the start point to the end point.
        Returns:
            Line2D: A Line2D object representing the segment from start to end.
        """
        return Line2D(self._pt1, self._pt2)
    
    def radius_cp_sp(self) -> float:
        """
        Returns the radius of the arc, which is the distance from the center point to the start point.
        Returns:
            float: The radius of the arc.
        """
        return self.segment_cp_sp().length()
    def set_radius_cp_sp(self, radius: float) -> None:
        """
        Sets the radius of the arc, which is the distance from the center point to the start point.
        Parameters:
            radius (float): The new radius of the arc.
        """
        #self._pt1 = self._pt0 + (self._pt1 - self._pt0).normalized() * radius
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a numeric value.")
        self.segment_cp_sp().set_length(radius)
    def angle_cp_sp(self) -> float:
        """
        Returns the angle of the arc from the center point to the start point.
        Returns:
            float: The angle in radians.
        """
        return self.segment_cp_sp().angle()
    def set_angle_cp_sp(self, angle: float) -> None:
        """
        Sets the angle of the arc from the center point to the start point.
        Parameters:
            angle (float): The new angle in radians.
        """
        if not isinstance(angle, (int, float)):
            raise TypeError("Angle must be a numeric value.")
        self.segment_cp_sp().set_angle(angle)
    def radius_cp_ep(self) -> float:
        """
        Returns the radius of the arc, which is the distance from the center point to the end point.
        Returns:
            float: The radius of the arc.
        """
        return self.segment_cp_ep().length()
    
    def set_radius_cp_ep(self, radius: float) -> None:
        """
        Sets the radius of the arc, which is the distance from the center point to the end point.
        Parameters:
            radius (float): The new radius of the arc.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a numeric value.")
        self.segment_cp_ep().set_length(radius)
    def angle_cp_ep(self) -> float:
        """
        Returns the angle of the arc from the center point to the end point.
        Returns:
            float: The angle in radians.
        """
        return self.segment_cp_ep().angle()
    def set_angle_cp_ep(self, angle: float) -> None:
        """
        Sets the angle of the arc from the center point to the end point.
        Parameters:
            angle (float): The new angle in radians.
        """
        if not isinstance(angle, (int, float)):
            raise TypeError("Angle must be a numeric value.")
        self.segment_cp_ep().set_angle(angle)
    def start_angle(self) -> float:
        """
        Returns the angle of the arc at the start point.
        Returns:
            float: The angle in radians.
        """
        return self.angle_cp_sp()
    def end_angle(self) -> float:
        """
        Returns the angle of the arc at the end point.
        Returns:
            float: The angle in radians.
        """
        return self.angle_cp_ep()
        
    def distance_sp_ep(self) -> float:
        """
        Returns the distance between the start point and the end point.
        Returns:
            float: The distance between the start and end points.
        """
        return self.segment_sp_ep().length()

    
    
    def __repr__(self) -> str:
        return f"Arc2D(start={self.sp}, center={self.cp}, end={self.ep})"
    def length(self) -> float:
        # Calculate the length of the arc.
        return abs(self.end_angle - self.start_angle) * self.radius

    def point_at_angle(self, angle: float) -> Point2D:
        # Get the point on the arc at a specific angle.
        if not (self.start_angle <= angle <= self.end_angle):
            raise ValueError("Angle is outside the arc's range.")
        x = self.center.x + self.radius * cos(angle)
        y = self.center.y + self.radius * sin(angle)
        return Point2D(x, y)
    def contains_point(self, pt: Point2D) -> bool:
        # Check if a point is on the arc.
        if not isinstance(pt, Point2D):
            raise TypeError("Point must be a Point2D instance.")
        angle = atan2(pt.y - self.center.y, pt.x - self.center.x)
        return self.start_angle <= angle <= self.end_angle and \
               sqrt((pt.x - self.center.x) ** 2 + (pt.y - self.center.y) ** 2) == self.radius