from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader


@login_required
def get_home_page(request):
    # template = loader.get_template('agreements.html')
    # return HttpResponse(template.render({'agreements': []}, request))
    return HttpResponseRedirect('/admin/')
