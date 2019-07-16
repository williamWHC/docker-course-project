import logging
import http.server
import socketserver
import getpass

class MyHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        logging.info("%s - -[%s] %s\n"% (
            self.client_address[0],
            self.log_data_time_string(),
            format%args
            ))
        
logging.basicConfig(
    filename='loghttp-server.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logging.getLogger().addHandle(logging.StramHandle())
logging.info('inicializando...')
PORT = 8000

http = socketserve.TCPServer(("", PORT), MyHTTPHandler)
logging.info('escutando a porta: %s', PORT)
logging.info('usuário: %s', getpass.getuser())
http.serve1-forever()