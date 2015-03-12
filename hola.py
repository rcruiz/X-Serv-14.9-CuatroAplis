#!/usr/bin/python
# -*- coding: latin-1-*-
"""
Clase saludo y despedida basada en webappmulti
Rosa Cristina Ruiz Rivas
Alumna de SAT
"""

import webapp


class saludo(webapp.app):
    """Hello/Bye worlds"""

    def parse(self, request, rest):
        """Parse the received request,extracting the relevant information."""
        recurso = request.split(' ', 2)[1]
        return recurso

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns 200 OK and an HTML page.
        """
        try:
            if parsedRequest.find('/hola') != -1:
                httpCod = "200 OK"
                htmlBody = "Hola."
            elif parsedRequest.find('/adios') != -1:
                httpCod = "200 OK"
                htmlBody = "Adi\xf3s."
        except:
            httpCod = "400 Bad Request"
            htmlBody = "Usage Error: /hola or /adios "
        #print parsedRequest, "Aqui process"
        return (httpCod, "<html><body><h1>" + htmlBody + "</h1></body></html>")

if __name__ == "__main__":
    hola = saludo()
    adios = saludo()
    testWebApp = webapp.webApp("localhost", 1234, {'/hola': hola,
                               '/adios': adios})
