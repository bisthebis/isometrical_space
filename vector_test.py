import vector
import unittest

class Vec3Test(unittest.TestCase):
    """
    Test the Vec3 class behavior
    """

    def test_vec_normalization(self):
        values = [vector.Vec3(1., 3., 10.), vector.Vec3(0., 1., 0.), vector.Vec3(50, -50, 30)]
        for v in values:
            self.assertAlmostEqual(v.normalized().length(), 1.0)


if __name__ == '__main__':
    unittest.main()