from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes


@api_view(['POST'])
def search(request):
    data = request.data
    query = data['query']

    print('query', query)

    return JsonResponse({'asdffds': 'asdfws'})
