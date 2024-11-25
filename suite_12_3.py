import unittest
import tests_12_1
import tests_12_2

suiteTs = unittest.TestSuite()
suiteTs.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
suiteTs.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suiteTs)
