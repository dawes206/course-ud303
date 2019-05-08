#!/usr/bin/env python3
#
# Step one in building the messageboard server:
# An echo server for POST requests.
#
# Instructions:
#
# This server should accept a POST request and return the value of the
# "message" field in that request.
#
# You'll need to add three things to the do_POST method to make it work:
#
# 1. Find the length of the request data.
# 2. Read the correct amount of request data.
# 3. Extract the "message" field from the request data.
#
# When you're done, run this server and test it from your browser using the
# Messageboard.html form.  Then run the test.py script to check it.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

form = '''<!DOCTYPE html>
  <title>Message Board</title>
  <form method="POST" action="http://localhost:8000/">
    <textarea name="message"></textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>'''


class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 1. How long was the message? (Use the Content-Length header.)
        headers = self.headers
        conLength = int(headers.get('content-length',0))

        # 2. Read the correct amount of data from the request.
        requestData = self.rfile.read(conLength).decode() #turns message body into string
        
        # 3. Extract the "message" field from the request data.
        #message = requestData[requestData.find('=')+1:] #only manipulates string (keeping %21, not !)
        messageDict = parse_qs(requestData) #translates the message body %21 into !
        message = messageDict['message'][0]   #parse_qs returns a dictionary of dicatiory with lists, not strings, as values. Need [0] to index first value in list
        
        # Send the "message" field back as the response.
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        #self.wfile.write(message.encode())
        #self.wfile.write("Content-Length: ".encode())
        #self.wfile.write(str(conLength).encode())
        #self.wfile.write('\n'.encode())
        #self.wfile.write("Request Data: ".encode())
        #self.wfile.write(requestData.encode())
        #self.wfile.write('\n'.encode())
        #self.wfile.write('Message: '.encode())
        self.wfile.write(message.encode()) #turn message, including ! into bytes to send to browser.
    
    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(303, 'Redirect')
        
        # Then send headers.
        self.send_header('Content-type', 'Location', 'text/html; charset=utf-8') #Need to specify what type of content type. Here I guess it's html
        self.end_headers()
        
        # Now, write the response body.
        self.wfile.write(self.header.encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
