import json
import time
from wsgiref.simple_server import make_server
from pl import PathDispatcher
#from loadData import loadData
#from retrieve import retrieve

_hello_resp = '''\
<html>
  <head>
     <title>Hello {name}</title>
   </head>
   <body>
     <h1>Hello {name}!</h1>
   </body>
</html>'''

def hello_world(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    params = environ['params']
    resp = _hello_resp.format(name=params.get('name'))
    yield resp.encode('utf-8')

# def match_info(environ, start_response):
#     start_response('200 OK', [('Content-type', 'text/html')])
#     params = environ['params']
#     load = loadData()
#     content = load.getTaskInfo(params.get('id'))
#     deal = retrieve()
#     resp = json.dumps(deal.getMatchInfos(content),ensure_ascii=False)
#     yield resp.encode('utf-8')

# def set_model(environ, start_response):
#     start_response('200 OK', [('Content-type', 'text/html')])
#     deal = retrieve()
#     resp = deal.setModel()
#     yield resp.encode('utf-8')

_localtime_resp = '''\
<?xml version="1.0"?>
<time>
  <year>{t.tm_year}</year>
  <month>{t.tm_mon}</month>
  <day>{t.tm_mday}</day>
  <hour>{t.tm_hour}</hour>
  <minute>{t.tm_min}</minute>
  <second>{t.tm_sec}</second>
</time>'''

def localtime(environ, start_response):
    start_response('200 OK', [('Content-type', 'application/xml')])
    resp = _localtime_resp.format(t=time.localtime())
    yield resp.encode('utf-8')

if __name__ == '__main__':

    # Create the dispatcher and register functions
    dispatcher = PathDispatcher()
    dispatcher.register('GET', '/hello', hello_world)
    # dispatcher.register('GET', '/getInfo', match_info)
    # dispatcher.register('GET', '/setModel', set_model)
    dispatcher.register('GET', '/localtime', localtime)

    # Launch a basic server
    httpd = make_server('', 8080, dispatcher)
    print('Serving on port 8080...')
    httpd.serve_forever()
