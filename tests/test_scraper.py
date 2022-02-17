import unittest

from src.scraper import LucernefestivalScraper


class TestScraperMethods(unittest.TestCase):
    def test_get_html(self):
        self.assertEqual(True, True)

    def test_parse(self):
        f = open("tests/data/main.html")
        cls = LucernefestivalScraper()
        self.assertEqual(
            len(
                cls.parse_page(
                    f,
                    'body > div.wi > div > main > div > div > div.mod-events-list > div.list > div[class="entry"]',
                )
            ),
            5,
        )


if __name__ == "__main__":
    unittest.main()
