import unittest

from point2d import Point2D
class TestPoint2D(unittest.TestCase):
    def test_default_initialization(self):
        point = Point2D()
        self.assertEqual(point.x, 0.0)
        self.assertEqual(point.y, 0.0)

    def test_single_value_initialization(self):
        point = Point2D(5)        
        self.assertEqual(point.x, 5)
        self.assertEqual(point.y, 0.0)

    def test_tuple_initialization(self):
        point = Point2D((3, 4))
        self.assertEqual(point.x, 3)
        self.assertEqual(point.y, 4)

    def test_list_initialization(self):
        point = Point2D([1, 2])
        self.assertEqual(point.x, 1)
        self.assertEqual(point.y, 2)

    def test_point_initialization(self):
        original = Point2D(1, 2)
        point = Point2D(original)
        self.assertEqual(point.x, original.x)
        self.assertEqual(point.y, original.y)

    def test_two_values_initialization(self):
        point = Point2D(3, 4)
        self.assertEqual(point.x, 3)
        self.assertEqual(point.y, 4)

    def test_invalid_type_initialization(self):
        with self.assertRaises(TypeError):
            Point2D("invalid")

    def test_distance_to(self):
        p1 = Point2D(1, 1)
        p2 = Point2D(4, 5)
        distance = p1.distance_to(p2)
        expected_distance = ((1 - 4) ** 2 + (1 - 5) ** 2) ** 0.5
        self.assertAlmostEqual(distance, expected_distance)

    def test_equality(self):
        p1 = Point2D(1, 1)
        p2 = Point2D(1, 1)
        self.assertEqual(p1, p2)
        self.assertTrue(p1 == p2)

    def test_id_uniqueness(self):
        p1 = Point2D()
        p2 = Point2D()
        self.assertNotEqual(p1.get_id, p2.get_id)
        self.assertIsInstance(p1.get_id, int)
        self.assertIsInstance(p2.get_id, int)

    def test_x_setter_type_error(self):
        p = Point2D()
        with self.assertRaises(TypeError):
            p.x = "not a number"

    def test_y_setter_type_error(self):
        p = Point2D()
        with self.assertRaises(TypeError):
            p.y = [1, 2]

    def test_invalid_tuple_length(self):
        with self.assertRaises(TypeError):
            Point2D((1, 2, 3))
        with self.assertRaises(TypeError):
            Point2D([1, 2, 3])

    def test_invalid_two_values_type(self):
        with self.assertRaises(TypeError):
            Point2D(1, "a")

    def test_repr(self):
        p = Point2D(3, 4)
        self.assertEqual(repr(p), "Point2D(x=3, y=4)")

    def test_distance_to_type_error(self):
        p = Point2D(1, 2)
        with self.assertRaises(TypeError):
            p.distance_to((1, 2))

    def test_single_element_list(self):
        p = Point2D([7])
        self.assertEqual(p.x, 7)
        self.assertEqual(p.y, 0.0)

    def test_single_element_tuple(self):
        p = Point2D((8,))
        self.assertEqual(p.x, 8)
        self.assertEqual(p.y, 0.0)

    def test_large_number_of_arguments(self):
        with self.assertRaises(TypeError):
            Point2D(1, 2, 3)
    def test_set_polar_cartesian_conversion(self):
        p = Point2D()
        p.set_polar(5, 0)
        self.assertAlmostEqual(p.x, 5)
        self.assertAlmostEqual(p.y, 0)

        p.set_polar(5, 90)
        self.assertAlmostEqual(p.x, 0, places=6)
        self.assertAlmostEqual(p.y, -5, places=6)

        p.set_polar(5, 180)
        self.assertAlmostEqual(p.x, -5, places=6)
        self.assertAlmostEqual(p.y, 0, places=6)

        p.set_polar(5, 270)
        self.assertAlmostEqual(p.x, 0, places=6)
        self.assertAlmostEqual(p.y, 5, places=6)

    def test_set_polar_type_error(self):
        p = Point2D()
        with self.assertRaises(TypeError):
            p.set_polar("radius", 45)
        with self.assertRaises(TypeError):
            p.set_polar(5, "angle")

    def test_set_polar_negative_radius(self):
        p = Point2D()
        with self.assertRaises(ValueError):
            p.set_polar(-1, 45)
    
    def test_get_polar_origin(self):
        p = Point2D(0, 0)
        radius, angle = p.get_polar()
        self.assertAlmostEqual(radius, 0.0)
        self.assertAlmostEqual(angle, 0.0)

    def test_get_polar_on_x_axis(self):
        p = Point2D(5, 0)
        radius, angle = p.get_polar()
        self.assertAlmostEqual(radius, 5.0)
        self.assertAlmostEqual(angle, 0.0)
        
        p_neg = Point2D(-5, 0)
        radius, angle = p_neg.get_polar()
        self.assertAlmostEqual(radius, 5.0)
        self.assertAlmostEqual(angle, 180.0)

    def test_get_polar_on_y_axis(self):
        p = Point2D(0, 5)
        radius, angle = p.get_polar()
        self.assertAlmostEqual(radius, 5.0)
        self.assertAlmostEqual(angle, 270.0)

        p_neg = Point2D(0, -5)
        radius, angle = p_neg.get_polar()
        self.assertAlmostEqual(radius, 5.0)
        self.assertAlmostEqual(angle, 90.0)
    
    def test_get_polar_non_axis(self):
        p = Point2D(3, 4)
        radius, angle = p.get_polar()
        self.assertAlmostEqual(radius, 5.0)
        self.assertAlmostEqual(angle, 306.869897645844059)
        p_neg = Point2D(-3, -4)
        radius, angle = p_neg.get_polar()
        self.assertAlmostEqual(radius, 5.0)
        self.assertAlmostEqual(angle, 126.86989764584402)
        p = Point2D(5, 5)
        radius, angle = p.get_polar()
        self.assertAlmostEqual(radius, 5 * (2 ** 0.5))
        self.assertAlmostEqual(angle, 315.0)
        p = Point2D(5, -5)
        radius, angle = p.get_polar()
        self.assertAlmostEqual(radius, 5 * (2 ** 0.5))
        self.assertAlmostEqual(angle, 45.0) 

    def test_get_polar_quadrants(self):
        p = Point2D(1, 1)
        radius, angle = p.get_polar()
        self.assertAlmostEqual(radius, 2 ** 0.5)
        self.assertAlmostEqual(angle, 315.0)

        p = Point2D(-1, 1)
        radius, angle = p.get_polar()
        self.assertAlmostEqual(radius, 2 ** 0.5)
        self.assertAlmostEqual(angle, 225.0)

        p = Point2D(-1, -1)
        radius, angle = p.get_polar()
        self.assertAlmostEqual(radius, 2 ** 0.5)
        self.assertAlmostEqual(angle, 135.0)

        p = Point2D(1, -1)
        radius, angle = p.get_polar()
        self.assertAlmostEqual(radius, 2 ** 0.5)
        self.assertAlmostEqual(angle, 45.0)
    def test_normalize_origin(self):
        p = Point2D(0, 0)
        result = p.normalize()
        self.assertFalse(result)
        self.assertEqual(p.x, 0.0)
        self.assertEqual(p.y, 0.0)

    def test_normalize_unit_distance(self):
        p = Point2D(1, 0)
        result = p.normalize()
        self.assertTrue(result)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 0)

    def test_normalize_greater_than_one(self):
        p = Point2D(3, 4)  # distance = 5
        result = p.normalize()
        self.assertTrue(result)
        self.assertAlmostEqual(p.x, 0.6)
        self.assertAlmostEqual(p.y, 0.8)
        self.assertAlmostEqual((p.x ** 2 + p.y ** 2) ** 0.5, 1.0)

    def test_normalize_less_than_one(self):
        p = Point2D(0.3, 0.4)  # distance = 0.5
        result = p.normalize()
        self.assertTrue(result)
        self.assertAlmostEqual(p.x, 0.15)
        self.assertAlmostEqual(p.y, 0.2)

    def test_normalize_negative_distance(self):
        # Should never happen, but test for code path
        p = Point2D(0, 0)
        # Patch distance_to to return negative
        orig_distance_to = p.distance_to
        p.distance_to = lambda other: -1
        with self.assertRaises(ValueError):
            p.normalize()
        p.distance_to = orig_distance_to

    def test_normalize_raises_on_zero_distance(self):
        p = Point2D(0, 0)
        # Patch distance_to to return zero
        orig_distance_to = p.distance_to
        p.distance_to = lambda other: 0
        with self.assertRaises(ValueError):
            p.normalize()
        p.distance_to = orig_distance_to



