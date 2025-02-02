import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        r = runner.Runner('Makar')
        for i in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    def test_run(self):
        r = runner.Runner('Denis')
        for i in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    def test_challenge(self):
        r1 = runner.Runner('Nadya')
        r2 = runner.Runner('Veronika')
        for i in range(10):
            r1.walk()         
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)


if __name__ == "__main__":
    unittest.main()
