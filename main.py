import webapp2
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader= jinja2.FileSystemLoader(template_dir), autoescape=True)


def convert_to_rot13(input):
    small = map(chr, range(ord('a'), ord('z')+1))
    large = map(chr, range(ord('A'), ord('Z')+1))

    output = ""
    for char in input:
        if(char.isupper()):
            index = large.index(char) + 13 -26
            output += large[index]
        elif(char.islower()):
            index = small.index(char) + 13 -26
            output += small[index]
        else:
            output += char
    print output
    return output

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t= jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class RotHandler(Handler):
    def get(self):
        self.render("rot13.html", output="")

    def post(self):
        input = self.request.get("input")
        output = convert_to_rot13(input)
        self.render("rot13.html",output = output)



app = webapp2.WSGIApplication([
    ('/', RotHandler)],
    debug=True)

