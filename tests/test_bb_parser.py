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


    def test_scrape_version_vim(self):
        """"
        Test that the version is correctly scraped from the file name
        """
        bb_file = os.path.join('tests', 'testfiles', 'bb', 'vim_8.0.0983.bb')
        expect = "8.0.0983"
        self.assertEqual(expect, bb_parser.scrape_version(os.path.basename(bb_file)))


    # def test_scrape_summary_htop(self):
    #     """
    #     Test that the package summary is correctly scraped
    #     from the bitbake file.
    #     """
    #
    #     bb_file = os.path.join('tests', 'testfiles', 'bb', 'htop_1.0.3.bb')
    #     bb_parser.bb_scraper(bb_file)
    #     expect = "htop process monitor"
    #     self.assertEqual(expect,
    #             bb_parser.bb_dict.get('summary'))
    #
    #
    # def test_scrape_section_htop(self):
    #     """
    #     Test that the package section is correctly scraped
    #     from the bitbake file.
    #     """
    #
    #     bb_file = os.path.join('tests', 'testfiles', 'bb', 'htop_1.0.3.bb')
    #     bb_parser.bb_scraper(bb_file)
    #     expect = "console/utils"
    #     self.assertEqual(expect,
    #             bb_parser.bb_dict.get('section'))
    #
    #
    # def test_scrape_license_htop(self):
    #     """
    #     Test that the package license is correctly scraped
    #     from the bitbake file.
    #     """
    #
    #     bb_file = os.path.join('tests', 'testfiles', 'bb', 'htop_1.0.3.bb')
    #     bb_parser.bb_scraper(bb_file)
    #     expect = "GPLv2"
    #     self.assertEqual(expect,
    #             bb_parser.bb_dict.get('license'))


    def test_scrape_inherits_htop(self):
        """
        Test that the package inherits are correctly scraped as a list
        """
        bb_file = os.path.join('tests', 'testfiles', 'bb', 'htop_1.0.3.bb')
        bb_dict = bb_parser.bb_scraper(bb_file, None)
        expect = ["autotools"]
        self.assertEqual(expect, bb_dict.get('inherits'))


    def test_scrape_inherits_vim(self):
        """
        Test that the package inherits are correctly scraped as a list
        """
        
        bb_file = os.path.join('tests', 'testfiles', 'bb', 'vim_8.0.0983.bb')
        bb_dict = bb_parser.bb_scraper(bb_file, None)
        expect = ["autotools update-alternatives", "autotools-brokensep"]
        self.assertEqual(expect, bb_dict.get('inherits'))


    # def test_scrape_lic_files_chksum_htop_double_eq(self):
    #     """
    #     Test that the package license file checksum is correctly scraped
    #     from the bitbake file.
    #     """
    #
    #     bb_file = os.path.join('tests', 'testfiles', 'bb', 'htop_1.0.3.bb')
    #     bb_parser.bb_scraper(bb_file)
    #     expect = "file://COPYING;md5=c312653532e8e669f30e5ec8bdc23be3"
    #     self.assertEqual(expect,
    #             bb_parser.bb_dict.get('lic_files_chksum'))
    #
    #
    # def test_scrape_plus_equal_packageconfig_vim(self):
    #     """
    #     Test that the package inherits are correctly scraped as a list
    #     """
    #
    #     bb_file = os.path.join('tests', 'testfiles', 'bb', 'vim_8.0.0983.bb')
    #     bb_parser.bb_scraper(bb_file)
    #     expect = "??"
    #     self.assertEqual(expect,
    #             bb_parser.bb_dict.get('packageconfig'))
#
#
#     def test_scrape_src_uri_replace_version_htop(self):
#         """
#         Test that the src uri is scraped and that any occurances of
#         ${PV} is replaced by the collected version
#         """
#
#         bb_file = os.path.join('tests', 'testfiles', 'bb', 'htop_1.0.3.bb')
#         bb_parser.bb_scraper(bb_file)
#         expect = "http://hisham.hm/htop/releases/1.0.3/htop-1.0.3.tar.gz"
#         self.assertEqual(expect,
#                 bb_parser.bb_dict.get('src_uri'))
#
#
#     def test_scrape_src_uri_multilines_vim(self):
#         """
#         Test that the src uri is scraped when it is written across
#         multiple lines.
#         """
#
#         bb_file = os.path.join('tests', 'testfiles', 'bb', 'vim_8.0.0983.bb')
#         bb_parser.bb_scraper(bb_file)
#         expect = '"git://github.com/vim/vim.git \
#            file://disable_acl_header_check.patch;patchdir=.. \
#            file://vim-add-knob-whether-elf.h-are-checked.patch;patchdir=.. \
# "'
#         self.assertEqual(expect,
#                 bb_parser.bb_dict.get('src_uri'))

    #
    # def test_scrape_depends_htop(self):
    #     """
    #     Test that the package license is correctly scraped
    #     from the bitbake file.
    #     """
    #
    #     bb_file = os.path.join('tests', 'testfiles', 'bb', 'htop_1.0.3.bb')
    #     bb_parser.bb_scraper(bb_file)
    #     expect = "ncurses"
    #     self.assertEqual(expect,
    #             bb_parser.bb_dict.get('depends'))
    #
    #
    # def test_scrape_rdepends_htop(self):
    #     """
    #     Test that the package license is correctly scraped
    #     from the bitbake file.
    #     """
    #
    #     bb_file = os.path.join('tests', 'testfiles', 'bb', 'htop_1.0.3.bb')
    #     bb_parser.bb_scraper(bb_file)
    #     expect = "ncurses-terminfo"
    #     self.assertEqual(expect,
    #             bb_parser.bb_dict.get('rdepends_${pn}'))


if __name__ == '__main__':
    unittest.main(buffer=True)
