from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json, logging, os
from pymongo import MongoClient

mongo_uri = 'mongodb://' + os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]
db = MongoClient(mongo_uri)['test_db']

class TodoListView(APIView):

    def get(self, request):
        todos = db['todo_collection'].find()

        todo_list=[]
        for todo in todos:
            todo_list.append(todo['todo'])
 
        return Response(todo_list, status=status.HTTP_200_OK)
        
    def post(self, request): 
        data = request.data
        result = db['todo_collection'].insert_one(data)
        return Response({"id": str(result.inserted_id)}, status=status.HTTP_201_CREATED)
    