import unittest
from line2d.line2d import Line2D
from point2d.point2d import Point2D

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

   
    '''
    def test_repr(self):
        l = Line2D(Point2D(1, 2), Point2D(3, 4))
        self.assertEqual(repr(l), "Line2D(Point2D(1, 2), Point2D(3, 4))")
    '''
if __name__ == "__main__":
    unittest.main()
