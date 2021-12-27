from django.db import models

# Create your models here.


class Technology(models.Model):
    # id = models.AutoField()
    name = models.CharField(default="Technology",max_length=255)
    sub_domain = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.sub_domain


class TechnologyKPI(models.Model):
    kpi_name = models.CharField(max_length=255)
    parent = models.ForeignKey(Technology, to_field='sub_domain', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    storage_type_name = models.CharField(max_length=255)
    storage_type_cost = models.IntegerField(default=0)
    other_cost = models.IntegerField(default=0)

    def __str__(self):
        return self.kpi_name







