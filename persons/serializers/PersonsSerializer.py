from persons.models import PersonsModel, DocumentTypeModel
from rest_framework import serializers
from persons.serializers.DocumentTypeSerializer import ListDocumentTypeSerializer

class PersonsSerializer(serializers.Serializer):
    document = serializers.CharField(max_length=12)
    document_type = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    hobbie = serializers.CharField(max_length=500)

    """ Validar existencia del documento """
    def validate_document(self, value):
        person_data = PersonsModel.objects.filter(document=value)
            
        if person_data.__len__() > 0:                
            raise serializers.ValidationError("Document exists")
        
        return value
    
    def create(self, validated_data):
        document_type_data = DocumentTypeModel.objects.get(id=validated_data["document_type"])
        validated_data["document_type"] = document_type_data;
        person = PersonsModel.objects.create(**validated_data)
        return person 
    
    class Meta:
        model = PersonsModel
        fields = ['id', 'document', 'document_type', 'name', 'last_name', 'hobbie']
    
class UpdatePersonSerializer(serializers.Serializer):
    document = serializers.CharField(max_length=12)
    document_type = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    hobbie = serializers.CharField(max_length=500)
    
    def update(self, instance, validated_data):
        document_type_data = DocumentTypeModel.objects.get(id=validated_data.get('document_type', instance.document_type))
        instance.document_type = document_type_data;
        instance.document = validated_data.get('document', instance.document)
        instance.document_type = document_type_data
        instance.name = validated_data.get('name', instance.name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.hobbie = validated_data.get('hobbie', instance.hobbie)
        instance.save()
        return instance

class DeletePersonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    
    def delete(self, instance):
        instance.delete()

class ListPersonsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    document = serializers.CharField(max_length=12)
    document_type = ListDocumentTypeSerializer(read_only=True);
    name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    hobbie = serializers.CharField(max_length=500)
    
    class Meta:
        model = PersonsModel
        fields = ['id', 'document', 'document_type', 'name', 'last_name', 'hobbie']