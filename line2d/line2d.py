from point2d.point2d import Point2D
from typing import Self
try:
    from .version import __version__
except ImportError:
    __version__ = "unknown"
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
    def get_sp(self) -> Point2D:
        """Get the start point of the line."""
        if self._pt1 is None:
            raise ValueError("Start point is not defined.")
        if not isinstance(self._pt1, Point2D):
            raise TypeError("Start point must be a Point2D instance.")
        return self._pt1
    
    def set_sp(self, pt: Point2D) -> None:
        """Set the start point of the line."""
        if self._pt1 is None:
            self._pt1 = Point2D()
        if not isinstance(pt, Point2D):
            raise TypeError("Start point must be a Point2D instance.")
        self._pt1 = pt
    sp = property(get_sp, set_sp, doc="Start point of the line.")
   
    def get_ep(self) -> Point2D:
        """Get the end point of the line."""
        if self._pt2 is None:
            raise ValueError("End point is not defined.")
        if not isinstance(self._pt2, Point2D):
            raise TypeError("End point must be a Point2D instance.")
        return self._pt2
    def set_ep(self, pt: Point2D) -> None:
        """Set the end point of the line."""
        if self._pt2 is None:
            self._pt2 = Point2D()
        if not isinstance(pt, Point2D):
            raise TypeError("End point must be a Point2D instance.")
        self._pt2 = pt
    ep = property(get_ep, set_ep, doc="End point of the line.")
    def get_points(self) -> tuple[Point2D, Point2D]:
        """Get the start and end points of the line."""
        if self._pt1 is None or self._pt2 is None:
            raise ValueError("Start or end point is not defined.")
        return self._pt1, self._pt2

    def set_points(self, pt1: Point2D, pt2: Point2D) -> None:
        """Set the start and end points of the line."""
        if not isinstance(pt1, Point2D) or not isinstance(pt2, Point2D):
            raise TypeError("Both points must be Point2D instances.")
        self._pt1 = pt1
        self._pt2 = pt2
    # points = property(get_points, set_points, doc="Start and end points of the line.")
    def get_sp_x(self) -> int | float | None:
        """Get the x-coordinate of the start point."""
        if self._pt1 is None:
            raise ValueError("Start point is not defined.")
        if not isinstance(self._pt1, Point2D):
            return None
        return self._pt1.x
    
    def set_sp_x(self, x: int | float) -> None:
        """Set the x-coordinate of the start point."""
        if self._pt1 is None:
            self._pt1 = Point2D()
        if not isinstance(self._pt1, Point2D):
            raise TypeError("Start point must be a Point2D instance.")
        self._pt1.x = x
    sp_x = property(get_sp_x, set_sp_x, doc="X-coordinate of the start point.")
    def get_sp_y(self) -> int | float | None:
        """Get the y-coordinate of the start point."""
        if self._pt1 is None:
            raise ValueError("Start point is not defined.")
        if not isinstance(self._pt1, Point2D):
            return None
        return self._pt1.y
    def set_sp_y(self, y: int | float) -> None:
        """Set the y-coordinate of the start point."""
        if self._pt1 is None:
            self._pt1 = Point2D()
        if not isinstance(self._pt1, Point2D):
            raise TypeError("Start point must be a Point2D instance.")
        self._pt1.y = y
    sp_y = property(get_sp_y, set_sp_y, doc="Y-coordinate of the start point.")
    def get_ep_x(self) -> int | float | None:
        """Get the x-coordinate of the end point."""
        if self._pt2 is None:
            raise ValueError("End point is not defined.")
        if not isinstance(self._pt2, Point2D):
            return None
        return self._pt2.x
    
    def set_ep_x(self, x: int | float) -> None:
        """Set the x-coordinate of the end point."""
        if self._pt2 is None:
            self._pt2 = Point2D()
        if not isinstance(self._pt2, Point2D):
            raise TypeError("End point must be a Point2D instance.")
        self._pt2.x = x
    ep_x = property(get_ep_x, set_ep_x, doc="X-coordinate of the end point.")
    def get_ep_y(self) -> int | float | None:
        """Get the y-coordinate of the end point."""
        if self._pt2 is None:
            raise ValueError("End point is not defined.")
        if not isinstance(self._pt2, Point2D):
            return None
        return self._pt2.y
    
    def set_ep_y(self, y: int | float) -> None:
        """Set the y-coordinate of the end point."""
        if self._pt2 is None:
            self._pt2 = Point2D()
        if not isinstance(self._pt2, Point2D):
            raise TypeError("End point must be a Point2D instance.")
        self._pt2.y = y
    ep_y = property(get_ep_y, set_ep_y, doc="Y-coordinate of the end point.")
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Line2D):
            return NotImplemented
        return (self._pt1 == other._pt1 and self._pt2 == other._pt2) or \
               (self._pt1 == other._pt2 and self._pt2 == other._pt1)

    def __repr__(self):
        return f"Line2D({self._pt1}, {self._pt2})"
