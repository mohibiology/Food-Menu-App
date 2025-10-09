import time
from django.http import HttpResponseForbidden

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
    
class TimerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        duration = time.time() - start
        print(f"Middleware req too {duration:.2f} seconds")
        return response

class BlockIPMiddleware:
    Blocked_IPs = [""]
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR")
        if ip in self.Blocked_IPs:
            return HttpResponseForbidden("Your IP is blocked")
        return self.get_response(request)