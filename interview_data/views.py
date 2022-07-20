from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Member, Comment


def index(request):
    not_interviewed_members= Member.objects.filter(is_interviewed= 0)
    interviewed_members= Member.objects.filter(is_interviewed= 1)
    
    return HttpResponse(render(request, 'interview_data/index.html', {'not_members': not_interviewed_members, 'members':interviewed_members}))

def addMember(request):
    return HttpResponse(render(request, 'interview_data/addMember.html'))

def post_member(request):
    print(request.POST.dict)
    Member.add_member(request.POST)
    return HttpResponseRedirect(reverse('add_member'))

def memberDetail(request, id):
    member= Member.objects.get(id=id)
    comments= member.comment_set.all()
    return HttpResponse(render(request, 'interview_data/detail.html', {'member': member, 'comments':comments}))

def addComment(request, idd):
    Comment.addComment(idd, request.POST['comment'])
    return HttpResponseRedirect(reverse('detail', args=(idd,)))

def interviewDone(request, id):
    Member.set_interviewed(id)
    return HttpResponseRedirect(reverse('index'))


