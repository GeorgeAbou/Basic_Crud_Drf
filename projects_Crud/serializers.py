from rest_framework import serializers
from .models import Projects

#serializer
class  ProjectSerializer(serializers.ModelSerializer):# por cada modelo,convierte el modelo en datos para consultarse

    class Meta:
        model=Projects
        fields=('id','title','description','technology')
        read_only_fields=('createt_At',)#tiene q ser tupla


   