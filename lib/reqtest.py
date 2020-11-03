import requests
from lib.core.attrDict import var

# class reqtest:
#     def __init__(self):
#         self.url = var.URL
#         self.payload = var.PAYLOAD
#     def req(self,payload):
#         proxy = {'http':'http://127.0.0.1:8080'}
#         var.PARAM[var.INJERP] =var.PAYLOAD.format(payload)
#         if var.METHOD == 'get':
#             r = requests.get(url = var.URL,params=var.PARAM)
#         else:
#             r = requests.post(url=var.URL,data=var.PARAM)
#         return r