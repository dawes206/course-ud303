#Create a server that sends the path in message body when it gets a GET request
#Seend it a GET request to test using NCAT
#Navigate to server in web browser and see message

from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # First, send a 200 OK response.
        # Then send headers.
        # Now, write the response body.

        self.send_response(200)
        
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(self.path.encode())

    
if __name__ == '__main__':
    server_address = ('', 8000)  # Serve on all addresses, port 8000.
    httpd = HTTPServer(server_address, HelloHandler)
    httpd.serve_forever()
