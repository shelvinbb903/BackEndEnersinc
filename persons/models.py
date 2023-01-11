from django.db import models
        
        
class DocumentTypeModel(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=12)
    
    class Meta:
        db_table = 'document_type_tb'

class PersonsModel(models.Model):
    id = models.AutoField(primary_key=True)
    document = models.CharField(max_length=12)
    document_type = models.ForeignKey(DocumentTypeModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    hobbie = models.CharField(max_length=500)
        
    class Meta:
        db_table = 'persons_tb'