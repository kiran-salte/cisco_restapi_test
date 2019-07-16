import json, urllib.request

mac_address = input("Please enter the mac address you want to search? \n" )


def get_companyName(mac_address):
    url = 'https://api.macaddress.io/v1?apiKey=at_UYcaOE3IiHyoPnM2f3mPEDFiYFB3b&output=json&search=' + mac_address
    resp = urllib.request.urlopen( url ).read()
    data = json.loads( resp )
    return data['vendorDetails']['companyName']


company_name = get_companyName( mac_address )
print("Company name associated with "+mac_address+" is "+company_name )


