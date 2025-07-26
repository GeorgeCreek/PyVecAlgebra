import unittest
from line2d.line2d import Line2D
from point2d.point2d import Point2D
from math import pi, sqrt, atan2, degrees

class TestLine2D(unittest.TestCase):

    def test_default_constructor(self):
        line = Line2D()
        self.assertIsInstance(line._pt1, Point2D)
        self.assertIsInstance(line._pt2, Point2D)

    def test_copy_constructor(self):
        pt1 = Point2D(1, 2)
        pt2 = Point2D(3, 4)
        original = Line2D(pt1, pt2)
        copy = Line2D(original)
        self.assertEqual(copy._pt1, pt1)
        self.assertEqual(copy._pt2, pt2)

    def test_constructor_with_two_points(self):
        pt1 = Point2D(5, 6)
        pt2 = Point2D(7, 8)
        line = Line2D(pt1, pt2)
        self.assertEqual(line._pt1, pt1)
        self.assertEqual(line._pt2, pt2)

    def test_constructor_with_four_numbers(self):
        line = Line2D(1, 2, 3, 4)
        self.assertEqual(line._pt1, Point2D(1, 2))
        self.assertEqual(line._pt2, Point2D(3, 4))

    def test_constructor_invalid_one_arg(self):
        with self.assertRaises(TypeError):
            Line2D(123)

    def test_constructor_invalid_two_args(self):
        with self.assertRaises(TypeError):
            Line2D(Point2D(1, 2), 5)

    def test_constructor_invalid_four_args(self):
        with self.assertRaises(TypeError):
            Line2D(1, 2, "a", 4)

    def test_constructor_too_many_args(self):
        with self.assertRaises(ValueError):
            Line2D(1, 2, 3, 4, 5)

    def test_equality(self):
        l1 = Line2D(Point2D(0, 0), Point2D(1, 1))
        l2 = Line2D(Point2D(0, 0), Point2D(1, 1))
        l3 = Line2D(Point2D(1, 1), Point2D(0, 0))
        l4 = Line2D(Point2D(1, 1), Point2D(2, 2))
        self.assertTrue(l1 == l2)
        self.assertTrue(l1 == l3)
        self.assertFalse(l1 == l4)

    

    def test_dx_and_dy(self):
        line = Line2D(Point2D(1, 2), Point2D(4, 6))
        self.assertEqual(line.dx(), 3)
        self.assertEqual(line.dy(), 4)

    def test_dx_and_dy_raises_when_none(self):
        line = Line2D()
        line._pt1 = None
        with self.assertRaises(ValueError):
            line.dx()
        line._pt1 = Point2D()
        line._pt2 = None
        with self.assertRaises(ValueError):
            line.dy()

    def test_length(self):
        line = Line2D(Point2D(0, 0), Point2D(3, 4))
        self.assertAlmostEqual(line.length(), 5.0)
        line2 = Line2D(Point2D(1, 1), Point2D(4, 5))
        self.assertAlmostEqual(line2.length(), 5.0)

    def test_length_raises_when_none(self):
        line = Line2D()
        line._pt1 = None
        with self.assertRaises(ValueError):
            line.length()
        line._pt1 = Point2D()
        line._pt2 = None
        with self.assertRaises(ValueError):
            line.length()

    def test_angle_horizontal_0(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        self.assertAlmostEqual(line.angle_deg(), 0.0)

    def test_angle_horizontal_neg(self):
        line = Line2D(Point2D(1, 0), Point2D(0, 0))
        self.assertAlmostEqual(line.angle_deg(), 180)
    
    def test_angle_diagonal_45(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        self.assertAlmostEqual(line.angle_deg(), 45)

    def test_angle_vertical_90(self):
        line = Line2D(Point2D(0, 0), Point2D(0, 1))
        self.assertAlmostEqual(line.angle_deg(), 90)

    def test_angle_diagonal_225(self):
        line = Line2D(Point2D(0, 0), Point2D(-1, 1)) #
        self.assertAlmostEqual(line.angle_deg(), 135)

    def test_angle_horizontal_180(self):
        line = Line2D(Point2D(0, 0), Point2D(-1, 0))
        self.assertAlmostEqual(line.angle_deg(), 180)

    def test_angle_diagonal_135(self):
        line = Line2D(Point2D(0, 0), Point2D(-1, -1)) # 225
        self.assertAlmostEqual(line.angle_deg(), 225)    
    def test_angle_vertical_90(self):
        line = Line2D(Point2D(0, 0), Point2D(0, -1))
        self.assertAlmostEqual(line.angle_deg(), 270)

    def test_angle_negative(self):
        line = Line2D(Point2D(0, 0), Point2D(-1, -1)) #  225 degrees
        self.assertAlmostEqual(line.angle_deg(), 225)

    def test_angle_raises_when_none(self):
        line = Line2D()
        line._pt1 = None
        with self.assertRaises(ValueError):
            line.angle()
        line._pt1 = Point2D()
        line._pt2 = None
        with self.assertRaises(ValueError):
            line.angle()

    def test_set_length_positive(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        line.set_length(5)
        self.assertAlmostEqual(line.length(), 5.0)
        self.assertEqual(line._pt1, Point2D(0, 0))
        self.assertAlmostEqual(line._pt2.x, 5.0)
        self.assertAlmostEqual(line._pt2.y, 0.0)

    def test_set_length_positive(self):
        line = Line2D(Point2D(0, 0), Point2D(3, 4))
        line.set_length(10)
        self.assertAlmostEqual(line.length(), 10.0)
        self.assertEqual(line._pt1, Point2D(0, 0))
        self.assertAlmostEqual(line._pt2.x, 6)
        self.assertAlmostEqual(line._pt2.y, 8)
    def test_set_length_positive(self):
        line = Line2D(Point2D(0, 0), Point2D(-3, -4))
        line.set_length(10)
        self.assertAlmostEqual(line.length(), 10.0)
        self.assertEqual(line._pt1, Point2D(0, 0))
        self.assertAlmostEqual(line._pt2.x, -6)
        self.assertAlmostEqual(line._pt2.y, -8)
    def test_set_length_negative(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        with self.assertRaises(ValueError):
            line.set_length(-5)

    def test_set_length_none_points_raises(self):
        line = Line2D()
        line._pt1 = None
        with self.assertRaises(ValueError):
            line.set_length(5)
        line._pt1 = Point2D()
        line._pt2 = None
        with self.assertRaises(ValueError):
            line.set_length(5)

    def test_set_length_non_numeric_raises(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        with self.assertRaises(TypeError):
            line.set_length("not a number")

    def test_set_length_zero_length_raises(self):
        pt = Point2D(1, 1)
        line = Line2D(pt, pt)
        with self.assertRaises(ValueError):
            line.set_length(5)

    def test_set_angle_horizontal(self):
        line = Line2D(Point2D(0, 0), Point2D(0, 1))
        line.set_angle_deg(0)
        self.assertAlmostEqual(line.angle_deg(), 0.0)
        self.assertAlmostEqual(line._pt2.x, 1.0)
        self.assertAlmostEqual(line._pt2.y, 0.0)

    def test_set_angle_vertical_up(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        line.set_angle_deg(90)
        self.assertAlmostEqual(line.angle_deg(), 90)
        self.assertAlmostEqual(line._pt2.x, 0.0)
        self.assertAlmostEqual(line._pt2.y, 1.0)
    def test_set_angle_vertical_down(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        line.set_angle_deg(-90)
        self.assertAlmostEqual(line.angle_deg(), 90)
        self.assertAlmostEqual(line._pt2.x, 0.0)
        self.assertAlmostEqual(line._pt2.y, 1.0)
    def test_set_angle_vertical_down(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        line.set_angle_deg(270)
        self.assertAlmostEqual(line.angle_deg(), 270)
        self.assertAlmostEqual(line._pt2.x, 0.0)
        self.assertAlmostEqual(line._pt2.y, -1.0)

    def test_set_angle_diagonal_315(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        line.set_angle_deg(315)
        self.assertAlmostEqual(line.angle_deg(), 315)
        self.assertAlmostEqual(line._pt2.x, 0.7071067811865474)
        self.assertAlmostEqual(line._pt2.y, -0.7071067811865477)
        self.assertAlmostEqual(line.length(), 1.0)
    def test_set_angle_diagonal_minus45(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        line.set_angle_deg(-45)
        self.assertAlmostEqual(line.angle_deg(), 315)
        self.assertAlmostEqual(line._pt2.x, 0.7071067811865474)
        self.assertAlmostEqual(line._pt2.y, -0.7071067811865477)
    def test_set_angle_diagonal_plus45(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        line.set_angle_deg(45)
        self.assertAlmostEqual(line.angle_deg(), 45)
        self.assertAlmostEqual(line._pt2.x, 0.7071067811865474)
        self.assertAlmostEqual(line._pt2.y, 0.7071067811865477)
        self.assertAlmostEqual(line.length(), 1.0)
    def test_set_angle_diagonal_225(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        line.set_angle_deg(225)
        self.assertAlmostEqual(line.angle_deg(), 225)
        self.assertAlmostEqual(line._pt2.x, -0.7071067811865474)
        self.assertAlmostEqual(line._pt2.y, -0.7071067811865477)
        self.assertAlmostEqual(line.length(), 1.0)
    def test_set_angle_diagonal_minus135(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        line.set_angle_deg(-135)
        self.assertAlmostEqual(line.angle_deg(), 225)
        self.assertAlmostEqual(line._pt2.x, -0.7071067811865474)
        self.assertAlmostEqual(line._pt2.y, -0.7071067811865477)
        self.assertAlmostEqual(line.length(), 1.0)
    def test_set_angle_non_numeric_raises(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        with self.assertRaises(TypeError):
            line.set_angle("not a number")

    def test_set_angle_none_points_raises(self):
        line = Line2D()
        line._pt1 = None
        with self.assertRaises(ValueError):
            line.set_angle(45)
        line._pt1 = Point2D()
        line._pt2 = None
        with self.assertRaises(ValueError):
            line.set_angle(45)

    def test_set_angle_zero_length_raises(self):
        pt = Point2D(1, 1)
        line = Line2D(pt, pt)
        with self.assertRaises(ValueError):
            line.set_angle(45)

    def test_angle_to_line_horizontal_vs_vertical(self):
        line1 = Line2D(Point2D(0, 0), Point2D(1, 0))  # 0 deg
        line2 = Line2D(Point2D(0, 0), Point2D(0, 1))  # 90 deg
        angle, is_clockwise = line1.angle_to_line(line2)
        self.assertAlmostEqual(degrees(angle), 90)
        self.assertFalse(is_clockwise)

    def test_angle_to_line_vertical_vs_horizontal(self):
        line1 = Line2D(Point2D(0, 0), Point2D(0, 1))  # 90 deg
        line2 = Line2D(Point2D(0, 0), Point2D(1, 0))  # 0 deg
        angle, is_clockwise = line1.angle_to_line(line2)
        self.assertAlmostEqual(degrees(angle), 90)
        self.assertTrue(is_clockwise)
    def test_angle_to_line_from_315_to_225(self):
        line1 = Line2D(Point2D(0, 0), Point2D(1, 1))  # 45 deg
        line2 = Line2D(Point2D(0, 0), Point2D(-1, 1)) # 135 deg
        angle, is_clockwise = line1.angle_to_line(line2)
        self.assertAlmostEqual(degrees(angle), 90)
        self.assertFalse(is_clockwise)
    def test_angle_to_line_from_225_to_315(self):
        line1 = Line2D(Point2D(0, 0), Point2D(-1, 1))  # 225 deg
        line2 = Line2D(Point2D(0, 0), Point2D(1, 1)) # 315 deg
        angle, is_clockwise = line1.angle_to_line(line2)
        self.assertAlmostEqual(degrees(angle), 90)
        self.assertTrue(is_clockwise)
    def test_angle_to_line_from_315_to_135(self):
        line1 = Line2D(Point2D(0, 0), Point2D(1, 1))  # 315 deg
        line2 = Line2D(Point2D(0, 0), Point2D(-1, -1)) # 135 deg
        angle, is_clockwise = line1.angle_to_line(line2)
        self.assertAlmostEqual(degrees(angle), 180)
        self.assertFalse(is_clockwise)
    def test_angle_to_line_from_135_to_315(self):
        line1 = Line2D(Point2D(0, 0), Point2D(-1, -1))  # 135 deg
        line2 = Line2D(Point2D(0, 0), Point2D(1, 1)) # 315 deg
        angle, is_clockwise = line1.angle_to_line(line2)
        self.assertAlmostEqual(degrees(angle), 180)
        self.assertTrue(is_clockwise)

    def test_angle_to_line_same_direction(self):
        line1 = Line2D(Point2D(0, 0), Point2D(1, 0)) # 0 deg
        line2 = Line2D(Point2D(0, 0), Point2D(2, 0)) # 0 deg
        angle, is_clockwise = line1.angle_to_line(line2)
        self.assertAlmostEqual(angle, 0)
        self.assertTrue(is_clockwise)

    def test_angle_to_line_opposite_direction(self):
        line1 = Line2D(Point2D(0, 0), Point2D(1, 0)) # 0 deg
        line2 = Line2D(Point2D(0, 0), Point2D(-1, 0)) # 180 deg
        angle, is_clockwise = line1.angle_to_line(line2)
        self.assertAlmostEqual(degrees(angle), 180)
        self.assertFalse(is_clockwise)

    def test_angle_to_line_diagonal(self):
        line1 = Line2D(Point2D(0, 0), Point2D(1, 0))  # 0 deg
        line2 = Line2D(Point2D(0, 0), Point2D(1, 1))  # 45 deg
        angle, is_clockwise = line1.angle_to_line(line2)
        self.assertAlmostEqual(degrees(angle), 45)
        self.assertFalse(is_clockwise)

    def test_angle_to_line_type_error(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        with self.assertRaises(TypeError):
            line.angle_to_line("not a line")

    def test_angle_to_line_none_points_raises(self):
        line1 = Line2D(Point2D(0, 0), Point2D(1, 0))
        line2 = Line2D(Point2D(0, 0), Point2D(1, 0))
        line1._pt1 = None
        with self.assertRaises(ValueError):
            line1.angle_to_line(line2)
        line1._pt1 = Point2D(0, 0)
        line1._pt2 = None
        with self.assertRaises(ValueError):
            line1.angle_to_line(line2)
        line1._pt2 = Point2D(1, 0)
        line2._pt1 = None
        with self.assertRaises(ValueError):
            line1.angle_to_line(line2)
        line2._pt1 = Point2D(0, 0)
        line2._pt2 = None
        with self.assertRaises(ValueError):
            line1.angle_to_line(line2)

    def test_normal_vector_horizontal(self):
        line = Line2D(Point2D(0, 0), Point2D(2, 0))
        normal = line.normal_vector()
        self.assertIsInstance(normal, Line2D)
        # For horizontal line from (0,0) to (2,0), normal should go from (0,0) to (0,2)
        self.assertEqual(normal._pt1, Point2D(0, 0))
        self.assertEqual(normal._pt2, Point2D(0, 2))

    def test_normal_vector_vertical(self):
        line = Line2D(Point2D(0, 0), Point2D(0, 3))
        normal = line.normal_vector()
        self.assertIsInstance(normal, Line2D)
        # For vertical line from (0,0) to (0,3), normal should go from (0,0) to (-3,0)
        self.assertEqual(normal._pt1, Point2D(0, 0))
        self.assertEqual(normal._pt2, Point2D(-3, 0))

    def test_normal_vector_diagonal(self):
        line = Line2D(Point2D(1, 2), Point2D(4, 6))
        normal = line.normal_vector()
        self.assertIsInstance(normal, Line2D)
        # dx = 3, dy = 4, so normal should go from (1,2) to (1-4, 2+3) = (-3,5)
        self.assertEqual(normal._pt1, Point2D(1, 2))
        self.assertEqual(normal._pt2, Point2D(-3, 5))

    def test_normal_vector_negative(self):
        line = Line2D(Point2D(0, 0), Point2D(-2, -2))
        normal = line.normal_vector()
        self.assertIsInstance(normal, Line2D)
        # dx = -2, dy = -2, so normal should go from (0,0) to (0-(-2), 0+(-2)) = (2, -2)
        self.assertEqual(normal._pt1, Point2D(0, 0))
        self.assertEqual(normal._pt2, Point2D(2, -2))

    def test_normal_vector_zero_length_raises(self):
        pt = Point2D(1, 1)
        line = Line2D(pt, pt)
        with self.assertRaises(ValueError):
            line.normal_vector()

    def test_normal_vector_none_points_raises(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        line._pt1 = None
        with self.assertRaises(ValueError):
            line.normal_vector()
        line._pt1 = Point2D(0, 0)
        line._pt2 = None
        with self.assertRaises(ValueError):
            line.normal_vector()

    def test_set_polar_coordinates_horizontal(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        line.set_polar_coordinates(5, 0)
        self.assertAlmostEqual(line.length(), 5.0)
        self.assertAlmostEqual(line._pt2.x, 5.0)
        self.assertAlmostEqual(line._pt2.y, 0.0)

    def test_set_polar_coordinates_vertical_up(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        line.set_polar_coordinates(3, 270)
        self.assertAlmostEqual(line.length(), 3.0)
        self.assertAlmostEqual(line._pt2.x, 0.0)
        self.assertAlmostEqual(line._pt2.y, 3.0)

    def test_set_polar_coordinates_vertical_down(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        line.set_polar_coordinates(2, 90)
        self.assertAlmostEqual(line.length(), 2.0)
        self.assertAlmostEqual(line._pt2.x, 0.0)
        self.assertAlmostEqual(line._pt2.y, -2.0)

    def test_set_polar_coordinates_diagonal_315(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        line.set_polar_coordinates(1, 315)
        self.assertAlmostEqual(line.length(), 1.0)
        self.assertAlmostEqual(line._pt2.x, 0.7071067811865476)
        self.assertAlmostEqual(line._pt2.y, 0.7071067811865474)

    def test_set_polar_coordinates_negative_length_raises(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        with self.assertRaises(ValueError):
            line.set_polar_coordinates(-1, 45)

    def test_set_polar_coordinates_non_numeric_length_raises(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        with self.assertRaises(TypeError):
            line.set_polar_coordinates("not a number", 45)

    def test_set_polar_coordinates_non_numeric_angle_raises(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        with self.assertRaises(TypeError):
            line.set_polar_coordinates(5, "not a number")

    def test_set_polar_coordinates_none_points_raises(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        line._pt1 = None
        with self.assertRaises(ValueError):
            line.set_polar_coordinates(5, 45)
        line._pt1 = Point2D(0, 0)
        line._pt2 = None
        with self.assertRaises(ValueError):
            line.set_polar_coordinates(5, 45)

    def test_set_cartesian_coordinates_horizontal(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        result = line.set_cartesian_coordinates(5, 0)
        self.assertIs(result, line)
        self.assertEqual(line._pt2, Point2D(5, 0))
        self.assertAlmostEqual(line.length(), 5.0)

    def test_set_cartesian_coordinates_vertical(self):
        line = Line2D(Point2D(2, 3), Point2D(4, 5))
        result = line.set_cartesian_coordinates(2, 8)
        self.assertIs(result, line)
        self.assertEqual(line._pt2, Point2D(2, 8))
        self.assertAlmostEqual(line.length(), 5.0)

    def test_set_cartesian_coordinates_diagonal(self):
        line = Line2D(Point2D(1, 1), Point2D(2, 2))
        result = line.set_cartesian_coordinates(4, 5)
        self.assertIs(result, line)
        self.assertEqual(line._pt2, Point2D(4, 5))
        self.assertAlmostEqual(line.length(), sqrt((4-1)**2 + (5-1)**2))

    def test_set_cartesian_coordinates_non_numeric_x(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        with self.assertRaises(TypeError):
            line.set_cartesian_coordinates("not a number", 5)

    def test_set_cartesian_coordinates_non_numeric_y(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        with self.assertRaises(TypeError):
            line.set_cartesian_coordinates(5, None)

    def test_set_cartesian_coordinates_none_pt1_raises(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        line._pt1 = None
        with self.assertRaises(AttributeError):
            line.set_cartesian_coordinates(5, 5)

    def test_distance_to_point_horizontal(self):
        line = Line2D(Point2D(0, 0), Point2D(4, 0))
        pt = Point2D(2, 3)
        # Distance from (2,3) to y=0 is 3
        self.assertAlmostEqual(line.distance_to_point(pt), 3.0)

    def test_distance_to_point_vertical(self):
        line = Line2D(Point2D(1, 1), Point2D(1, 5))
        pt = Point2D(4, 3)
        # Distance from (4,3) to x=1 is 3
        self.assertAlmostEqual(line.distance_to_point(pt), 3.0)

    def test_distance_to_point_diagonal(self):
        line = Line2D(Point2D(0, 0), Point2D(4, 4))
        pt = Point2D(2, 0)
        # Distance from (2,0) to line y=x is sqrt(2)
        self.assertAlmostEqual(line.distance_to_point(pt), sqrt(2), places=6)

    def test_distance_to_point_on_line(self):
        line = Line2D(Point2D(0, 0), Point2D(4, 0))
        pt = Point2D(2, 0)
        self.assertAlmostEqual(line.distance_to_point(pt), 0.0)

    def test_distance_to_point_type_error(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        with self.assertRaises(TypeError):
            line.distance_to_point("not a point")

    def test_distance_to_point_none_points_raises(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        line._pt1 = None
        with self.assertRaises(ValueError):
            line.distance_to_point(Point2D(1, 2))
        line._pt1 = Point2D(0, 0)
        line._pt2 = None
        with self.assertRaises(ValueError):
            line.distance_to_point(Point2D(1, 2))

    def test_distance_to_point_zero_length_line(self):
        pt = Point2D(1, 1)
        line = Line2D(pt, pt)
        # Should return inf for zero-length line
        self.assertEqual(line.distance_to_point(Point2D(2, 2)), float('inf'))

    def test_rotate_horizontal_90(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        line.rotate(90)
        self.assertAlmostEqual(line._pt2.x, 0.0)
        self.assertAlmostEqual(line._pt2.y, 1.0)
        self.assertAlmostEqual(line.length(), 1.0)
    def test_rotate_horizontal_minus90(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        line.rotate(-90)
        self.assertAlmostEqual(line._pt2.x, 0.0)
        self.assertAlmostEqual(line._pt2.y, -1.0)
        self.assertAlmostEqual(line.length(), 1.0)
    def test_rotate_horizontal_180(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        line.rotate(180)
        self.assertAlmostEqual(line._pt2.x, -1.0)
        self.assertAlmostEqual(line._pt2.y, 0.0)
        self.assertAlmostEqual(line.length(), 1.0)

    def test_rotate_horizontal_270(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        line.rotate(270)
        self.assertAlmostEqual(line._pt2.x, 0.0)
        self.assertAlmostEqual(line._pt2.y, -1.0)
        self.assertAlmostEqual(line.length(), 1.0)

    def test_rotate_horizontal_360(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        line.rotate(360)
        self.assertAlmostEqual(line._pt2.x, 1.0)
        self.assertAlmostEqual(line._pt2.y, 0.0)
        self.assertAlmostEqual(line.length(), 1.0)

    def test_rotate_vertical_90(self):
        line = Line2D(Point2D(0, 0), Point2D(0, 1))
        line.rotate(90)
        self.assertAlmostEqual(line._pt2.x, -1.0)
        self.assertAlmostEqual(line._pt2.y, 0.0)
        self.assertAlmostEqual(line.length(), 1.0)
    
    def test_rotate_negative_angle(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        line.rotate(-90)
        self.assertAlmostEqual(line._pt2.x, 0)
        self.assertAlmostEqual(line._pt2.y, -1.0)
        self.assertAlmostEqual(line.length(), 1.0)
    def test_rotate_diagonal_45(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        line.rotate(45)
        self.assertAlmostEqual(line._pt2.x, 0.0)
        self.assertAlmostEqual(line._pt2.y, 1.41421356237309510)
        self.assertAlmostEqual(line.length(), sqrt(2))
    def test_rotate_diagonal_minus45(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        line.rotate(-45)
        self.assertAlmostEqual(line._pt2.x, 1.41421356237309510)
        self.assertAlmostEqual(line._pt2.y, 0.0)
        self.assertAlmostEqual(line.length(), sqrt(2))
    
    def test_rotate_non_numeric_angle_raises(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        with self.assertRaises(TypeError):
            line.rotate("not a number")

    def test_rotate_none_points_raises(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        line._pt1 = None
        with self.assertRaises(ValueError):
            line.rotate(90)
        line._pt1 = Point2D(0, 0)
        line._pt2 = None
        with self.assertRaises(ValueError):
            line.rotate(90)

    def test_evaluate_no_args_returns_none(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        self.assertIsNone(line.evaluate())

    def test_evaluate_one_point_on_line(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        pt = Point2D(2, 2)
        # For y = x, coefficients are a=1, b=-1, c=0
        # -(1*2 + (-1)*2 + 0)/-1 = -(2-2)/-1 = 0/-1 = 0.0
        self.assertAlmostEqual(line.evaluate(pt), 0.0)

    def test_evaluate_one_point_off_line(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        pt = Point2D(2, 3)
        # For y=0, coefficients a=0, b=-1, c=0
        # -(0*2 + (-1)*3 + 0)/-1 = -(-3)/-1 = 3/-1 = -3.0
        self.assertAlmostEqual(line.evaluate(pt), -3.0)

    def test_evaluate_two_points(self):
        line = Line2D(Point2D(0, 0), Point2D(0, 1))
        print(line.coefficients())
        x = 1
        y = 2
        #pt2 = Point2D(3, 4)
        # For vertical line x=0, coefficients a=1, b=0, c=0
        # b==0, so should return None
        self.assertIsNone(line.evaluate(x, y))

    def test_evaluate_non_point_arg_raises(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        with self.assertRaises(TypeError):
            line.evaluate("not a point")
        with self.assertRaises(TypeError):
            line.evaluate(Point2D(1, 2), "not a point")

    def test_evaluate_none_points_raises(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        line._pt1 = None
        with self.assertRaises(ValueError):
            line.evaluate(Point2D(1, 2))
        line._pt1 = Point2D(0, 0)
        line._pt2 = None
        with self.assertRaises(ValueError):
            line.evaluate(Point2D(1, 2))

    def test_intersection_with_parallel_lines(self):
        line1 = Line2D(Point2D(0, 0), Point2D(1, 1))
        line2 = Line2D(Point2D(0, 1), Point2D(1, 2))
        result, pt = line1.intersection_with(line2)
        self.assertFalse(result)
        self.assertEqual(pt, Point2D(0, 0))

    def test_intersection_with_coincident_lines(self):
        line1 = Line2D(Point2D(0, 0), Point2D(1, 1))
        line2 = Line2D(Point2D(0, 0), Point2D(1, 1))
        result, pt = line1.intersection_with(line2)
        self.assertFalse(result)
        self.assertEqual(pt, Point2D(0, 0))

    def test_intersection_with_degenerate_line(self):
        pt = Point2D(1, 1)
        line1 = Line2D(pt, pt)
        line2 = Line2D(Point2D(0, 0), Point2D(1, 1))
        result, pt_out = line1.intersection_with(line2)
        self.assertFalse(result)
        self.assertEqual(pt_out, Point2D(0, 0))

    def test_intersection_with_non_intersecting_lines(self):
        line1 = Line2D(Point2D(0, 0), Point2D(1, 0))
        line2 = Line2D(Point2D(0, 1), Point2D(1, 1))
        result, pt = line1.intersection_with(line2)
        self.assertFalse(result)
        self.assertEqual(pt, Point2D(0, 0))

    def test_intersection_with_intersecting_lines(self):
        line1 = Line2D(Point2D(0, 0), Point2D(1, 0))
        line2 = Line2D(Point2D(0.5, -1), Point2D(0.5, 1))
        result, pt = line1.intersection_with(line2)
        self.assertTrue(result)
        self.assertAlmostEqual(pt.x, 0.5)
        self.assertAlmostEqual(pt.y, 0.0)

    def test_intersection_with_intersecting_diagonal(self):
        line1 = Line2D(Point2D(0, 0), Point2D(2, 2))
        line2 = Line2D(Point2D(0, 2), Point2D(2, 0))
        result, pt = line1.intersection_with(line2)
        self.assertTrue(result)
        self.assertAlmostEqual(pt.x, 1.0)
        self.assertAlmostEqual(pt.y, 1.0)

    def test_intersection_with_type_error(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        with self.assertRaises(TypeError):
            line.intersection_with("not a line")

    def test_intersection_with_none_points_raises(self):
        line1 = Line2D(Point2D(0, 0), Point2D(1, 1))
        line2 = Line2D(Point2D(0, 0), Point2D(1, 1))
        line1._pt1 = None
        with self.assertRaises(ValueError):
            line1.intersection_with(line2)
        line1._pt1 = Point2D(0, 0)
        line1._pt2 = None
        with self.assertRaises(ValueError):
            line1.intersection_with(line2)
        line1._pt2 = Point2D(1, 1)
        line2._pt1 = None
        with self.assertRaises(ValueError):
            line1.intersection_with(line2)
        line2._pt1 = Point2D(0, 0)
        line2._pt2 = None
        with self.assertRaises(ValueError):
            line1.intersection_with(line2)

    def test_intersection_with_line_parallel(self):
        line1 = Line2D(Point2D(0, 0), Point2D(1, 1))
        line2 = Line2D(Point2D(0, 1), Point2D(1, 2))
        result, pt = line1.intersection_with_line(line2)
        self.assertEqual(result, 0)
        self.assertEqual(pt, Point2D(0, 0))

    def test_intersection_with_line_coincident(self):
        line1 = Line2D(Point2D(0, 0), Point2D(1, 1))
        line2 = Line2D(Point2D(0, 0), Point2D(1, 1))
        result, pt = line1.intersection_with_line(line2)
        self.assertEqual(result, 0)
        self.assertEqual(pt, Point2D(0, 0))

    def test_intersection_with_line_degenerate(self):
        pt = Point2D(1, 1)
        line1 = Line2D(pt, pt)
        line2 = Line2D(Point2D(0, 0), Point2D(1, 1))
        result, pt_out = line1.intersection_with_line(line2)
        self.assertEqual(result, 0)
        self.assertEqual(pt_out, Point2D(0, 0))

    def test_intersection_with_line_no_intersection(self):
        line1 = Line2D(Point2D(0, 0), Point2D(1, 0))
        line2 = Line2D(Point2D(0, 1), Point2D(1, 1))
        result, pt = line1.intersection_with_line(line2)
        self.assertEqual(result, 0)
        self.assertEqual(pt, Point2D(0, 0))

    def test_intersection_with_line_segments_intersect(self):
        line1 = Line2D(Point2D(0, 0), Point2D(2, 2))
        line2 = Line2D(Point2D(0, 2), Point2D(2, 0))
        result, pt = line1.intersection_with_line(line2)
        self.assertEqual(result, 1)
        self.assertAlmostEqual(pt.x, 1.0)
        self.assertAlmostEqual(pt.y, 1.0)

    def test_intersection_with_line_segments_intersect_outside(self):
        line1 = Line2D(Point2D(0, 0), Point2D(1, 1))
        line2 = Line2D(Point2D(2, 2), Point2D(3, 3))
        result, pt = line1.intersection_with_line(line2)
        self.assertEqual(result, 0)
        # Intersection point is outside both segments, but should be collinear
        self.assertIsInstance(pt, Point2D)

    def test_intersection_with_line_segments_intersect_at_endpoint(self):
        line1 = Line2D(Point2D(0, 0), Point2D(1, 1))
        line2 = Line2D(Point2D(1, 1), Point2D(2, 0))
        result, pt = line1.intersection_with_line(line2)
        self.assertEqual(result, 1)
        self.assertEqual(pt, Point2D(1, 1))

    def test_intersection_with_line_type_error(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        with self.assertRaises(TypeError):
            line.intersection_with_line("not a line")

    def test_intersection_with_line_none_points_raises(self):
        line1 = Line2D(Point2D(0, 0), Point2D(1, 1))
        line2 = Line2D(Point2D(0, 0), Point2D(1, 1))
        line1._pt1 = None
        with self.assertRaises(ValueError):
            line1.intersection_with_line(line2)
        line1._pt1 = Point2D(0, 0)
        line1._pt2 = None
        with self.assertRaises(ValueError):
            line1.intersection_with_line(line2)
        line1._pt2 = Point2D(1, 1)
        line2._pt1 = None
        with self.assertRaises(ValueError):
            line1.intersection_with_line(line2)
        line2._pt1 = Point2D(0, 0)
        line2._pt2 = None
        with self.assertRaises(ValueError):
            line1.intersection_with_line(line2)

    def test_sp_x_getter_and_setter(self):
        line = Line2D(Point2D(1, 2), Point2D(3, 4))
        self.assertEqual(line.sp_x, 1)
        line.sp_x = 10
        self.assertEqual(line._pt1.x, 10)
        self.assertEqual(line.sp_x, 10)

    def test_sp_x_setter_type_error(self):
        line = Line2D(Point2D(1, 2), Point2D(3, 4))
        with self.assertRaises(TypeError):
            line.sp_x = "not a number"
        line._pt1 = None
        with self.assertRaises(TypeError):
            line.sp_x = 5

    def test_sp_y_getter_and_setter(self):
        line = Line2D(Point2D(1, 2), Point2D(3, 4))
        self.assertEqual(line.sp_y, 2)
        line.sp_y = 20
        self.assertEqual(line._pt1.y, 20)
        self.assertEqual(line.sp_y, 20)

    def test_sp_y_setter_type_error(self):
        line = Line2D(Point2D(1, 2), Point2D(3, 4))
        with self.assertRaises(TypeError):
            line.sp_y = "not a number"
        line._pt1 = None
        with self.assertRaises(TypeError):
            line.sp_y = 5

    def test_ep_x_getter_and_setter(self):
        line = Line2D(Point2D(1, 2), Point2D(3, 4))
        self.assertEqual(line.ep_x, 3)
        line.ep_x = 30
        self.assertEqual(line._pt2.x, 30)
        self.assertEqual(line.ep_x, 30)

    def test_ep_x_setter_type_error(self):
        line = Line2D(Point2D(1, 2), Point2D(3, 4))
        with self.assertRaises(TypeError):
            line.ep_x = "not a number"
        line._pt2 = None
        # Should create a new Point2D if _pt2 is not a Point2D
        line.ep_x = 7
        self.assertIsInstance(line._pt2, Point2D)
        self.assertEqual(line._pt2.x, 7)

    def test_ep_y_getter_and_setter(self):
        line = Line2D(Point2D(1, 2), Point2D(3, 4))
        self.assertEqual(line.ep_y, 4)
        line.ep_y = 40
        self.assertEqual(line._pt2.y, 40)
        self.assertEqual(line.ep_y, 40)

    def test_ep_y_setter_type_error(self):
        line = Line2D(Point2D(1, 2), Point2D(3, 4))
        with self.assertRaises(TypeError):
            line.ep_y = "not a number"
        line._pt2 = None
        # Should create a new Point2D if _pt2 is not a Point2D
        line.ep_y = 8
        self.assertIsInstance(line._pt2, Point2D)
        self.assertEqual(line._pt2.y, 8)

  
    
if __name__ == "__main__":
    unittest.main()
