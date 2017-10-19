import unittest
import unittest.mock
import os

import bb_parser


class TestParseBitBakeFile(unittest.TestCase):
    def test_scrape_version_htop(self):
        """"
        Test that the version is correctly scraped from the file name
        """
        bb_file = os.path.join('tests', 'testfiles', 'bb', 'htop_1.0.3.bb')
        expect = "1.0.3"
        self.assertEqual(expect, bb_parser.scrape_version(os.path.basename(bb_file)))


if __name__ == '__main__':
    unittest.main(buffer=True)
