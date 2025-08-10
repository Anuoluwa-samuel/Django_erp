# purchases/utils.py
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile

def generate_quotation_pdf(context):
    html_string = render_to_string('purchases/quotation_list.html', context)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as output:
        HTML(string=html_string).write_pdf(output.name)
        return output.name
