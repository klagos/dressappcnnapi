from rest_framework import serializers 
from tutorials.models import Tutorial, Image
 
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id',
                  'tipo',
                  'color',
                  'created_at') 

class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')