import unittest
from src import __main__ as main


class Test_CLI(unittest.TestCase):

    def test_download(self):
        # this is how to pass arguments to be parsed  by argparse
        # more information for unittest available at https://docs.python.org/3/library/unittest.html
        parser = main.parse_cmd_args(['download', 'google'])
        print(parser, parser.subparser_name, parser.url)
        self.assertTrue(1 == 1)

if __name__ == "__main__":
    unittest.main()