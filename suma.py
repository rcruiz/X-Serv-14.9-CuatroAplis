#!/usr/bin/python3

import webappmulti


class suma(webappmulti.app):
    """Simple add"""

    def __init__(self):
        """
        Included primero to operate.
        """
        self.primero = 0

    def parse(self, request, rest):
        try:
            numero = int(rest[1:])
        except ValueError:
            numero = "Error"
        return numero

    def process(self, parsedRequest):
        if parsedRequest != "Error":
            if not self.primero:
                self.primero = parsedRequest
                res = "falta segundo numero"
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
    testWebApp = webappmulti.webApp("localhost", 1234, {'/suma': suma})
