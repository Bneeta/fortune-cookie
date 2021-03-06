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
# working on
import webapp2
import random

class MainHandler(webapp2.RequestHandler):
    def getRandomfortunecookie(self):

        fortunecookie=["A dream you have will come true.","You will marry your lover.",
        "Your high-minded principles spell success.","You can make your own happiness.",
        "Wealth awaits you very soon.","A feeling is an idea with roots.",
        "Not all closed eye is sleeping, nor open eye is seeing.","Everything will be ok. Don't obsess.Time will prove you right, you must stay where you are."]

        display = random.choice(fortunecookie)

        return display

    def get(self):

        header="<h1> Fortune Cookie</h1>"

        fortunecookie="<strong>"+self.getRandomfortunecookie()+"</strong>"
        fortune_line="Your Fortune: " +  fortunecookie
        fortune_paragraph="<p>"+fortune_line+"</p>"

        number ="<strong>" +str(random.randint(1,100))+"</strong>"
        lucky_number="Your Lucky Number: "+ number
        number_paragraph="<p>"+lucky_number+"</p>"

        cookie_button ="<button>" "<a href= '.'> Another Cookie Please</a>""</button>"



        content= header + fortune_paragraph + number_paragraph + cookie_button


        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
