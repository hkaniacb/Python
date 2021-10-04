import xml.etree.ElementTree as ET
import zeep as soap
import requests


wsdl = r"http://www.dneonline.com/calculator.asmx?wsdl"
a,b = 5,3
client = soap.Client(wsdl = wsdl)
#Method Add
response = client.service.Add(a,b)
print("Result Add:", response)
#Method Devide
response = client.service.Divide(a,b)
print("Result devide", response)
#Method Multiply
response = client.service.Multiply(a,b)
print("Result multiply:",response)

ns = {"soap": "http://schemas.xmlsoap.org/soap/envelope/",
      "a": "http://tempuri.org/"}

def method_add(message):
    root = ET.fromstring(message)
    result = root.find("./soap:Body/a:AddResponse/a:AddResult", namespaces=ns)
    return result.text

def method_multiply(message):
    root = ET.fromstring(message)
    #result = root.find("./soap:Body/a:MultiplyResponse/a:MultiplyResult", namespaces=ns)
    result = root.find(".//a:MultiplyResult", namespaces=ns)
    return result.text




headers = {"content-type":"text/xml"}
add_body = f"""
      <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
       <soapenv:Header/>
       <soapenv:Body>
          <tem:Add>
             <tem:intA>{a}</tem:intA>
             <tem:intB>{b}</tem:intB>
          </tem:Add>
       </soapenv:Body>
     </soapenv:Envelope>
"""

multiply_body = f"""
      <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
          <soapenv:Header/>
           <soapenv:Body>
              <tem:Multiply>
                 <tem:intA>{a}</tem:intA>
                 <tem:intB>{b}</tem:intB>
              </tem:Multiply>
           </soapenv:Body>
     </soapenv:Envelope>
"""

response = requests.post(url=wsdl, headers=headers, data=add_body)
print("Requests method ADD:", method_add(response.text))
response = requests.post(url=wsdl, headers=headers, data=multiply_body)
print("Requests method MULTIPLY:", method_multiply(response.text))


class ApiCalculator:

    headers = {"content-type":"text/xml"}
    def __init__(self, url):
        self.url = url

    def add(self, a, b):
        def _add(message):
            root = ET.fromstring(message)
            result = root.find("./soap:Body/a:AddResponse/a:AddResult", namespaces=ns)
            return result.text
        post_data = f"""
          <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
           <soapenv:Header/>
           <soapenv:Body>
              <tem:Add>
                 <tem:intA>{a}</tem:intA>
                 <tem:intB>{b}</tem:intB>
              </tem:Add>
           </soapenv:Body>
         </soapenv:Envelope>
        """
        response = requests.post(url=self.url, headers=self.headers, data=post_data)
        return int(_add(response.text))

    def multiply(self, a, b):
        def _multiply(message):
            root = ET.fromstring(message)
            result = root.find("./soap:Body/a:MultiplyResponse/a:MultiplyResult", namespaces=ns)
            return result.text
        post_data = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
          <soapenv:Header/>
           <soapenv:Body>
              <tem:Multiply>
                 <tem:intA>{a}</tem:intA>
                 <tem:intB>{b}</tem:intB>
              </tem:Multiply>
           </soapenv:Body>
         </soapenv:Envelope>"""
        response = requests.post(self.url, headers=self.headers, data=post_data)
        return int(_multiply(response.text))
