import os
from pymongo import MongoClient
from abc import ABC, abstractmethod

class TodoService(ABC):

    @abstractmethod
    def get_all_todos(self):
        pass

    @abstractmethod
    def create_todo(self, data):
        pass

class MongoTodoService(TodoService):
    def __init__(self):
        self.db = self._connect_to_mongodb()

    def _connect_to_mongodb(self):
        mongo_uri = 'mongodb://' + os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]
        return MongoClient(mongo_uri)['test_db']

    def get_all_todos(self):
        todos = self.db['todo_collection'].find()
        todo_list = [todo['todo'] for todo in todos]
        return todo_list

    def create_todo(self, data):
        result = self.db['todo_collection'].insert_one(data)
        return result