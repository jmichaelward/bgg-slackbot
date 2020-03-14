from bgg.api import BoardGameGeek

"""
Accepts and processes commands requested by users in Slack.

Commands:
- latest [username]: get the latest game played by a particular BoardGameGeek user.
"""
from flask import jsonify


class CommandHandler:
    def __init__(self, data):
        self.bgg = BoardGameGeek()
        self.data = data
        self.command_string = data['text']
        self.command = self.__get_command_name()
        self.command_args = self.__get_command_args()

    def handle(self):
        if 0 == len(self.command_string):
            return 'Please select a sub-command, e.g., _/bgg latest [username]_'

        # @TODO - Check for empty string. Our BGG command should have a subcommand.
        # Get the first word from the front of the string
        command = self.__get_command_name()
        arguments = self.__get_command_args()

        if 'latest' == command:
            return self.get_latest(arguments)
        elif 'hot' == command:
            return self.get_hot(arguments)

        return 'Command not found.'

    def __get_command_name(self):
        return self.command_string.split(' ', maxsplit=1)[0]

    def __get_command_args(self):
        data = self.command_string.split(' ', maxsplit=1)

        return data[1] if 2 == len(data) else ''

    def get_hot(self, data):
        return self.bgg.get_hotness()

    def get_latest(self, data):
        if 0 == len(data):
            return "Can't get the latest game because you didn't provide a username."

        username = data.split(' ', maxsplit=1)[0]

        return BoardGameGeek().get_collection(username)

