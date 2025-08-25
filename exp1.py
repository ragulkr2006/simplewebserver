from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!doctype html>
<html>
<head> <title> WEB PAGE </title>
</head>
<body>
    <table align="center" border="6" bgcolor="aqua"cellpadding="30">
        <caption>list of PROTOCOLS in TCP/IP Protocol suite</caption>
        <tr><th>S.No.</th><th>Name of the layer</th><th>Name of the protocol</th></tr>
        <tr><td>1</td><td bgcolor="red">Application Layer</td><td>HTTP,FTP,DNS & SSH</td> bgcolor="green"</tr>
        <tr><td>2</td><td>Transport Layer</td><td>TCP/UDP</td> bgcolor="violet"</tr>
        <tr><td>3</td><td>Network Layer</td><td>IPV4/IPV6</td> bgcolor="gold"</tr>
        <tr><td>4</td><td>Link Layer</td><td>Ethernet</td> bgcolor="pink"</tr>
    </table>
    

</body>
</html>'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()