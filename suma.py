#!/usr/bin/python

import webapp


class suma(webapp.app):
    """Simple add"""

    def __init__(self):
        """
        Included primero to operate.
        """
        self.primero = 0

    def parse(self, request, rest):
        """Parse the received request, extracting the relevant information."""
        try:
            numero = int(rest[1:])
        except ValueError:
            numero = "Error"
        return numero

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns 200 OK and an HTML page.
        """
        #global primero
        if parsedRequest != "Error":
            if not self.primero:
                self.primero = parsedRequest
                res = "falta segundo numero"
                #primero = False
            else:
                res = self.primero + parsedRequest
                self.primero = 0
            httpCode = "200 OK"
            htmlBody = "La suma es: " + str(res)
        else:
            httpCode = "400 Bad Request"
            htmlBody = "Usage Error: /suma/operando"
        return (httpCode, "<html><body><p>" + htmlBody + "</p></body></html>")


if __name__ == "__main__":
    suma = suma()
    testWebApp = webapp.webApp("localhost", 1234, {'/suma': suma})
