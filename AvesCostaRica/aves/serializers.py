from rest_framework import serializers
from .models import Ave, Clase, Orden, Familia, Genero, Especie


class AveSerializer(serializers.ModelSerializer):
    # Implement ForeignKey Relations
    # http://www.django-rest-framework.org/api-guide/relations/
    class Meta:
        model = Ave
        fields = ('id', 'clase', 'orden', 'familia', 'genero', 'especie', 'name',
                  'mainImage', 'mainAudio', 'description', 'dateCreated',
                  'dateModified')


class ClaseSerializer(serializers.ModelSerializer):
    # Implement ForeignKey Relations
    # http://www.django-rest-framework.org/api-guide/relations/
    class Meta:
        model = Clase
        fields = ('id', 'name', 'dateCreated', 'dateModified')


class OrdenSerializer(serializers.ModelSerializer):
    # Implement ForeignKey Relations
    # http://www.django-rest-framework.org/api-guide/relations/
    class Meta:
        model = Orden
        fields = ('id', 'name', 'dateCreated', 'dateModified')


class FamiliaSerializer(serializers.ModelSerializer):
    # Implement ForeignKey Relations
    # http://www.django-rest-framework.org/api-guide/relations/
    class Meta:
        model = Familia
        fields = ('id', 'name', 'dateCreated', 'dateModified')


class GeneroSerializer(serializers.ModelSerializer):
    # Implement ForeignKey Relations
    # http://www.django-rest-framework.org/api-guide/relations/
    class Meta:
        model = Genero
        fields = ('id', 'name', 'dateCreated', 'dateModified')


class EspecieSerializer(serializers.ModelSerializer):
    # Implement ForeignKey Relations
    # http://www.django-rest-framework.org/api-guide/relations/
    class Meta:
        model = Especie
        fields = ('id', 'name', 'dateCreated', 'dateModified')
