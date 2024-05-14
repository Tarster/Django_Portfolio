from ninja import NinjaAPI
from ninja.security import django_auth
api = NinjaAPI(csrf=True)

@api.get("/hello",auth=django_auth)
def hello(request, name:str="something"):
    return f"Hello {name}"

