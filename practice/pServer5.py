#Create a server that reads the body (web address) of the request (if requests have bodies?)
#Server parses web address in body, analyses it, and responds with it in body of response
#Start with just 1 attribute to be printed
#Seend it a GET request to test using NCAT
#Create loop to print all parsed-object attributes
#Seend it a GET request to test using NCAT


from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # First, send a 200 OK response.
        # Then send headers.
        # Now, write the response body.

        self.send_response(200)

        contLen = self.headers.get('Content-Length') #contLen will be string
        contLen = int(contLen) #converts to int
        request_body = self.rfile.read(contLen) #reads contLen number of bytes from request body
        request_body = request_body.decode()


        #Parse request
        bodyParse = urlparse(request_body) #creates parsed object

        
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        #self.wfile.write(bodyParse.scheme.encode())
        table = {'scheme':0,
                 'netloc':1,
                 'path': 2,
                 'query':3}
        for i in ['path','scheme','netloc','query']:
            self.wfile.write('{}: {}\n'.format(i,bodyParse[table[i]]).encode())

    
if __name__ == '__main__':
    server_address = ('', 8000)  # Serve on all addresses, port 8000.
    httpd = HTTPServer(server_address, HelloHandler)
    httpd.serve_forever()
