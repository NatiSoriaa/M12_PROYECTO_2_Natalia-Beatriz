#API KEY

from flask import request, jsonify

api_keys = {
    "usuario1" : "123"
}
def validarApiKey(request):
    api_key = request.headers.get('x-api-key')

    if not api_key:
        return False
    
    if api_key in api_keys.values():
        return True
    
    else:
        return False

