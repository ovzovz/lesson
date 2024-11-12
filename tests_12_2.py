import unittest
from runner import Runner
import runner_and_tournament as rt

class TournamentTest(unittest.TestCase):
    def test_start1(self):
        t = rt.Tournament(90, self.runner1, self.runner3 )
        self.all_results = t.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())] == 'Ник')

    def test_start2(self):
        t = rt.Tournament(90, self.runner2, self.runner3 )
        self.all_results = t.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())] == 'Ник')

    def test_start3(self):
        t = rt.Tournament(90, self.runner1, self.runner2, self.runner3 )
        self.all_results = t.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())] == 'Ник')

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = rt.Runner('Усэйн', 10)
        self.runner2 = rt.Runner('Андрей', 9)
        self.runner3 = rt.Runner('Ник', 3)

    def tearDown(self):
        print({x : str(y) for x, y in self.all_results.items()})

if __name__ == '__main__':
    unittest.main()