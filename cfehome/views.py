from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf
from django.template.loader import get_template
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from io import BytesIO
from django.utils import timezone



class GeneratePDF(View):
    """docstring for GeneratePDF."""
    def get(self,request, *args, **kwargs):
        template = get_template('invoice.html')
        cuotas = {
            "couta_1":{
                "numero": 1,
                "fecha_cobro": "12/12/1234",
                "fecha_pago": "12/12/1234",
                "valor": "123.456",
                "codigo": "123456789"
            },
            "couta_2":{
                "numero": 2,
                "fecha_cobro": "12/12/1234",
                "fecha_pago": "12/12/1234",
                "valor": "123.456",
                "codigo": "123456789"
            }
         }
        context = {
            "name": "John Doe",
            "rut": "12.345.678-9",
            "doc_date": "12/12/1234",
            "num_contrato": "12345-6",
            "time_trans": "12:34",
            "num_orden": "12345678900000",
            "name_bank": "XXXXXXXXXXXXXXXXX",
            "vars": cuotas
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf,content_type='application/pdf')
            filename = "Invoice_%s.pdf" %(context["num_orden"])
            content = "inline; filename='%s'" %(filename) ## Para mostrarlo
            #content = "attachment; filename='%s'" %(filename) ## Para descarga forzada
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not Found")


