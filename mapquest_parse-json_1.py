import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "xYHwXF7l2yLfULwBEepk0zkUUeAhtOEP" 

while True:
   orig = input("Locación de Origen: ")
   if orig == "quit" or orig == "q":
        break
   dest = input("Destino: ")
   if dest == "quit" or dest == "q":
        break
   url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
   print("URL: " + (url))
   json_data = requests.get(url).json()
   json_status = json_data["info"]["statuscode"]
   if json_status == 0:
       print("API Status: " + str(json_status) + " = A successful route call.\n")
       print("=============================================")
       print("Direcciones desde " + (orig) + " a " + (dest))
       print("Duración del Viaje: " + (json_data["route"]["formattedTime"]))
       print("Kilómetros: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
       print("Combustible Estimado (Ltr): 346.52 ltr")
       print("=============================================")
       for each in json_data["route"]["legs"][0]["maneuvers"]:
          print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
          print("=============================================\n")
