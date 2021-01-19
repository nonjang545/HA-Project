import requests
import json

def formatjson(url):
    temp = requests.get(url).text
    return json.loads(temp)


food = input("What did you eat?: ")

foodDataJson = formatjson('https://api.nal.usda.gov/fdc/v1/foods/search?api_key=heumVFa25DPieTnd2d6xKf63BAw4olMHxnVQL81f&query='+food)
fdcId = foodDataJson["foods"][0]["fdcId"]
foodServingJson = formatjson('https://api.nal.usda.gov/fdc/v1/food/'+str(fdcId)+'?api_key=heumVFa25DPieTnd2d6xKf63BAw4olMHxnVQL81f')
if not foodServingJson["foodPortions"]:
    servingSizeGram = str(foodServingJson["servingSize"])+str(foodServingJson["servingSizeUnit"])
    servingSizeMod = foodServingJson["householdServingFullText"]
else:    
    servingSizeGram = str(foodServingJson["foodPortions"][0]["gramWeight"])
    servingSizeMod = "1 " + foodServingJson["foodPortions"][0]["modifier"]

print(food + "'s serving size: "+servingSizeMod + "\n"+food+"'s weight per serving: " + servingSizeGram+" grams")
#calories = str(result['parsed'][0]['food']['nutrients']['ENERC_KCAL'])

#print('The calorie of the '+food+' is '+calories +'kcal')
#print('The calorie of the '+food+)
