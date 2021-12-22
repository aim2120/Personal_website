import os
from jinja2 import Template

# Get File Content in String
template_string = open("template.html", 'r').read()
artwork_template_string = open("artwork.html", 'r').read()
index_content_template_string = open("index_content.html", 'r').read()
contact_content_html_string = open("contact_content.html", 'r').read()

# Create Template Object
template = Template(template_string)
artwork_template = Template(artwork_template_string)
index_content_template = Template(index_content_template_string)

artwork_files = []
artwork_dir = os.getcwd() + '/images/artwork'
for filename in os.listdir(artwork_dir):
    if filename.endswith('.jpg'):
        artwork_files.append(filename)

artwork_files.sort()

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
index_context = dict(
    content = index_content_html_string,
    title = "Art"
)

contact_context = dict(
    content = contact_content_html_string,
    title = "Contact"
)

index_html_template_string = template.render(**index_context)
contact_html_template_string = template.render(**contact_context)

print(index_html_template_string)
print(contact_html_template_string)

index_output = open('index.html', 'w')
index_output.write(index_html_template_string)
index_output.close()

contact_output = open('contact.html', 'w')
contact_output.write(contact_html_template_string)
contact_output.close()
