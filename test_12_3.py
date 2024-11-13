import unittest
from runner import Runner
import runner_and_tournament as rt

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner('first')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('first')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner('first')
        runner2 = Runner('second')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @unittest.skipIf( is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start1(self):
        t = rt.Tournament(90, self.runner1, self.runner3 )
        self.all_results = t.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start2(self):
        t = rt.Tournament(90, self.runner2, self.runner3 )
        self.all_results = t.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start3(self):
        t = rt.Tournament(90, self.runner1, self.runner2, self.runner3 )
        self.all_results = t.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())] == 'Ник')

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner1 = rt.Runner('Усэйн', 10)
        self.runner2 = rt.Runner('Андрей', 9)
        self.runner3 = rt.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def tearDown(self):
        pass
        #print({x : str(y) for x, y in self.all_results.items()})

if __name__ == '__main__':
    unittest.main()