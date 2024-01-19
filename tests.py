import unittest
import coverage

if __name__ == "__main__":
    # Start coverage collection
    cov = coverage.Coverage()
    cov.start()

    # Load all tests from the 'autogpt/tests' package
    suite = unittest.defaultTestLoader.discover("./tests")

    # Run the tests
    unittest.TextTestRunner().run(suite)
    cov.stop()
    cov.save()
    cov.report(show_missing=True)
