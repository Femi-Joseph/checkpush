from django.http.response import ResponseHeaders
from io import BytesIO,StringIO


from django.http import HttpResponse
from django.template.loader import get_template
from app1.models import *
from django.contrib.staticfiles import finders
import os


from xhtml2pdf import pisa
from xhtml2pdf.document import pisaDocument
from django.core.files.base import ContentFile,File
from django.conf import settings
from django.http import response

def link_callback(uri,rel):
    sUrl=settings.STATIC_URL
    sRoot=settings.STATIC_ROOT
    mUrl=settings.MEDIA_URL
    mRoot=settings.MEDIA_ROOT

    if uri.startswith(mUrl):
        print("muri checking")
        path=os.path.join(mRoot,uri.replace(mUrl,""))
    else:
        return uri
    return path
    '''elif uri.startswith(sUrl):
        print("surl checking")
       
        path=os.path.join(sRoot,uri.replace(sUrl,""))
        print('path=',path)'''
    
        

    

def render_to_pdf(id,template_src,context_dict={}):
    template=get_template(template_src)
    html=template.render(context_dict)
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result,link_callback=link_callback)
    print("cheking pdf")
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='applications/pdf')

    return None


