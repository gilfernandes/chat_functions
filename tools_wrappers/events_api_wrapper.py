import requests
import urllib.parse

from typing import Dict, Optional
from pydantic import BaseModel, Extra

class EventsAPIWrapper(BaseModel):
    """Wrapper around a custom API used to fetch public event information.

    There is no need to install any package to get this to work.
    """

    offset: int = 0
    limit: int = 10
    filter_by_country: str = "United Kingdom"
    doc_content_chars_max: int = 4000

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid

    def run(self, query: str) -> str:
        """Run Events search and get page summaries."""
        encoded_query =  urllib.parse.quote_plus(query)
        encoded_filter_by_country =  urllib.parse.quote_plus(self.filter_by_country)
        response = requests.get(f"https://events.brahmakumaris.org/events-rest/event-search-v2?search={encoded_query}" + 
                     f"&limit=10&offset={self.offset}&filterByCountry={encoded_filter_by_country}&includeDescription=true")
        if response.status_code >= 200 and response.status_code < 300:
            json = response.json()
            summaries = [self._formatted_event_summary(e) for e in json['events']]
            return "\n\n".join(summaries)[: self.doc_content_chars_max]
        else:
            return f"Failed to call events API with status code {response.status_code}"
        

    @staticmethod
    def _formatted_event_summary(event: Dict) -> Optional[str]:
        return (f"Event: {event['name']}\n" + 
                f"Start: {event['startDate']} {event['startTime']}\n" + 
                f"End: {event['endDate']} {event['endTime']}\n" +
                f"Venue: {event['venueAddress']} {event['postalCode']} {event['locality']} {event['countryName']}\n" +
                f"Event Description: {event['description']}\n" +
                f"Event URL: https://brahmakumaris.uk/event/?id={event['id']}\n"
        )
