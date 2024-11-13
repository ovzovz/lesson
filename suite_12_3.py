import unittest
import test_12_3

TS=unittest.TestSuite()
TS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
TS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))
test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(TS)

