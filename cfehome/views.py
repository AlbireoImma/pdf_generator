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
# from models import * #Importar los modelos por aqui



class GeneratePDF(View):
    """docstring for GeneratePDF."""
    def get(self,request, *args, **kwargs):
        id_token = request.POST.get('token','')
        # Sacando datos necesarios de la Orden
        orden = OrdenCompra.objects.filter(token=id_token)
        cant_cuotas = orden.cantidad_cuotas
        monto_total = orden.monto_orden
        tipo_pago = orden.tipo_pago
        fecha_doc = orden.fecha_orden.date.strftime("%d/%m/%y")
        time_trans = orden.fecha_orden.date.strftime("%H:%M")
        nro_tarjeta = orden.nro_tarjeta
        num_orden = orden.id
        # Obteniendo nro de contrato
        contrato = Contratos.objects.filter(id=contrato_id)
        num_cont = contrato.numero_contrato
        # Obteniendo Datos Cliente
        cliente = Clientes.objects.filter(id=orden.cliente_id)
        nombre = cliente.nombre
        fst_ape = cliente.apellido_paterno
        scd_ape = cliente.apellido_materno
        name = nombre + " " + fst_ape + " " + scd_ape
        rut = cliente.rut
        # Obteniendo Datos de las Coutas
        cuotas = DetalleOrden.objects.filter(orden=orden.id)
        dict_cuotas = dict()
        i = 1
        for a in cuotas:
            dict_cuotas[i] = {
                "nro":i,
                "cuota_id":a.cuota_id,
                "fecha_cuota":a.fecha_cuota.date.strftime("%d/%m/%y"),
                "monto":a.monto
            }
            i = i + 1
        # Armando diccionario de las Cuotas
        template = get_template('invoice.html')
        context = {
            "name": name,
            "rut": rut,
            "doc_date": fecha_doc,
            "num_contrato": num_cont,
            "time_trans": time_trans,
            "num_orden": num_orden,
            "name_bank": "nombre_banco",
            "monto": monto_total,
            "nro_tarjeta": nro_tarjeta,
            "tipo_pago": tipo_pago,
            "cant_cuotas": cant_cuotas,
            "vars": dict_cuotas
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


