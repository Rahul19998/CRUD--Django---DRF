from django.http.response import Http404
from rest_framework.views import APIView
from .models import Courses
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializer import CoursesSerializer
# Create your views here.


class CoursesListView(APIView):

    def get(self, request, format=None):
        # Return list of all courses.

        course = Courses.objects.all()
        serializer = CoursesSerializer(course, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CoursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CoursesView(APIView):

    def get_object(self, id):
        try:
            return Courses.objects.get(id=id)
        except Courses.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        # Return a course with particular id
        course = self.get_object(id)
        serializer = CoursesSerializer(course)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        course = self.get_object(id)
        serializer = CoursesSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        course = self.get_object(id)
        # serializer = CoursesSerializer(course)
        course.delete()
        return Response({"message": "The specified course was deleted"}, status=status.HTTP_200_OK)
