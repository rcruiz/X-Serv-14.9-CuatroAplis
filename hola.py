#!/usr/bin/python3

"""
Clase saludo y despedida basada en webappmulti
"""

import webappmulti


class saludo(webappmulti.app):
    """Hello/Bye worlds"""

    def parse(self, request, rest):
        recurso = request.split(' ', 2)[1]
        return recurso

    def process(self, parsedRequest):
        try:
            if parsedRequest.find('/hola') != -1:
                httpCod = "200 OK"
                htmlBody = "Hola."
            elif parsedRequest.find('/adios') != -1:
                httpCod = "200 OK"
                htmlBody = "Adios."
        except:
            httpCod = "400 Bad Request"
            htmlBody = "Usage Error: /hola or /adios "
        return (httpCod, "<html><body><h1>" + htmlBody + "</h1></body></html>")

if __name__ == "__main__":
    hola = saludo()
    adios = saludo()
    testWebApp = webappmulti.webApp("localhost", 1234, {'/hola': hola,
                                                        '/adios': adios})
