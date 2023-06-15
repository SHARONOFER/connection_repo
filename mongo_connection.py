import pymongo
import json
# Set up the MongoDB connection string
connection_string = "mongodb://localhost:27017/"

# Connect to the MongoDB server
client = pymongo.MongoClient(connection_string)

# Access a specific database
database = client["testdb"]

# Access a specific collection within the database
collection = database["users"]

# Now you can perform operations on the collection
# For example, you can insert a document
document = {"usrname": "dba5"}
collection.insert_one(document)



#select data from mongo  table name users 
collection = database["users"]

#brinf first record
x = collection.find_one()


# add where  clause
query = {'usrname': 'dba5'}


documents = collection.find(query)

#documents.limit (10)

print (type(documents) )

# Print each document
for document in documents:
    print(document)



# Remember to close the connection when you're done
client.close()