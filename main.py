#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class ExclaimHandler(webapp2.RequestHandler):
    def get(self):
        form_template = JINJA_ENVIRONMENT.get_template("templates/landing.html")
        self.response.write(form_template.render())

    def post(self):
      def add_excitement(phrase):
        return (phrase + "!!!").upper()
      user_input = self.request.get("user_word")
      excited_input = add_excitement(user_input)
      excited_dictionary = {"original_word":user_input, "excited_word":excited_input}
      excited_template = JINJA_ENVIRONMENT.get_template("templates/excited.html")
      self.response.write(excited_template.render(excited_dictionary))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/exclaim', ExclaimHandler)
], debug=True)
