from point2d.point2d import Point2D
from line2d.line2d import Line2D
from typing import Self, Union, Tuple, Optional
from math import pi, cos, sin, atan2, degrees, sqrt, radians

TOLERANCE_LENGTH = 1e-9
TOLERANCE_ANGLE = 1e-8

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
    def is_null(self) -> bool:
        """
        Checks if the arc is null (all points are at the origin).
        Returns:
            bool: True if the arc is null, False otherwise.
        """
        return self._pt1 == self._pt2
    def is_zero(self) -> bool:
        """
        Checks if the arc is zero (all points are at the origin).
        Returns:
            bool: True if the arc is zero, False otherwise.
        """
        return self._pt0 == Point2D(0, 0) and self._pt1 == Point2D(0, 0) and self._pt2 == Point2D(0, 0)
    def is_valid(self) -> bool:
        """
        Checks if the arc is valid (the start and end points are not the same).
        Returns:
            bool: True if the arc is valid, False otherwise.
        """
        return not self.is_null() and not self.is_zero()
    
    def is_clockwise(self) -> bool:
        """
        Checks if the arc is clockwise.
        Returns:
            bool: True if the arc is clockwise, False otherwise.
        """
        angle, is_clockwise = self.segment_cp_sp().angle_to_line(self.segment_cp_ep())
        return is_clockwise
        

    def is_counter_clockwise(self) -> bool:
        """
        Checks if the arc is counter-clockwise.
        Returns:
            bool: True if the arc is counter-clockwise, False otherwise.
        """
        return not self.is_clockwise()

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
    @property
    def points(self) -> Tuple[Point2D, Point2D, Point2D]:
        """
        Returns the start, center, and end points of the arc as a tuple.
        Returns:
            Tuple[Point2D, Point2D, Point2D]: The start, center, and end points.
        """
        return self._pt0, self._pt1, self._pt2
    @points.setter
    def points(self, points) -> None:
        """
        Sets the start, center, and end points of the arc.
        Parameters:
            pt0 (Point2D): The new center point.
            pt1 (Point2D): The new start point.
            pt2 (Point2D): The new end point.
        
        Raises:
            TypeError: If any of the points are not Point2D instances.
        """
        if len(points) == 0:
            self._pt0 = Point2D(0, 0)
            self._pt1 = Point2D(0, 0)
            self._pt2 = Point2D(0, 0)
        elif len(points) == 3:
            if all(isinstance(pt, Point2D) for pt in points):
                self._pt0, self._pt1, self._pt2 = points[0], points[1], points[2]
            elif all(isinstance(pt, (list, tuple)) for pt in points):
                if all(isinstance(coord, (int, float)) for pt in points for coord in pt):
                    self._pt0 = Point2D(points[0][0], points[0][1])
                    self._pt1 = Point2D(points[1][0], points[1][1])
                    self._pt2 = Point2D(points[2][0], points[2][1])
                else:
                    raise TypeError("Coordinates must be numeric values.")
        else:
            raise ValueError("Arc2D requires exactly three points (start, center and end points on the arc).")
    
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

    def arc_length(self) -> float:
        """
        Returns the length of the arc.
        Returns:
            float: The length of the arc.
        """
        radius = self.radius_cp_sp()
        angle, is_clockwise = self.segment_cp_sp().angle_to_line(self.segment_cp_ep())
        return radius * angle

    def arc_angle(self) -> float:
        """
        Returns the angle of the arc.
        Returns:
            float: The angle of the arc in radians.
        """
        angle, is_clockwise = self.segment_cp_sp().angle_to_line(self.segment_cp_ep())
        if angle < 0:
            angle += 2 * pi
        elif angle >= 2 * pi:
            angle -= 2 * pi
        return angle

    def arc_angle_deg(self) -> float:
        """
        Returns the angle of the arc in degrees.
        Returns:
            float: The angle of the arc in degrees.
        """
        return degrees(self.arc_angle())
    def point_at_angle(self, angle: float) -> Point2D:
        """
        Returns the point on the arc at a specific angle.
        Parameters:
            angle (float): The angle in radians.
        Returns:
            Point2D: The point on the arc at the specified angle.
        """
        if not (self.start_angle() <= angle <= self.end_angle()):
            raise ValueError("Angle is outside the arc's range.")
        x = self.cp.x + self.radius_cp_sp() * cos(angle)
        y = self.cp.y + self.radius_cp_sp() * sin(angle)
        return Point2D(x, y)
    def point_at_angle_deg(self, angle: float) -> Point2D:
        """
        Returns the point on the arc at a specific angle in degrees.
        Parameters:
            angle (float): The angle in degrees.
        Returns:
            Point2D: The point on the arc at the specified angle.
        """
        angle_rad = radians(angle)
        return self.point_at_angle(angle_rad)
    def point_at_midpoint(self) -> Point2D:
        """
        Returns the midpoint of the arc.
        Returns:
            Point2D: The midpoint of the arc.
        """
        angle, is_clockwise = self.segment_cp_sp().angle_to_line(self.segment_cp_ep())
        mid_angle = angle / 2
        return self.point_at_angle(mid_angle)
    def get_middle_point(self) -> Point2D:
        """
        Returns the middle point of the arc.
        Returns:
            Point2D: The middle point of the arc.
        """
        segment = self.segment_cp_sp()
        if segment.is_null():
            return self.cp
        segment.set_polar(segment.length(), segment.angle() + self.arc_angle() / 2)
        return segment.ep()

    def set_arc_angle(self, angle: float) -> None:
        """
        Sets the angle of the arc in radians.
        Parameters:
            angle (float): The new angle in radians.
        """
        if not isinstance(angle, (int, float)):
            raise TypeError("Angle must be a numeric value.")
        if angle < 0:
            angle += 2 * pi
        elif angle >= 2 * pi:
            angle -= 2 * pi
        arc_angle = self.angle_cp_sp() + angle
        self._pt2 = self.point_at_angle(arc_angle)

    def set_arc_angle_deg(self, angle: float) -> None:
        """
        Sets the angle of the arc in degrees.
        Parameters:
            angle (float): The new angle in degrees.
        """
        if not isinstance(angle, (int, float)):
            raise TypeError("Angle must be a numeric value.")
        angle_rad = radians(angle)
        self.set_arc_angle(angle_rad)
    @classmethod
    def create_from_cp_sp_ep(cls, center: Point2D, start: Point2D, end: Point2D) -> Self:
        """
        Creates an Arc2D object from center, start, and end points.
        Parameters:
            center (Point2D): The center point of the arc.
            start (Point2D): The start point of the arc.
            end (Point2D): The end point of the arc.
        Returns:
            Arc2D: A new Arc2D object.
        """
        return cls(center, start, end)
    @classmethod
    def create_from_sp_mp_ep(cls, start_pt: Point2D, mid_pt: Point2D, end_pt: Point2D) -> tuple[bool, Self]:
        """
        Creates an Arc2D object from start, midpoint, and end points.
        Parameters:
            start (Point2D): The start point of the arc.
            midpoint (Point2D): The midpoint of the arc.
            end (Point2D): The end point of the arc.
        Returns:
            Arc2D: A new Arc2D object.
        """
        if not isinstance(start_pt, Point2D) or not isinstance(mid_pt, Point2D) or not isinstance(end_pt, Point2D):
            raise TypeError("Start, midpoint, and end points must be Point2D instances.")
        if start_pt == mid_pt or mid_pt == end_pt or start_pt == end_pt:
            #raise ValueError("Start, midpoint, and end points must be distinct.")
            return False, None 
        if start_pt.distance_to(mid_pt) < TOLERANCE_LENGTH or\
             mid_pt.distance_to(end_pt) < TOLERANCE_LENGTH or\
           start_pt.distance_to(end_pt) < TOLERANCE_LENGTH:
            return False, None
        # Calculate the center point using the intersection of the normals at the midpoint
        mid_line_sp_mp = Line2D(start_pt.midpoint_to(mid_pt), start_pt)
        mid_line_mp_ep = Line2D(mid_pt.midpoint_to(end_pt), mid_pt)
        normal_sp_mp = mid_line_sp_mp.normal_vector()
        normal_mp_ep = mid_line_mp_ep.normal_vector()
        inter, center_pt = normal_sp_mp.intersection_with(normal_mp_ep)
        if inter is False or center_pt is None:
            return False, None
        if not isinstance(center_pt, Point2D):
            raise TypeError("Intersection point must be a Point2D instance.")
        if center_pt.distance_to(start_pt) < TOLERANCE_LENGTH or center_pt.distance_to(end_pt) < TOLERANCE_LENGTH:
            return False, None
        print(f"Center point: {center_pt}")
        return True, cls(center_pt, start_pt, end_pt)
    @classmethod
    def create_from_sp_ep_rd_cw(cls, start_pt: Point2D, end_pt: Point2D, radius: float, cw: bool) -> tuple[bool, Self | None]:
        """
        Creates an Arc2D object from two points, a radius, and a direction (clockwise or counter-clockwise).
        
        Parameters:
            start_pt (Point2D): The start point of the arc.
            end_pt (Point2D): The end point of the arc.
            radius (float): The radius of the arc.
            cw (bool): True for clockwise, False for counter-clockwise.
            
        Returns:
            tuple[bool, Arc2D]: A tuple containing a success flag and a new Arc2D object.
        """
        if not isinstance(start_pt, Point2D) or not isinstance(end_pt, Point2D):
            raise TypeError("Points must be Point2D instances.")
        if start_pt == end_pt:
            raise ValueError("Start and end points must be distinct.")
        if start_pt.distance_to(end_pt) < TOLERANCE_LENGTH:
            return False, None
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a numeric value.")
        # Check if radius is positive
        if radius <= 0:
            raise ValueError("Radius must be positive.")

        mid_point = start_pt.midpoint_to(end_pt)
        mid_to_start = Line2D(mid_point, start_pt)
        length = mid_to_start.length()
        
        # Check if radius is too small
        if length > radius:
            # Check if radius is too small - RAISE ValueError here instead of returning False
            raise ValueError(f"Points are too far apart ({length*2}) for the given radius ({radius})")
            #return False, cls()  # Changed from Arc2D() to cls()
            
        height = sqrt(pow(radius, 2) - pow(length, 2))
        
        # Get the endpoint of the normal vector after setting length
        normal_vec = mid_to_start.normal_vector()
        if normal_vec.is_null():
            # If the normal vector is null, the points are collinear or too close
            return False, None
        normal_vec.set_length(height)
        center_pt = normal_vec.ep
        
        arc2d = cls(center_pt, start_pt, end_pt)  # Changed from Arc2D() to cls()
        if cw == arc2d.is_clockwise():
            return True, arc2d
            
        mid_to_end = Line2D(mid_point, end_pt)
        normal_vec = mid_to_end.normal_vector()
        normal_vec.set_length(height)
        center_pt = normal_vec.ep
        
        arc2d = cls(center_pt, start_pt, end_pt)  # Changed from Arc2D() to cls()
        if cw == arc2d.is_clockwise():
            return True, arc2d
            
        return False, None  # Changed from Arc2D() to cls()
    @classmethod
    def create_from_cp_sp_aa_cw(cls, center_pt: Point2D, start_pt: Point2D, arc_angle: float, cw: bool = True) -> (bool, Self | None):
        """
        Creates an Arc2D object from a center point, a start point, and an angle, with a specified direction (clockwise or counter-clockwise).
        """
        if arc_angle <= 0:
            return False, None
        segment_cp_sp = Line2D(center_pt, start_pt)
        start_angle = segment_cp_sp.angle()
        segment_cp_ep = segment_cp_sp
        if cw:
            segment_cp_ep.set_angle(start_angle - arc_angle)
        else:
            segment_cp_ep.set_angle(start_angle + arc_angle)
        end_pt = segment_cp_ep.ep
        arc2d = cls(center_pt, start_pt, end_pt)
        return True, arc2d

    @classmethod
    def create_from_cp1_sp1_aa_ccw(cls, center_pt: Point2D, start_pt: Point2D, arc_angle: float, cw: bool = True) -> (bool, Self | None):
        """
        Creates an Arc2D object from a center point, a start point, and an angle, with a specified direction (clockwise or counter-clockwise).

        Parameters:
            center_pt (Point2D): The center point of the arc.
            start_pt (Point2D): The start point of the arc.
            arc_angle (float): The angle of the arc in radians.
            cw (bool): True for clockwise, False for counter-clockwise.

        Returns:
            tuple[bool, Arc2D]: A tuple containing a success flag and a new Arc2D object.
        """
        if not isinstance(center_pt, Point2D) or not isinstance(start_pt, Point2D):
            raise TypeError("Points must be Point2D instances.")
        if center_pt == start_pt:
            raise ValueError("Center and start points must be distinct.")
        if not isinstance(arc_angle, (int, float)):
            raise TypeError("Angle must be a numeric value.")
        if arc_angle <= 0:
            raise ValueError("Angle must be positive.")

        radius = center_pt.distance_to(start_pt)
        if radius <= 0:
            raise ValueError("Center and start points are too close to form an arc.")

        end_angle = center_pt.angle_to(start_pt) + arc_angle
        end_x = center_pt.x + radius * cos(end_angle)
        end_y = center_pt.y + radius * sin(end_angle)
        end_pt = Point2D(end_x, end_y)
        success, arc = cls.create_from_sp_ep_rd_cw(start_pt, end_pt, radius, cw)
        if not success:
            return False, None
        return success, arc
    @classmethod
    def create_from_cp_sp_aa(cls, center_pt: Point2D, start_pt: Point2D, aa: float, cw: bool = True) -> tuple[bool, Self | None]:
        """
        Creates an Arc2D object from a center point, a start point, an angle, and a direction (clockwise or counter-clockwise).

        Parameters:
            center_pt (Point2D): The center point of the arc.
            start_pt (Point2D): The start point of the arc.
            aa (float): The angle of the arc in radians.
            cw (bool): True for clockwise, False for counter-clockwise.

        Returns:
            tuple[bool, Arc2D]: A tuple containing a success flag and a new Arc2D object.
        """
        if not isinstance(center_pt, Point2D) or not isinstance(start_pt, Point2D):
            raise TypeError("Points must be Point2D instances.")
        if center_pt == start_pt:
            raise ValueError("Center and start points must be distinct.")
        if not isinstance(aa, (int, float)):
            raise TypeError("Angle must be a numeric value.")
        if aa <= 0:
            raise ValueError("Angle must be positive.")

        radius = center_pt.distance_to(start_pt)
        if radius <= 0:
            raise ValueError("Center and start points are too close to form an arc.")

        end_angle = start_pt.angle_to(center_pt) + aa
        end_x = center_pt.x + radius * cos(end_angle)
        end_y = center_pt.y + radius * sin(end_angle)
        end_pt = Point2D(end_x, end_y)
        success, arc = cls.create_from_sp_ep_rd_cw(start_pt, end_pt, radius, cw)
        if not success:
            return False, None
        return success, arc

    @classmethod
    def create_from_sp_ep_aa(cls, start_pt: Point2D, end_pt: Point2D, aa: float, cw: bool = True) -> tuple[bool, Self | None]:
        """
        Creates an Arc2D object from two points, an angle, and a direction (clockwise or counter-clockwise).

        Parameters:
            start_pt (Point2D): The start point of the arc.
            end_pt (Point2D): The end point of the arc.
            aa (float): The angle of the arc in radians.
            cw (bool): True for clockwise, False for counter-clockwise.

        Returns:
            tuple[bool, Arc2D]: A tuple containing a success flag and a new Arc2D object.
        """
        if not isinstance(start_pt, Point2D) or not isinstance(end_pt, Point2D):
            raise TypeError("Points must be Point2D instances.")
        if start_pt == end_pt:
            raise ValueError("Start and end points must be distinct.")
        if start_pt.distance_to(end_pt) < TOLERANCE_LENGTH:
            return False, None
        if not isinstance(aa, (int, float)):
            raise TypeError("Angle must be a numeric value.")
        if aa <= 0:
            raise ValueError("Angle must be positive.")

        mid_point = start_pt.midpoint_to(end_pt)
        mid_to_start = Line2D(mid_point, start_pt)
        length = mid_to_start.length()

        # Check if radius is too small
        radius = length / sin(aa / 2)
        if radius <= 0:
            raise ValueError(f"Points are too far apart ({length*2}) for the given angle ({aa})")
        success, arc = Arc2D.create_from_sp_ep_rd_cw(start_pt, end_pt, radius, cw)
        if not success:
            return False, None
        return success, arc


    @classmethod
    def create_from_sp1_ep1_rd_cw(cls, start_pt: Point2D, end_pt: Point2D, radius: float, cw: bool) -> tuple[bool, Self]:
        """
        Creates an Arc2D object from two points, a radius, and a direction (clockwise or counter-clockwise).
        
        Parameters:
            start_pt (Point2D): The start point of the arc.
            end_pt (Point2D): The end point of the arc.
            radius (float): The radius of the arc.
            cw (bool): True for clockwise, False for counter-clockwise.
            
        Returns:
            tuple[bool, Arc2D]: A tuple containing a success flag and a new Arc2D object.
        """
        if not isinstance(start_pt, Point2D) or not isinstance(end_pt, Point2D):
            raise TypeError("Points must be Point2D instances.")
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a numeric value.")
        if radius <= 0:
            raise ValueError("Radius must be positive.")

        # Calculate chord length between start and end points
        chord_length = start_pt.distance_to(end_pt)
        
        # Check if radius is large enough for the arc to exist
        if chord_length / 2 > radius:
            raise ValueError(f"Points are too far apart ({chord_length}) for the given radius ({radius})")
        
        # Find midpoint of chord
        mid_point = Point2D((start_pt.x + end_pt.x) / 2, (start_pt.y + end_pt.y) / 2)
        
        # Calculate height of perpendicular from midpoint to arc center
        height = sqrt(radius**2 - (chord_length/2)**2)
        
        # Create perpendicular line from midpoint
        perp_line = Line2D(start_pt, end_pt).normal_vector()
        perp_line.sp = mid_point
        perp_line.set_length(height)
        
        # Try first potential center
        center_pt1 = perp_line.ep
        arc1 = cls(center_pt1, start_pt, end_pt)
        
        # Check if this matches the desired direction
        if cw == arc1.is_clockwise():
            return True, arc1
        
        # Try opposite direction for center
        perp_line.set_angle_deg(perp_line.angle_deg() + 180)
        perp_line.set_length(height)
        center_pt2 = perp_line.ep
        
        arc2 = cls(center_pt2, start_pt, end_pt)
        
        # Check if this matches the desired direction
        if cw == arc2.is_clockwise():
            return True, arc2
        
        # If we get here, something is wrong with our calculation or is_clockwise check
        # This should never happen, but as a fallback:
        return False, cls()

    def __repr__(self) -> str:
        return f"Arc2D(start={self.sp}, center={self.cp}, end={self.ep})"
    def length(self) -> float:
        # Calculate the length of the arc.
        return abs(self.end_angle - self.start_angle) * self.radius
    """
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
    """