import json
from django.http import JsonResponse

# Create your views here.
def api_home(request):
    # print(request.GET)
    
    body  = request.body
    # print(request.GET)
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content-type'] = request.content_type

    return JsonResponse(data)