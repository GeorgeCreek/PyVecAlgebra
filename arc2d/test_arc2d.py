import unittest
from arc2d.arc2d import Arc2D
from point2d.point2d import Point2D

class TestArc2D(unittest.TestCase):
    def setUp(self):
        # This method will run before each test
        self.arc = Arc2D(Point2D(1, 2), Point2D(3, 4), Point2D(5, 6))
    def tearDown(self):
        # This method will run after each test
        pass
    def test_init_with_no_arguments(self):
        arc = Arc2D()
        self.assertEqual((arc._pt0.x, arc._pt0.y), (0, 0))
        self.assertEqual((arc._pt1.x, arc._pt1.y), (0, 0))
        self.assertEqual((arc._pt2.x, arc._pt2.y), (0, 0))

    def test_init_with_three_point2d(self):
        p0 = Point2D(1, 2)
        p1 = Point2D(3, 4)
        p2 = Point2D(5, 6)
        arc = Arc2D(p0, p1, p2)
        self.assertIs(arc._pt0, p0)
        self.assertIs(arc._pt1, p1)
        self.assertIs(arc._pt2, p2)

    def test_init_with_three_lists(self):
        arc = Arc2D([1, 2], [3, 4], [5, 6])
        self.assertEqual((arc._pt0.x, arc._pt0.y), (1, 2))
        self.assertEqual((arc._pt1.x, arc._pt1.y), (3, 4))
        self.assertEqual((arc._pt2.x, arc._pt2.y), (5, 6))

    def test_init_with_three_tuples(self):
        arc = Arc2D((1, 2), (3, 4), (5, 6))
        self.assertEqual((arc._pt0.x, arc._pt0.y), (1, 2))
        self.assertEqual((arc._pt1.x, arc._pt1.y), (3, 4))
        self.assertEqual((arc._pt2.x, arc._pt2.y), (5, 6))

    def test_init_with_mixed_types_raises_type_error(self):
        with self.assertRaises(TypeError):
            Arc2D(Point2D(1, 2), [3, 4], (5, 6))

    def test_init_with_wrong_number_of_points_raises_value_error(self):
        with self.assertRaises(ValueError):
            Arc2D(Point2D(1, 2), Point2D(3, 4))
        with self.assertRaises(ValueError):
            Arc2D(Point2D(1, 2), Point2D(3, 4), Point2D(5, 6), Point2D(7, 8))
    ########################################################
    def test_sp_property(self):
        self.assertEqual(self.arc.sp, self.arc._pt1)
        new_sp = Point2D(10, 10)
        self.arc.sp = new_sp
        self.assertEqual(self.arc.sp, new_sp)
        new_sp = (10, 20)
        self.arc.sp = new_sp
        self.assertEqual(self.arc.sp, Point2D(new_sp[0], new_sp[1]))
        new_sp = [10, 30]
        self.arc.sp = new_sp
        self.assertEqual(self.arc.sp, Point2D(*new_sp))
    def test_cp_property(self):
        self.assertEqual(self.arc.cp, self.arc._pt0)
        new_cp = Point2D(20, 20)
        self.arc.cp = new_cp
        self.assertEqual(self.arc.cp, new_cp)
        new_cp = (20, 30)
        self.arc.cp = new_cp
        self.assertEqual(self.arc.cp, Point2D(new_cp[0], new_cp[1]))
        new_cp = [20, 40]
        self.arc.cp = new_cp
        self.assertEqual(self.arc.cp, Point2D(*new_cp))       

    def test_ep_property(self):
        self.assertEqual(self.arc.ep, self.arc._pt2)
        new_ep = Point2D(30, 30)
        self.arc.ep = new_ep
        self.assertEqual(self.arc.ep, new_ep)
        new_ep = (30, 40)
        self.arc.ep = new_ep
        self.assertEqual(self.arc.ep, Point2D(new_ep[0], new_ep[1]))
        new_ep = [30, 50]
        self.arc.ep = new_ep
        self.assertEqual(self.arc.ep, Point2D(*new_ep))

    def test_sp_setter_invalid_type(self):
        with self.assertRaises(TypeError):
            self.arc.sp = "not a point"
        with self.assertRaises(TypeError):
            self.arc.sp = (1,)  # not length 2
        with self.assertRaises(TypeError):
            self.arc.sp = [1, "a"]  # non-numeric

    def test_cp_setter_invalid_type(self):
        with self.assertRaises(TypeError):
            self.arc.cp = 123
        with self.assertRaises(TypeError):
            self.arc.cp = (1,)  # not length 2
        with self.assertRaises(TypeError):
            self.arc.cp = [1, None]  # non-numeric

    def test_ep_setter_invalid_type(self):
        with self.assertRaises(TypeError):
            self.arc.ep = {"x": 1, "y": 2}
        with self.assertRaises(TypeError):
            self.arc.ep = (1, 2, 3)  # length 3
        with self.assertRaises(TypeError):
            self.arc.ep = [1, object()]  # non-numeric

    def test_sp_property_type_check(self):
        self.arc._pt1 = "not a Point2D"
        with self.assertRaises(TypeError):
            _ = self.arc.sp

    def test_cp_property_type_check(self):
        self.arc._pt0 = 42
        with self.assertRaises(TypeError):
            _ = self.arc.cp

    def test_ep_property_type_check(self):
        self.arc._pt2 = None
        with self.assertRaises(TypeError):
            _ = self.arc.ep


if __name__ == "__main__":
    unittest.main()
    