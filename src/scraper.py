from os import getenv
from typing import List
from dataclasses import dataclass, field
from urllib.request import urlopen

import psycopg

from bs4 import BeautifulSoup

from models.models import Event


@dataclass
class LucernefestivalScraper:
    """Scraper designed for the Lucernefestival events

    Args:
        url (str): url of the festival program
        events_selector (str): CSS selector to the parent div which encapsulates all events
        event_detail_selector (str): CSS selector to parent div which encapsulates event details
    """

    url: str
    events_selector: str
    event_detail_selector: str
    base_url: str = field(init=False)

    def __post_init__(self):
        self.base_url: str = "/".join(self.url.split("/")[0:3])

    def run(self):
        html_doc = self.get_html(self.url)
        raw_events = self.parse_page(html_doc, self.events_selector)
        events = self.parse_events(raw_events)
        self.insert_events(events)

    @staticmethod
    def get_html(url: str) -> str:
        return urlopen(url).read().decode("utf-8")

    def parse_page(self, html_doc: str, css_selector: str) -> List[str]:
        soup = BeautifulSoup(html_doc, "html.parser")
        if events := soup.select(css_selector):
            return events

        raise Exception(
            "No events found, can be 1) Edgecase 2) Website html structure changed"
        )

    @staticmethod
    def clean_work(raw_work: str) -> str:
        """This is not pretty"""
        with_seperator = raw_work.text.replace("\n\t\t\n\t\n\t\n\t\n", " - ")
        cleaner = with_seperator.replace("\n", "").replace("\t", "")
        cleaned = " ".join(cleaner.split())
        return cleaned

    def parse_events(self, raw_events: List[str]) -> List[dict]:
        events = []

        for event in raw_events:
            event_subdir = event.find("a", attrs={"class": "detail"}).attrs["href"]
            event_detail = self.get_html("/".join([self.base_url, event_subdir]))
            raw_works = self.parse_page(event_detail, self.event_detail_selector)
            raw_image_link = event.find("div", attrs={"class": "image"}).attrs["style"]

            events.append(
                Event(
                    date=event.attrs["data-date"],
                    time=event.find("span", attrs={"class": "time"}).text.replace(
                        ".", ":"
                    ),
                    location=event.find("p", attrs={"class": "location"}).text.strip(),
                    title=event.find("p", attrs={"class": "title"})
                    .text.split("|")[0]
                    .strip(),
                    artists=event.find("p", attrs={"class": "title"}).text.split("|")[
                        1:
                    ],
                    works=[self.clean_work(work) for work in raw_works],
                    image_link=raw_image_link[
                        raw_image_link.find("(") + 1 : raw_image_link.find(")")
                    ],
                )
            )

        return events

    def insert_events(self, events: dict):
        with psycopg.connect(getenv("DATABASE_URL")) as conn:
            with conn.cursor() as cur:
                with cur.copy(
                    "COPY event (date, time, location, title, artists, works, image_link) FROM STDIN"
                ) as copy:
                    for event in events:
                        copy.write_row(event.dict(exclude={"id"}).values())


if __name__ == "__main__":
    events_selector = getenv("EVENTS_SELECTOR", 'body > div.wi > div > main > div > div > div.mod-events-list > div.list > div[class="entry"]')
    event_detail_selector = getenv("EVENTS_DETAIL_SELECTOR", 'body > div.wi > div > main > div > div > div > div > div.content > div.tab-content > div > div > div.artists-musical-pieces > div[class="musical-piece"], div[class="with-spaces"]')

    scraper = LucernefestivalScraper(
        "https://www.lucernefestival.ch/en/program/summer-festival-22",
        events_selector,
        event_detail_selector,
    )
    scraper.run()
