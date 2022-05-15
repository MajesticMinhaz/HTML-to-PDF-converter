from pdfkit import from_file

css_file = './files/style.css'  # your css file path
# If you have multiple css file then you need to add within a list. Like this ['first_path.css', 'second_path.css']


html_file = './files/index.html'  # your html file path

options = {  # your pdf file's configuration
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    'no-outline': None
}

from_file(  # call this function to get your pdf file
    input=html_file,
    output_path='./files/output.pdf',
    options=options,
    css=css_file
)

print("Program Finished")
