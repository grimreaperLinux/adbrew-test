from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import MongoTodoService

class TodoListView(APIView):

    def get(self, request):
        todo_service = MongoTodoService()
        todo_list = todo_service.get_all_todos()
        return Response(todo_list, status=status.HTTP_200_OK)

    def post(self, request):
        todo_service = MongoTodoService()
        data = request.data
        result = todo_service.create_todo(data)
        return Response({"id": str(result.inserted_id)}, status=status.HTTP_201_CREATED)