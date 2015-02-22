from django.shortcuts import render
from django.db.models import Q

from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

from disclosures.models import Disclosure

def index(request):
    return render_to_response("index.html", None, RequestContext(request))

def search(request):
    query = request.REQUEST['q']

    context = {'query': query}
    if query:
        results = Disclosure.objects.filter(Q(title__icontains=query) |
                                            Q(abstract__icontains=query) |
                                            Q(body__icontains=query))

        context['results'] = results


    return render_to_response("search.html", context, RequestContext(request))

def faq(request):
    return render_to_response("faq.html", None, RequestContext(request))
