import unittest
import tests
import definition
import fixed_definition

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(tests.suite(definition.Account, definition.Advertiser))
    runner.run(tests.suite(fixed_definition.Account, fixed_definition.Advertiser))
