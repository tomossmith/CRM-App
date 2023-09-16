from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  clubmembers = Member.objects.all().values()
  template = loader.get_template('members.html')
  context = {
    'clubmembers': clubmembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  clubmembers = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'clubmembers': clubmembers,
  }
  return HttpResponse(template.render(context, request))