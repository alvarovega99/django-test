from django.http import JsonResponse

class ResponseDto:
    def __init__(self, status=200, message="OK", data=None):
        self.status = status
        self.message = message
        self.data = data or {}
    
    def to_json(self):
        return JsonResponse({
            'status': self.status,
            'message': self.message,
            'data': self.data
        })