#!/usr/bin/python3

import webappmulti
import random


class aleat(webappmulti.app):
    """Generator random URLs with classes"""

    def process(self, parsedRequest):
        randomURL = str(random.randint(0, 10000000))
        newURL = "http://localhost:1234/aleat/" + randomURL
        return ("200 OK", "<html><body><p>Hola. " + '<a href="' + newURL +
                '">' + "Dame otra</a>" + "</p></body></html>")


if __name__ == "__main__":
    aleatoria = aleat()
    testWebApp = webappmulti.webApp("localhost", 1234, {'/aleat/': aleatoria},)
