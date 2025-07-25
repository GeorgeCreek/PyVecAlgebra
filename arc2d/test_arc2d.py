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

    def test_points_property(self):
        # First test - verify initial points
        self.assertEqual(self.arc.points, (self.arc._pt0, self.arc._pt1, self.arc._pt2))
        
        # Create a separate arc for testing
        arc = Arc2D(Point2D(1, 2), Point2D(3, 4), Point2D(5, 6))
        print(arc.points)
        # Test setting points with Point2D objects
        new_points = (Point2D(10, 20), Point2D(30, 40), Point2D(50, 60))
        arc.points = new_points
        print(arc.points)
        self.assertEqual(arc.points, new_points)  # Compare with new_points, not the original test points
        
        # Test setting points with lists
        list_points = ([11, 11], [22, 22], [33, 33])
        arc.points = list_points
        print(arc.points)
        expected_points = (Point2D(11, 11), Point2D(22, 22), Point2D(33, 33))
        self.assertEqual(arc.points, expected_points)
    
        # Test setting points with tuples
        tuple_points = ((22, 22), (33, 33), (44, 44))
        arc.points = tuple_points
        print(arc.points)
        expected_points = (Point2D(22, 22), Point2D(33, 33), Point2D(44, 44))
        self.assertEqual(arc.points, expected_points)
        
    def test_points_setter_with_empty_tuple(self):
        arc = Arc2D(Point2D(1, 2), Point2D(3, 4), Point2D(5, 6))
        arc.points = ()
        self.assertEqual(arc.points, (Point2D(0, 0), Point2D(0, 0), Point2D(0, 0)))

    def test_arc_length_and_arc_angle(self):
        # Create an arc with center at (0,0), start at (1,0), end at (0,1)
        # This should be a quarter circle, radius 1, angle pi/2, length pi/2
        arc = Arc2D(Point2D(0, 0), Point2D(1, 0), Point2D(0, 1))
        # Mock angle_to_line to return (pi/2, False) for this test if needed
        # But let's assume the implementation is correct and uses geometry
        # The radius is distance from center to start: sqrt((1-0)^2 + (0-0)^2) = 1
        self.assertAlmostEqual(arc.radius_cp_sp(), 1.0)
        # The angle should be pi/2 (90 degrees)
        angle = arc.arc_angle()
        self.assertAlmostEqual(angle, 1.57079632679, places=5)
        # The arc length should be radius * angle = 1 * pi/2 = pi/2
        length = arc.arc_length()
        self.assertAlmostEqual(length, 1.57079632679, places=5)

        # Test for a half circle (start at (1,0), end at (-1,0)), center at (0,0)
        arc = Arc2D(Point2D(0, 0), Point2D(1, 0), Point2D(-1, 0))
        angle = arc.arc_angle()
        self.assertAlmostEqual(angle, 3.14159265359, places=5)
        length = arc.arc_length()
        self.assertAlmostEqual(length, 3.14159265359, places=5)

        # Test for a full circle (start and end at (1,0)), center at (0,0)
        arc = Arc2D(Point2D(0, 0), Point2D(1, 0), Point2D(1, 0))
        angle = arc.arc_angle()
        # Depending on implementation, this could be 0 or 2*pi, but let's check for 0
        self.assertAlmostEqual(angle % (2 * 3.14159265359), 0.0, places=5)
        length = arc.arc_length()
        self.assertAlmostEqual(length, 0.0, places=5)

        # Test negative angle (start at (0,1), end at (1,0)), center at (0,0)
        arc = Arc2D(Point2D(0, 0), Point2D(0, 1), Point2D(1, 0))
        angle = arc.arc_angle()
        # Should be positive pi/2 after normalization
        self.assertAlmostEqual(angle, 1.57079632679, places=5)
        length = arc.arc_length()
        self.assertAlmostEqual(length, 1.57079632679, places=5)
    """
    def test_points_setter_with_three_point2d(self):
        arc = Arc2D()
        pts = (Point2D(7, 8), Point2D(9, 10), Point2D(11, 12))
        arc.points = pts
        self.assertEqual(arc.points, pts)

    def test_points_setter_with_three_lists(self):
        arc = Arc2D()
        new_points = ([1, 2], [3, 4], [5, 6])
        self.arc.points = new_points
        print(arc.points)
        self.assertEqual(arc.points, (Point2D(1, 2), Point2D(3, 4), Point2D(5, 6)))
        arc = Arc2D()
        pts = ([1, 2], [3, 4], [5, 6])
        arc.points = pts
        self.assertEqual(arc.points, (Point2D(1, 2), Point2D(3, 4), Point2D(5, 6)))
    """
    """
    def test_points_setter_with_three_tuples(self):
        arc = Arc2D()
        pts = ((1, 2), (3, 4), (5, 6))
        arc.points = pts
        self.assertEqual(arc.points, (Point2D(1, 2), Point2D(3, 4), Point2D(5, 6)))

    def test_points_setter_with_wrong_number_of_points(self):
        arc = Arc2D()
        with self.assertRaises(ValueError):
            arc.points = (Point2D(1, 2), Point2D(3, 4))
        with self.assertRaises(ValueError):
            arc.points = (Point2D(1, 2), Point2D(3, 4), Point2D(5, 6), Point2D(7, 8))

    def test_points_setter_with_mixed_types(self):
        arc = Arc2D()
        with self.assertRaises(TypeError):
            arc.points = (Point2D(1, 2), [3, 4], (5, 6))

    def test_points_setter_with_non_numeric_coordinates(self):
        arc = Arc2D()
        with self.assertRaises(TypeError):
            arc.points = ([1, "a"], [3, 4], [5, 6])

    def test_points_setter_with_invalid_type(self):
        arc = Arc2D()
        with self.assertRaises(ValueError):
            arc.points = "not a tuple"
    """

if __name__ == "__main__":
    unittest.main()
    