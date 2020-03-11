"""
The main interface against the BoardGameGeek API.

The methods on the BoardGameGeek object will map directly to requests against the API. We just need a couple set
up for now so they can act as the data source for particular Slack commands.
"""
from flask import jsonify
from urllib.request import urlopen
import xmltodict


class BoardGameGeek:
    base_url = 'https://boardgamegeek.com/xmlapi2/'

    """
    Get the collection for a given user.
    
    This method will query the BoardGameGeek API for a user's collection. We'll then filter the
    individual titles into a list and return a JSON object with those values.
    
    @TODO - a lot.
    - BGG will return a non-200 response if it's the first request in awhile so that it can process the data.
    - We probably only want to show games that are owned, possibly excluding expansions.
    - Determine whether this would even be useful to return inside a Slack response. Some games lists could be gigantic.
    - Check for a cached request so we don't pound and get banned from the BGG servers.
    """
    def get_collection(self, username):
        request = urlopen(self.base_url + 'collection?username=' + username)
        data = xmltodict.parse(request.read())
        games = []

        for game in data['items']['item']:
            games.append(game['name']['#text'])

        return jsonify(games)
