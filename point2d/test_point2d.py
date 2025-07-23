import unittest
from math import sqrt
# from point2d.point2d import Point2D
from point2d import Point2D

import copy
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
    def test_distance_to_invalid_type(self):
        p1 = Point2D(1, 1)
        with self.assertRaises(TypeError):
            p1.distance_to((1, 2))
    
    def test_normalize_less_than_one(self):
        p = Point2D(0.5, 0.5)
        p.normalize()
        self.assertAlmostEqual(p.x, 0.7071, places=4)

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
        p.set_polar(5, 45)
        self.assertAlmostEqual(p.x, 3.5355339059327378)
        self.assertAlmostEqual(p.y, -3.5355339059327378)
        p.set_polar(5, -45)
        self.assertAlmostEqual(p.x, 3.5355339059327378)
        self.assertAlmostEqual(p.y, 3.5355339059327378)
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
        self.assertAlmostEqual(p.x, 0.6)
        self.assertAlmostEqual(p.y, 0.8)

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
    
    def test_angle_deg_on_x_axis(self):
        p = Point2D(5, 0)
        self.assertAlmostEqual(p.angle_deg(), 0.0)
        p_neg = Point2D(-5, 0)
        self.assertAlmostEqual(p_neg.angle_deg(), 180.0)

    def test_angle_deg_on_y_axis(self):
        p = Point2D(0, 5)
        self.assertAlmostEqual(p.angle_deg(), 270.0)
        p_neg = Point2D(0, -5)
        self.assertAlmostEqual(p_neg.angle_deg(), 90.0)

    def test_angle_deg_quadrants(self):
        p = Point2D(1, 1)
        self.assertAlmostEqual(p.angle_deg(), 315.0)
        p = Point2D(-1, 1)
        self.assertAlmostEqual(p.angle_deg(), 225.0)
        p = Point2D(-1, -1)
        self.assertAlmostEqual(p.angle_deg(), 135.0)
        p = Point2D(1, -1)
        self.assertAlmostEqual(p.angle_deg(), 45.0)

    def test_angle_deg_origin(self):
        p = Point2D(0, 0)
        self.assertAlmostEqual(p.angle_deg(), 0.0)
    
    def test_negate_positive_coordinates(self):
        p = Point2D(3, 4)
        neg = p.negate()
        self.assertIsInstance(neg, Point2D)
        self.assertEqual(neg.x, -3)
        self.assertEqual(neg.y, -4)

    def test_negate_negative_coordinates(self):
        p = Point2D(-2, -5)
        neg = p.negate()
        self.assertEqual(neg.x, 2)
        self.assertEqual(neg.y, 5)

    def test_negate_zero(self):
        p = Point2D(0, 0)
        neg = p.negate()
        self.assertEqual(neg.x, 0)
        self.assertEqual(neg.y, 0)

    def test_negate_mixed_coordinates(self):
        p = Point2D(-7, 8)
        neg = p.negate()
        self.assertEqual(neg.x, 7)
        self.assertEqual(neg.y, -8)

    def test_negate_does_not_modify_original(self):
        p = Point2D(1, -1)
        neg = p.negate()
        self.assertNotEqual(id(p), id(neg))
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, -1)

    def test_positive_positive_coordinates(self):
        p = Point2D(3, 4)
        pos = p.positive()
        self.assertIsInstance(pos, Point2D)
        self.assertEqual(pos.x, 3)
        self.assertEqual(pos.y, 4)

    def test_positive_negative_coordinates(self):
        p = Point2D(-2, -5)
        pos = p.positive()
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.y, 5)

    def test_positive_zero_coordinates(self):
        p = Point2D(0, 0)
        pos = p.positive()
        self.assertEqual(pos.x, 0)
        self.assertEqual(pos.y, 0)

    def test_positive_mixed_coordinates(self):
        p = Point2D(-7, 8)
        pos = p.positive()
        self.assertEqual(pos.x, 7)
        self.assertEqual(pos.y, 8)

    def test_positive_does_not_modify_original(self):
        p = Point2D(-1, 1)
        pos = p.positive()
        self.assertNotEqual(id(p), id(pos))
        self.assertEqual(p.x, -1)
        self.assertEqual(p.y, 1)
    
    def test_clone_returns_new_instance_with_same_coordinates(self):
        p = Point2D(10, 20)
        clone = p.clone()
        self.assertIsInstance(clone, Point2D)
        self.assertEqual(clone.x, 10)
        self.assertEqual(clone.y, 20)
        self.assertNotEqual(id(p), id(clone))

    def test_clone_of_origin(self):
        p = Point2D()
        clone = p.clone()
        self.assertEqual(clone.x, 0.0)
        self.assertEqual(clone.y, 0.0)
        self.assertNotEqual(id(p), id(clone))

    def test_clone_does_not_affect_original(self):
        p = Point2D(5, -7)
        clone = p.clone()
        clone.x = 100
        clone.y = 200
        self.assertNotEqual(p.x, clone.x)
        self.assertNotEqual(p.y, clone.y)
    
    def test_deepcopy_returns_new_instance_with_same_coordinates(self):
        p = Point2D(10, 20)
        p_deep = copy.deepcopy(p)
        self.assertIsInstance(p_deep, Point2D)
        self.assertEqual(p_deep.x, 10)
        self.assertEqual(p_deep.y, 20)
        self.assertNotEqual(id(p), id(p_deep))

    def test_deepcopy_of_origin(self):
        p = Point2D()
        p_deep = copy.deepcopy(p)
        self.assertEqual(p_deep.x, 0.0)
        self.assertEqual(p_deep.y, 0.0)
        self.assertNotEqual(id(p), id(p_deep))

    def test_deepcopy_does_not_affect_original(self):
        p = Point2D(5, -7)
        p_deep = copy.deepcopy(p)
        p_deep.x = 100
        p_deep.y = 200
        self.assertNotEqual(p.x, p_deep.x)
        self.assertNotEqual(p.y, p_deep.y)

    def test_deepcopy_memoization(self):
        p = Point2D(1, 2)
        memo = {}
        p_deep1 = p.__deepcopy__(memo)
        p_deep2 = p.__deepcopy__(memo)
        self.assertIs(p_deep1, p_deep2)
        self.assertEqual(p_deep1.x, 1)
        self.assertEqual(p_deep1.y, 2)





