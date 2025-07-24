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

    def test_get_points(self):
        pt1 = Point2D(10, 20)
        pt2 = Point2D(30, 40)
        line = Line2D(pt1, pt2)
        points = line.get_points()
        self.assertEqual(points, (pt1, pt2))

    def test_get_points_raises_when_none(self):
        line = Line2D()
        # Manually set to None to simulate error condition
        line._pt1 = None
        with self.assertRaises(ValueError):
            line.get_points()
        line._pt1 = Point2D()
        line._pt2 = None
        with self.assertRaises(ValueError):
            line.get_points()

    def test_set_points_valid(self):
        line = Line2D()
        pt1 = Point2D(1, 1)
        pt2 = Point2D(2, 2)
        line.set_points(pt1, pt2)
        self.assertEqual(line._pt1, pt1)
        self.assertEqual(line._pt2, pt2)

    def test_set_points_invalid(self):
        line = Line2D()
        with self.assertRaises(TypeError):
            line.set_points("not a point", Point2D(1, 2))
        with self.assertRaises(TypeError):
            line.set_points(Point2D(1, 2), 123)

    def test_sp_x_property(self):
        line = Line2D(Point2D(1, 2), Point2D(3, 4))
        self.assertEqual(line.sp_x, 1)
        line.sp_x = 10
        self.assertEqual(line.sp_x, 10)
        self.assertEqual(line._pt1.x, 10)

    def test_sp_x_setter_creates_point_if_none(self):
        line = Line2D()
        line._pt1 = None
        line.sp_x = 5
        self.assertIsInstance(line._pt1, Point2D)
        self.assertEqual(line.sp_x, 5)

    def test_sp_x_getter_raises_if_none(self):
        line = Line2D()
        line._pt1 = None
        with self.assertRaises(ValueError):
            _ = line.sp_x

    def test_sp_y_property(self):
        line = Line2D(Point2D(1, 2), Point2D(3, 4))
        self.assertEqual(line.sp_y, 2)
        line.sp_y = 20
        self.assertEqual(line.sp_y, 20)
        self.assertEqual(line._pt1.y, 20)

    def test_sp_y_setter_creates_point_if_none(self):
        line = Line2D()
        line._pt1 = None
        line.sp_y = 15
        self.assertIsInstance(line._pt1, Point2D)
        self.assertEqual(line.sp_y, 15)

    def test_sp_y_getter_raises_if_none(self):
        line = Line2D()
        line._pt1 = None
        with self.assertRaises(ValueError):
            _ = line.sp_y

    def test_ep_x_property(self):
        line = Line2D(Point2D(1, 2), Point2D(3, 4))
        self.assertEqual(line.ep_x, 3)
        line.ep_x = 30
        self.assertEqual(line.ep_x, 30)
        self.assertEqual(line._pt2.x, 30)

    def test_ep_x_setter_creates_point_if_none(self):
        line = Line2D()
        line._pt2 = None
        line.ep_x = 25
        self.assertIsInstance(line._pt2, Point2D)
        self.assertEqual(line.ep_x, 25)

    def test_ep_x_getter_raises_if_none(self):
        line = Line2D()
        line._pt2 = None
        with self.assertRaises(ValueError):
            _ = line.ep_x

    def test_ep_y_property(self):
        line = Line2D(Point2D(1, 2), Point2D(3, 4))
        self.assertEqual(line.ep_y, 4)
        line.ep_y = 40
        self.assertEqual(line.ep_y, 40)
        self.assertEqual(line._pt2.y, 40)

    def test_ep_y_setter_creates_point_if_none(self):
        line = Line2D()
        line._pt2 = None
        line.ep_y = 35
        self.assertIsInstance(line._pt2, Point2D)
        self.assertEqual(line.ep_y, 35)

    def test_ep_y_getter_raises_if_none(self):
        line = Line2D()
        line._pt2 = None
        with self.assertRaises(ValueError):
            _ = line.ep_y

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

    def test_repr(self):
        pt1 = Point2D(1, 2)
        pt2 = Point2D(3, 4)
        line = Line2D(pt1, pt2)
        self.assertEqual(repr(line), f"Line2D({pt1}, {pt2})")

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
    
    def test_angle_diagonal_315(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 1))
        self.assertAlmostEqual(line.angle_deg(), 315)

    def test_angle_vertical_270(self):
        line = Line2D(Point2D(0, 0), Point2D(0, 1))
        self.assertAlmostEqual(line.angle_deg(), 270)

    def test_angle_diagonal_225(self):
        line = Line2D(Point2D(0, 0), Point2D(-1, 1))
        self.assertAlmostEqual(line.angle_deg(), 225)

    def test_angle_horizontal_180(self):
        line = Line2D(Point2D(0, 0), Point2D(-1, 0))
        self.assertAlmostEqual(line.angle_deg(), 180)

    def test_angle_diagonal_135(self):
        line = Line2D(Point2D(0, 0), Point2D(-1, -1))
        self.assertAlmostEqual(line.angle_deg(), 135)    
    def test_angle_vertical_90(self):
        line = Line2D(Point2D(0, 0), Point2D(0, -1))
        self.assertAlmostEqual(line.angle_deg(), 90)

    def test_angle_negative(self):
        line = Line2D(Point2D(0, 0), Point2D(-1, -1))
        self.assertAlmostEqual(line.angle_deg(), 135)

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
        line.set_angle(0)
        self.assertAlmostEqual(line.angle_deg(), 0.0)
        self.assertAlmostEqual(line._pt2.x, 1.0)
        self.assertAlmostEqual(line._pt2.y, 0.0)

    def test_set_angle_vertical_up(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        line.set_angle(270)
        self.assertAlmostEqual(line.angle_deg(), 270)
        self.assertAlmostEqual(line._pt2.x, 0.0)
        self.assertAlmostEqual(line._pt2.y, 1.0)

    def test_set_angle_vertical_down(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        line.set_angle(90)
        self.assertAlmostEqual(line.angle_deg(), 90)
        self.assertAlmostEqual(line._pt2.x, 0.0)
        self.assertAlmostEqual(line._pt2.y, -1.0)

    def test_set_angle_diagonal_315(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        line.set_angle(315)
        self.assertAlmostEqual(line.angle_deg(), 315)
        self.assertAlmostEqual(line._pt2.x, 0.7071067811865474)
        self.assertAlmostEqual(line._pt2.y, 0.7071067811865477)
        self.assertAlmostEqual(line.length(), 1.0)
    def test_set_angle_diagonal_minus45(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        line.set_angle(-45)
        self.assertAlmostEqual(line.angle_deg(), 315)
        self.assertAlmostEqual(line._pt2.x, 0.7071067811865474)
        self.assertAlmostEqual(line._pt2.y, 0.7071067811865477)
        self.assertAlmostEqual(line.length(), 1.0)
    def test_set_angle_diagonal_225(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        line.set_angle(225)
        self.assertAlmostEqual(line.angle_deg(), 225)
        self.assertAlmostEqual(line._pt2.x, -0.7071067811865474)
        self.assertAlmostEqual(line._pt2.y, 0.7071067811865477)
        self.assertAlmostEqual(line.length(), 1.0)
    def test_set_angle_diagonal_minus135(self):
        line = Line2D(Point2D(0, 0), Point2D(1, 0))
        line.set_angle(-135)
        self.assertAlmostEqual(line.angle_deg(), 225)
        self.assertAlmostEqual(line._pt2.x, -0.7071067811865474)
        self.assertAlmostEqual(line._pt2.y, 0.7071067811865477)
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

    
    
if __name__ == "__main__":
    unittest.main()
