from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf
from django.template.loader import get_template
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from io import BytesIO

class GeneratePDF(View):
    """docstring for GeneratePDF."""
    def get(self,request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
            "id_boleta": 123,
            "nombre": "John Doe",
            "monto": 10000,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf,content_type='application/pdf')
            filename = "Invoice_%d.pdf" %(context["id_boleta"])
            content = "inline; filename='%s'" %(filename) ## Para mostrarlo
            #content = "attachment; filename='%s'" %(filename) ## Para descarga forzada
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not Found")


def report(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
