from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def main(request):
    context = RequestContext(request)
    context_dict = {}
    
    return render_to_response('dashboard/base.html', context)