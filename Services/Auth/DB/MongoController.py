from pymongo import MongoClient

connection = MongoClient("mongodb+srv://Artyom:Artyom30000@flamber-mongodb-pjxiq.mongodb.net/test?retryWrites=true")
db = connection["ServiceAuth"]