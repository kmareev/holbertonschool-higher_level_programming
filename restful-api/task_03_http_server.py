#!/usr/bin/python3
"""This module sets up a basic HTTP server using
'http.server'."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        '''get landing page'''
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(bytes("Hello, this is a simple API!", "utf-8"))

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = json.dumps({"name": "John", "age": 30, "city": "New York"})
            self.wfile.write(bytes(data, "utf-8"))

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = json.dumps(
                {"version": "1.0", "description": "A simple API built with http.server"})
            self.wfile.write(bytes(data, "utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "plain/text")
            self.end_headers()

            self.wfile.write(bytes("OK", "utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(bytes("404 Not Found", "utf-8"))

PORT = 8000
Handler = SimpleHTTPHandler
HOST = "localhost"

server = HTTPServer((HOST, PORT), SimpleHTTPHandler)
print("Server is running at localhost: 8000")
server.serve_forever()
