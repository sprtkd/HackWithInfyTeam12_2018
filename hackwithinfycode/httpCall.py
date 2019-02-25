import json
import urllib.request


def fetchBasicDetails(prodID):
    url_string = "http://192.168.43.107:5002/Sample/"
    contents = urllib.request.urlopen(url_string+prodID).read()
    contents = contents.decode("utf-8")
    contents = json.loads(contents)
    contents = json.loads(contents)
    #print(contents,"\n\n")
    return contents
    

def FormatBasicData(prodID):
    basic_data = fetchBasicDetails(prodID)
    stringData = basic_data['Title'] + '     ('+basic_data['Product Type']+')'+'\n'
    stringData = stringData + basic_data['Company'] + '             '+basic_data['Weight']+'\n\n'
    stringData = stringData + basic_data['Description'] + '\n\n'
    stringData = stringData + 'Shelf Life: ' + basic_data['Shelf Life'] + '\n'
    return stringData


#print(FormatBasicData("890121"))
