info = {

    "name" : "rajat",
    "cgpa" : 8.9,
    "marks": [87 , 98 ,88],
    "subject" :{
        "maths": 97,
        "phy" : 98,
        "chem" : 78,
    }

}
 
info["name"] = "nakul"
info["surname"] = "sharma"

print(list(info.keys()))

print(info.values())

print(list(info.items()))

print(info.get("name"))

info.update({"city" : "INDORE"})

print(info)

# print(info["subject"]["maths "])