import pymongo


class Documents:
    client = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = client["schools"]
    mycol = mydb["schools_list"]


class MongoClient(Documents):
    def __init__(self):
        self.__model = Documents

    def find_one(self):
        documents = self.__model.mycol.find_one()
        return print(documents)

    def find_chosen_one(self, document):
        documents = self.__model.mycol.find_one(document)
        return print(documents)

    def find_all(self):
        documents = self.__model.mycol.find()
        for value in documents:
            print(value)
        return documents

    def insert_one(self, document):
        documents = self.__model.mycol.insert_one(document)
        return documents, print("inserted")

    def insert_many(self, document):
        documents = self.__model.mycol.insert_many(document)
        return documents, print("inserted")

    def update(self, document, updated_document):
        documents = self.__model.mycol.update_one(document, {"$set": updated_document})
        return documents, print("updated")

    def sort_by(self, value):
        documents = self.__model.mycol.find().sort(value)
        for value in documents:
            print(value)
        return documents

    def delete(self, document):
        documents = self.__model.mycol.delete_one(document)
        return documents, print("deleted")



