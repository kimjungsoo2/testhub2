from django.db import models

# Create your models here.
class Primarydomain(models.Model):
    name = models.CharField(max_length=128, unique=True)
    
    def __unicode__(self):
        return self.name
    
class Secondarydomain(models.Model):
    primary = models.ForeignKey(Primarydomain)
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name
    
class Component(models.Model):
    secondary = models.ForeignKey(Secondarydomain)
    name = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.name
    
class Testplan(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __unicode__(self):
        return self.name
    
    
class Testcase(models.Model):
    Resolution_ID = models.IntegerField(null=True)
    Due = models.DateTimeField(null=True)
    Priority = models.IntegerField(null=True)
    Type = models.CharField(max_length=255)
    Secondary_domain_name = models.CharField(max_length=255)
    Status = models.CharField(max_length=255)
    Updated = models.DateTimeField(null=True)
    Primary_domain_name = models.CharField(max_length=255)
    Primary_domain_key = models.ForeignKey(Primarydomain)
    Regression_Level = models.CharField(null=True, max_length=255)
    Reporter = models.CharField(max_length=255)
    Project_Key = models.CharField(max_length=255)
    Status_ID = models.IntegerField(null=True)
    Key = models.CharField(max_length=255, unique=True)
    Num = models.IntegerField(null=True)
    Project_ID = models.IntegerField(null=True)
    Requirements_Traceability = models.TextField(null=True)
    Created = models.DateTimeField(null=True)
    Summary = models.TextField(null=True)
    Type_ID = models.IntegerField(null=True)
    Component_ID = models.TextField(null=True)
    Resolution = models.CharField(null=True, max_length=255)
    Description = models.TextField(null=True)
    Project = models.CharField(max_length=255)
    Labels = models.TextField(null=True)
    Assignee = models.CharField(null=True, max_length=255)
    Components = models.TextField(null=True)
    
    def __unicode__(self):
        return self.Key
    
class TestExecution(models.Model):
    Test_Case_ID = models.CharField(null=True, max_length=255)
    Resolution_ID = models.CharField(null=True, max_length=255)
    Due = models.CharField(null=True, max_length=255)
    Priority = models.CharField(null=True, max_length=255)
    Type = models.CharField(null=True, max_length=255)
    Status = models.CharField(null=True, max_length=255)
    Updated = models.DateTimeField(null=True)
    #Component_ID = models.TextField()
    Description = models.TextField(null=True)
    Reporter = models.CharField(null=True, max_length=255)
    Project_Key = models.CharField(null=True, max_length=255)
    Status_ID = models.IntegerField(null=True)
    Test_Plan_CR = models.CharField(null=True, max_length=255)
    Test_Plan_Key = models.ForeignKey(Testplan)
    Key = models.CharField(max_length=255, unique=True)
    Project_ID = models.IntegerField(null=True)
    Created = models.DateTimeField(null=True)
    Remote_Defect_CR = models.CharField(null=True, max_length=255)
    Summary = models.TextField(null=True)
    TypeID = models.IntegerField(null=True)
    Resolution = models.CharField(null=True, max_length=255)
    Project = models.CharField(null=True, max_length=255)
    Labels = models.CharField(null=True, max_length=255)
    Assignee = models.CharField(null=True, max_length=255)
    Components = models.CharField(max_length=255, null=True)
    Test_Results = models.CharField(null=True, max_length=255)
    
    def __unicode__(self):
        #return self.Key
        #return self
        return unicode(self.Key) or u''
    
