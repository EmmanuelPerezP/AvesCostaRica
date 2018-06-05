from rest_framework import serializers
from .models import Ave


class AveSerializer(serializers.ModelSerializer):
    # Implement ForeignKey Relations
    # http://www.django-rest-framework.org/api-guide/relations/
    class Meta:
        model = Ave
        fields = ('clase', 'orden', 'familia', 'genero', 'name',
                  'mainImage', 'mainAudio', 'description', 'dateCreated',
                  'dateModified')
