import unittest

from urlParser import urlParser

class basicProtocolParsing(unittest.TestCase):
    def test_html_protocol(self):
        purl = urlParser('http://www.essex.ac.uk')
        self.assertEqual(purl.protocol, 'http')

    def test_ftp_protocol(self):
        purl = urlParser('ftp://ftp.essex.ac.uk')
        self.assertEqual(purl.protocol, 'ftp')

    def test_other_protocol(self):
        purl = urlParser('w61xw://some.site.com')
        self.assertEqual(purl.protocol, 'w61xw')