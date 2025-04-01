import RestClient

turListe,response = RestClient.GetAll()
print("Status code = ", str(response.status_code))
for t in turListe:
    print(f"Tur nr:{t['id']} navn={t['name']} dato={t['dato']} distance={t['distance']}")


nyTur = dict(id = 4, name = "Peter", dato= "010425", distance= 1)
tur,response = RestClient.Add(nyTur)
print("Status code = ", str(response.status_code))
print(f"Tur nr:{tur['id']} navn={tur['name']} dato={tur['dato']} distance={tur['distance']}")