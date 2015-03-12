#!/usr/bin/python

"""
Clase servidor de aplicaciones, generador de URLs Aleatorias
Rosa Cristina Ruiz Rivas
Alumna de SAT
"""

import webapp
import random


class aleat(webapp.app):
    """Generator random URLs with classes"""

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns 200 OK and an HTML page.
        """
        randomURL = str(random.randint(0, 1000000000))
        newURL = "http://localhost:1234/aleat/" + randomURL
        return ("200 OK", "<html><body><p>Hola. " + '<a href="' + newURL +
                '">' + "Dame otra''</a>" + "</p></body></html>")


if __name__ == "__main__":
    aleato = aleat()
    testWebApp = webapp.webApp("localhost", 1234, {'/aleat': aleato},)
