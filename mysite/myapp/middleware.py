class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # process before
        print(f"Middleware Req Path:{request.path}")
        response = self.get_response(request)
        # process after
        print(f"Middle Res status:{response.status_code}")
        return response