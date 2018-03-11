from rest_framework import serializers
from .models import Ave


class AveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ave
        fields = ('clase', 'orden', 'suborden', 'familia', 'genero', 'name',
                  'mainImage', 'description', 'dateCreated', 'dateModified')
