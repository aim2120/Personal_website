from jinja2 import Template

# Get File Content in String
jinja2_template_string = open("template.html", 'r').read()

print(jinja2_template_string)

# Create Template Object
template = Template(jinja2_template_string)

# Render HTML Template String
html_template_string = template.render(name = "John")

print(html_template_string)

output = open('index.html', 'w')
output.write(html_template_string)
output.close()
