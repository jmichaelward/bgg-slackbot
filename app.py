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
from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return 'Welcome to the home of bgg-slackbot!'


if __name__ == "__main__":
    app.run()
