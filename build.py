import os
from jinja2 import Template

# get templates and components from files
template_string = open("template.html", 'r').read()
artwork_template_string = open("artwork.html", 'r').read()
index_content_template_string = open("index_content.html", 'r').read()
contact_content_html_string = open("contact_content.html", 'r').read()

# create templates
template = Template(template_string)
artwork_template = Template(artwork_template_string)
index_content_template = Template(index_content_template_string)

# get artwork files
artwork_files = []
artwork_dir = os.getcwd() + '/images/artwork'
for filename in os.listdir(artwork_dir):
    if filename.endswith('.jpg'):
        artwork_files.append(filename)

artwork_files.sort()

# build the artworks html string
artworks_html_string = ''
for artwork_file in artwork_files:
    artwork_info = artwork_file.split('.')[0].split('_')
    artwork_context = dict(
        filename = artwork_file,
        title = ' '.join(artwork_info[2].split('-')),
        dimensions = artwork_info[4],
        year = artwork_info[5]
    )
    artworks_html_string += artwork_template.render(**artwork_context)
    artworks_html_string += '\n'


# create index file using artworks html string
index_content_context =  dict(
    artwork_content = artworks_html_string
)
index_content_html_string = index_content_template.render(**index_content_context)

# create index & contact contexts for top-level template
index_context = dict(
    content = index_content_html_string,
    title = "Art"
)
contact_context = dict(
    content = contact_content_html_string,
    title = "Contact"
)

# create the top-level html strings
index_html_string = template.render(**index_context)
contact_html_string = template.render(**contact_context)

print(index_html_string)
print(contact_html_string)

# write the top-level html strings to files
index_output = open('index.html', 'w')
index_output.write(index_html_string)
index_output.close()

contact_output = open('contact.html', 'w')
contact_output.write(contact_html_string)
contact_output.close()
