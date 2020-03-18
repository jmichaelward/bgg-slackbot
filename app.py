#!/usr/bin/env python3

"""
bgg-slackbot - a BoardGameGeek bot for Slack!

This app file is going to be the main dumping ground for logic and ideas as I work through this project.
I'm still learning about the Python language and the best way to structure my projects, and I want to have a
place to get those ideas down first before refactoring the logic into separate places within the app.

This means, too, that I'll be able to leave long comments about what it is in particular that I'm trying to
accomplish, without worrying too much about how things are structured or whether they need edits. The main goal
right now is to get a functioning app in place, and as large features come together, I'll look secondarily at
reorganizing the code. Things are going to be sloppy for awhile as I attempt to mentally map everything.
"""
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, json, request
import requests
from bgg.CommandHandler import CommandHandler
import bgg.api

load_dotenv()
app = Flask(__name__)
bgg_api = bgg.api.BoardGameGeek()


@app.route('/')
def main():
    return 'Welcome to the home of bgg-slackbot!'


@app.route('/slack', methods=['POST'])
def slack():
    data = request.get_json()
    challenge_token = data.get('challenge')

    if not challenge_token:
        return bgg_command(data)

    # @TODO Verify this Slack request. See: https://api.slack.com/events/url_verification
    return jsonify({
        'Content-type': 'application/json',
        'challenge': challenge_token
    })


def bgg_command(data):
    # @TODO Verify token from Slack.
    if not has_valid_token(data):
        return ''

    bgg_response = CommandHandler(data).handle()

    if not bgg_response:
        return ''

    try:
        return create_response({"text": bgg_response})
    except TypeError:
        return ''


def create_response(payload):
    requests.post(
        os.getenv('SLACKBOT_WEBHOOK_URL'),
        data=json.dumps(payload),
        headers={
            'Authorization': 'Bearer ' + os.getenv('SLACKBOT_ACCESS_TOKEN')
        }
    )

    return ''


# @TODO Figure out how to validate the token provided by Slack.
def has_valid_token(data):
    return True


if __name__ == "__main__":
    app.run(ssl_context='adhoc')
