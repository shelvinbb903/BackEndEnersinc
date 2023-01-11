from persons.models import DocumentTypeModel
from rest_framework import serializers

class ListDocumentTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    description = serializers.CharField(max_length=12)
    
    class Meta:
        model = DocumentTypeModel
        fields = ['id', 'description']