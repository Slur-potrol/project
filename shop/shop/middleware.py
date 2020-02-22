import json


class LastQuestion:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.headers['content-type'] == 'application/json':
            data = json.loads(request.body)
            request.POST = data

        response = self.get_response(request)

        return response