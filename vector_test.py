import vector
import math
import unittest

class Vec3Test(unittest.TestCase):
    """
    Test the Vec3 class behavior
    """

    def test_vec_normalization(self):
        values = [vector.Vec3(1., 3., 10.), vector.Vec3(0., 1., 0.), vector.Vec3(50, -50, 30)]
        for v in values:
            self.assertAlmostEqual(v.normalized().length(), 1.0)

    def test_vec_printing(self):
        vec = vector.Vec3(5,3,0)
        self.assertEqual(str(vec), "(5, 3, 0)")

    def test_vec_addition(self):
        vec1 = vector.Vec3(5., 3., -2.)
        vec2 = vector.Vec3(-5., 2., 0.)
        expected = vector.Vec3(0., 5., -2.)
        self.assertEqual(vec1 + vec2, expected)

    def test_vec_spherical(self):
        vec = vector.unit_vector_from_spherical(0, math.pi / 4)
        self.assertAlmostEqual(vec.length(), 1)
        self.assertAlmostEqual(vec.x, 0.5 * math.sqrt(2))
        self.assertAlmostEqual(vec.y, 0)
        self.assertAlmostEqual(vec.z, 0.5 * math.sqrt(2))

if __name__ == '__main__':
    unittest.main()