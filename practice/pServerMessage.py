#Create server that accespts a post request and prints the request body into response body
#Test server with ncat


from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class HelloHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        #Send response code
        self.send_response(200)
        
        contLen = int(self.headers.get('Content-length'))
        bodyCont = self.rfile.read(contLen).decode() #should be message='text in url-ese'
        bodyEng = parse_qs(bodyCont) #body content now in english
        messages = bodyEng['message'] #returns all values given to message variable
        message = messages[0]#just the message, in english
        #send headers
        self.send_header('Content-type','text/plain')
        #self.send_header('content-length',contLen)
        self.end_headers()
        #write body of response
        self.wfile.write(message.encode())
        

        

        

    
if __name__ == '__main__':
    server_address = ('', 8000)  # Serve on all addresses, port 8000.
    httpd = HTTPServer(server_address, HelloHandler)
    httpd.serve_forever()
