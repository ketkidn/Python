import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb=myclient["MyFirstMongo"]
mycol=mydb["Employee"]
mydict={"name": "John", "address":"USA"}
x= mycol.insert_one(mydict)
print(x)
