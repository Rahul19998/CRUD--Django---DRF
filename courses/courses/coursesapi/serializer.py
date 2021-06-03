from coursesapi.models import Courses
from rest_framework import serializers


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'date_created', 'date_updated', 'description',
                  'image_path', 'on_discount', 'price', 'title']
        extra_kwargs = {
            "title": {
                "validators": [],
            },
        }
