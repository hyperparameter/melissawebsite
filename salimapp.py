import webapp2
import cgi
from google.appengine.api import mail


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

    def post(self):
        address = cgi.escape(self.request.get('EMAIL'))
        mail.send_mail(sender="Daoud Clarke <daoud.clarke@gmail.com>",
                       to='sasobieroj@yahoo.co.uk, daoud.clarke@gmail.com',
                       subject="Contact request from %s" % address,
                       body="""
Hi Salim,

You have a contact request from:

%s

Love,

Daoud
""" % address)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Thanks! Someone will be in touch shortly.')

application = webapp2.WSGIApplication([
        ('/email.py', MainPage),
        ], debug=True)
