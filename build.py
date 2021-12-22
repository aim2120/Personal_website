import os
from jinja2 import Template

# Get File Content in String
template_string = open("template.html", 'r').read()
artwork_template_string = open("artwork.html", 'r').read()
index_content_template_string = open("index_content.html", 'r').read()

# Create Template Object
template = Template(template_string)
artwork_template = Template(artwork_template_string)
index_content_template = Template(index_content_template_string)

artwork_files = []
artwork_dir = os.getcwd() + '/images/artwork'
for filename in os.listdir(artwork_dir):
    if filename.endswith('.jpg'):
        artwork_files.append(filename)

sorted(artwork_files)

artworks_html_string = ''
for artwork_file in artwork_files:
    context = dict(
        filename = artwork_file
    )
    artworks_html_string += artwork_template.render(**context)


index_content_context =  dict(
    artwork_content = artworks_html_string
)

index_content_html_string = index_content_template.render(**index_content_context)

# Render HTML Template String
context = dict(
    content = index_content_html_string,
    title = "Home"
)

html_template_string = template.render(**context)
print(html_template_string)

output = open('index.html', 'w')
output.write(html_template_string)
output.close()
