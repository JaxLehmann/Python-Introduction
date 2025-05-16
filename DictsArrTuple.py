map = {"a": 1, "b" : 2}
print(map.get("a"))
print ("c" in map)
map["b"] = 3
del map["b"]
map["d"] = 2
map["d"] = 4
map["f"] = 5
for k, v in map.items():
    print (k, "->", v)