from operator import mod
from django.db import models

class Member(models.Model):
    id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    interview_time= models.DateTimeField()
    is_interviewed= models.BooleanField()

    C= models.IntegerField()
    CPP= models.IntegerField()
    CHash= models.IntegerField()
    Java= models.IntegerField()
    Python= models.IntegerField()
    
    Git= models.IntegerField()
    OpenCV= models.IntegerField()
    Arduino= models.IntegerField()

    other_micro_controllers= models.CharField(max_length=100, null=True)
    
    image_processing= models.IntegerField()
    machine_learning= models.IntegerField()
    communication= models.IntegerField()
    
    data_structures= models.IntegerField()
    algorithms= models.IntegerField()
    
    PCB_design_eagle= models.IntegerField()
    PCB_design_altium= models.IntegerField()
    PCB_design_proteus= models.IntegerField()
    
    PCB_manufacture_single= models.IntegerField()
    PCB_manufacture_double= models.IntegerField()
    SMD= models.IntegerField()
    
    projects= models.CharField(max_length=200,  null=True)
    sensors_knowledge= models.CharField(max_length=200, null=True)
    GUI= models.BooleanField()


    def add_member(dict):
        print(dict['GUI'])
        member= Member(
            name=dict['name'], interview_time=dict['interview_time'], is_interviewed= False,
            C=dict['C'], CPP= dict['CPP'], CHash= dict['CHash'], Java= dict['Java'], Git= dict['Git'],
            OpenCV= dict['OpenCV'], Arduino= dict['Arduino'], other_micro_controllers= dict['other_micro_controllers'],
            image_processing= dict['image_processing'], machine_learning= dict['machine_learning'], communication= dict['communication'],
            data_structures= dict['data_structures'], algorithms= dict['algorithms'],
            PCB_design_eagle= dict['PCB_design_eagle'], PCB_design_altium= dict['PCB_design_altium'], PCB_design_proteus= dict['PCB_design_proteus'],
            PCB_manufacture_single= dict['PCB_manufacture_single'], PCB_manufacture_double= dict['PCB_manufacture_double'], SMD= dict['SMD'],
            projects= dict['projects'], sensors_knowledge= dict['sensors_knowledge'], GUI= dict['GUI'], Python=True
            )
        member.save()
        return True

    def set_interviewed(id):
        member=Member.objects.all().get(id=id)
        member.is_interviewed= True
        member.save()



class Comment(models.Model):
    member_id= models.ForeignKey(Member, on_delete=models.CASCADE)
    comment= models.CharField(max_length=100)

    def addComment(id, comment):
        member= Member.objects.get(id=id)
        member.comment_set.create(comment=comment)
    
    
    
    

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)