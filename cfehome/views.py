from datetime import datetime
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf
from django.template.loader import get_template
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from io import BytesIO
from django.utils import timezone
from django.db.models import (
    DateField, DateTimeField, DurationField, Field, Func, IntegerField,
    TimeField, Transform, fields,
)
from django.http import HttpResponse
from django.template.loader import render_to_string 
import tempfile
from io import StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from cgi import escape
# from models import * #Importar los modelos por aqui


def dummy_dict():
    orden = 1
    cant_cuotas = 1
    monto_total = 100000
    tipo_pago = "orden.tipo_pago"
    fecha_doc = "DD/MM/AAAA"
    time_trans = "HH:MM"
    nro_tarjeta = "XXXXXXXXXXXXXXXXXXXXX"
    num_orden = 1234
    # Obteniendo nro de contrato
    contrato = 1234
    num_cont = 1234
    # Obteniendo Datos Cliente
    cliente = 1
    nombre = "John"
    fst_ape = "Ein"
    scd_ape = "Zwei"
    name = nombre + " " + fst_ape + " " + scd_ape
    rut = 123456789-0
    # Obteniendo Datos de las Coutas
    cuotas = [1,2,3]
    dict_cuotas = dict()
    i = 1
    for a in cuotas:
        dict_cuotas[i] = {
            "nro": i,
            "cuota_id": i+1,
            "fecha_cuota": "DD/MM/AAAA",
            "monto": 30000
        }
        i = i + 1
    # Armando diccionario de las Cuotas
    template = get_template('invoice.html')
    context = {
        "name": name,
        "rut": rut,
        "doc_date": fecha_doc,
        "num_cont": num_cont,
        "time_trans": time_trans,
        "num_orden": num_orden,
        "name_bank": "nombre_banco",
        "monto": monto_total,
        "nro_tarjeta": nro_tarjeta,
        "tipo_pago": tipo_pago,
        "cant_cuotas": cant_cuotas,
        "vars": dict_cuotas
    }
    return context


class GeneratePDF(View):
    """docstring for GeneratePDF."""
    def get(self,request, *args, **kwargs):
        id_token = request.POST.get('token','')
        # Sacando datos necesarios de la Orden
        template = get_template('invoice.html')
        context = dummy_dict()
        html = render_to_string("invoice.html", context).encode('utf8')        
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

