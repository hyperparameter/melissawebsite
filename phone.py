import webapp2
import cgi
from google.appengine.api import mail


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

    def post(self):
        phone = cgi.escape(self.request.get('PHONE'))
        mail.send_mail(sender="Daoud Clarke <daoud.clarke@gmail.com>",
                       to='daoud.clarke@gmail.com',
                       subject="Contact request from %s" % phone,
                       body="""
Good news! you have a request from: %s
""" % address)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Thanks! Someone will be in touch shortly.')

application = webapp2.WSGIApplication([
        ('/email.py', MainPage),
        ], debug=True)
