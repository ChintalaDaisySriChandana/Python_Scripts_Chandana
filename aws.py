mydict={
"name":"John",
"id":17,
"domain":["DevOps", "Cloud Engineer", "SRE"],
"tools": {"os":["Linux", "Windows"],"cloud":["AWS"]}
}

print(mydict)
print(mydict["name"])
print(mydict["id"])
print(mydict["domain"])
print(mydict["tools"]["os"][1])
mydict["country"]= ["India", "NZ"]
mydict1={
"name1": "Doe",
"id1":112
}
mydict.update(mydict1)
print(mydict)

