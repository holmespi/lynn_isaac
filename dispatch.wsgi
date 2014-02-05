import os, sys
oldpath = sys.path
sys.path = ['/home/holmes90/'] + oldpath
sys.path.append("/home/holmes90/lynn_isaac");
os.environ['DJANGO_SETTINGS_MODULE'] = 'lynn_isaac.settings'
os.environ['PYTHON_EGG_CACHE'] = '/home/holmes90/.python_egg_cache'
import django.core.handlers.wsgi
_application = django.core.handlers.wsgi.WSGIHandler();
def application(environ, start_response):
environ['PATH_INFO'] = environ['SCRIPT_NAME'] + environ['PATH_INFO'];
try: # added so that I can see errors if they occur; should be removed once the website is fully functional
        return _application(environ, start_response)
except Exception, e:
                import traceback
                trace = traceback.format_exc()
                status = '500 Internal Server Error'
                output = trace
                response_headers = [('Content-type', 'text/plain'),('Content-Length', str(len(output)))]
                start_response(status, response_headers)
                return [output]