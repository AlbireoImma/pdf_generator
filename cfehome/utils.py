from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    nro = context_dict["num_cont"]
    fecha = context_dict["doc_date"]
    fecha2 = fecha.replace("/","-")
    if not pdf.err:
        pdf_file = open("pdfs/"+str(nro)+"_"+str(fecha2)+".pdf","wb")
        pdf2 = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),pdf_file)
        pdf_file.close()
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
