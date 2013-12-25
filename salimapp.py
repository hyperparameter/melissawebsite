import webapp2
from google.appengine.api import mail


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

    def post(self):
        mail.send_mail(sender="Salim Sobieroj <support@example.com>",
                       to="Albert Johnson <daoud.clarke@gmail.com>",
                       subject="Your account has been approved",
                       body="""
Dear Albert:

Your example.com account has been approved.  You can now visit
http://www.example.com/ and sign in using your Google Account to
access new features.

Please let us know if you have any questions.

The example.com Team
""")
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

application = webapp2.WSGIApplication([
        ('/', MainPage),
        ], debug=True)
