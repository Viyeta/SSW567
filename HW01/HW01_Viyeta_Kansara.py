"""  Date: 10th Sept 2021
     Code by: Viyeta Kansara
     CWID: 10473081

     About Development: To write a function classify_triangle() that takes three  parameters: a, b, and c. 
     The three parameters represent the lengths of the sides of a triangle. 
     The function returns a string that specifies whether the triangle is scalene, isosceles, or equilateral, and whether
     it is a right triangle as well.

"""

import unittest


def classify_triangle(a: float, b: float, c: float) -> str:
    """ returns string specifying type of triangle """
    try:
        # Convert sides into float
        float(a)
        float(b)
        float(c)
    except ValueError:
        raise ValueError("Invalid input")

    if not is_valid_triangle(a, b, c):
        return 'NotATriangle'

    if is_equilateral(a, b, c):
        return 'Equilateral'
    elif is_isosceles(a, b, c):
        return 'Isosceles'
    elif is_right(a, b, c):
        return 'Right'
    else:
        return 'Scalene'


def is_valid_triangle(a, b, c):
    """ Checking if the triangle is valid"""
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    else:
        return True


def is_equilateral(a, b, c) -> bool:
    """ Returns true if all sides are equal """
    if a == b == c:
        return True
    return False


def is_isosceles(a, b, c) -> bool:
    """ Returns true if two sides are equal """
    if a == b or b == c or c == a:
        return True
    return False


def is_right(a, b, c) -> bool:
    """ Returns true if two sides are equal """
    if (a * a + b * b == c * c) or (c * c + b * b == a * a) or (a * a + c * c == b * b):
        return True
    return False


class Triangle(unittest.TestCase):

    # Test cases for triangles.
    def test(self):

        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3, 4, 5 is a Right triangle')
        self.assertEqual(classify_triangle(6, 9, 12), 'Scalene', '6, 9, 12 is a Scalene triangle')
        self.assertEqual(classify_triangle(6, 8, 10), 'Right', '6, 8, 10 is a Right triangle')
        self.assertEqual(classify_triangle(9, 9, 13), 'Isosceles', '9, 9, 13 is a Isosceles triangle')
        self.assertEqual(classify_triangle(8, 12, 8), 'Isosceles', '8, 12, 8 is a Isosceles triangle')
        self.assertEqual(classify_triangle(11, 12, 13), 'Scalene', '11, 12, 13 is a Scalene triangle')
        self.assertEqual(classify_triangle(10, 20, 15), 'Scalene', '10, 20, 15 is a Scalene triangle')
        self.assertEqual(classify_triangle(10, 10, 10), 'Equilateral', '10, 10, 10 is a Equilateral triangle')
        self.assertNotEqual(classify_triangle(19, 9, 9), 'Equilateral', '19, 9, 9 is not a Equilateral triangle')
        self.assertNotEqual(classify_triangle(10, 10, 10), 'Isosceles', '10, 10, 10 is not a Isosceles triangle')
        self.assertNotEqual(classify_triangle(6, 6, 8), 'Scalene', '6, 6, 8 is not a Scalene triangle')
        self.assertEqual(classify_triangle(1, 1, 10), 'NotATriangle', '1, 1, 10 is not a triangle')
        self.assertEqual(classify_triangle(0, 5, 10), 'NotATriangle', '0, 5, 10 is not a triangle')
        self.assertEqual(classify_triangle(-5, 10, 20), 'NotATriangle', 'is not a triangle')
        self.assertRaises(ValueError, classify_triangle, 'a', 'b', 'c')
        self.assertRaises(ValueError, classify_triangle, 1, 'b', 'c')
        self.assertRaises(ValueError, classify_triangle, 'a', 2, 'c')
        self.assertRaises(ValueError, classify_triangle, 'a', 'b', 3)
        self.assertRaises(ValueError, classify_triangle, 1, 2, 'c')
        self.assertRaises(ValueError, classify_triangle, 'a', 2, 3)
        self.assertRaises(ValueError, classify_triangle, 1, 'b', 3)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
