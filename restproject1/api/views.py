from django.shortcuts import render
from django.http import HttpResponse
import json
import xml.etree.ElementTree as ET

# Create your views here.
def text_output(request):
    msg = "<h1> This is text message</h1>"
    response=HttpResponse(msg,content_type="text/plan")
    return response

def html_output(request):
    response=HttpResponse()
    response.write("<p>This is Paragraph1</p>")
    response.write("<p>This is Paragraph2</p>")
    return response

def header_output(request):
    response=HttpResponse()
    response['Age']=40
    return response

def attach_output(request):
    msg="Attachment"
    response =HttpResponse('msg',headers={"Content-Type":"application/vnd.microsoft", "Content-Disposition": 'attachment; filename="Book1.xlsx"'})
    return response

def json_output(request):
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }
    response = HttpResponse(json.dumps(data), content_type='text/json')
    return response

def xml_output(request):
    root = ET.Element("root")
    person = ET.SubElement(root, "person")
    name = ET.SubElement(person, "name").text = "John Doe"
    age = ET.SubElement(person, "age").text = "30"
    city = ET.SubElement(person, "city").text = "New York"
    response = HttpResponse(ET.tostring(root, encoding='unicode'), content_type='text/xml')
    return response