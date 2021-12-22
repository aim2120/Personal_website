from jinja2 import Template

# Get File Content in String
template_string = open("template.html", 'r').read()
index_content_string = open("index_content.html", 'r').read()

# Create Template Object
template = Template(template_string)

# Render HTML Template String
context = dict(
    content = index_content_string,
    title = "Home"
)

html_template_string = template.render(**context)
print(html_template_string)

output = open('index.html', 'w')
output.write(html_template_string)
output.close()
