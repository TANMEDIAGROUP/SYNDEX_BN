from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import UserModel
from .serializer import UserSerialize
from api.src.middleware.cloud import  handleFileActions

@api_view(['GET'])
def root(request):
    data = {"data":"null","message": "root","status":"success"}
    return Response(data,status="200")

@api_view(['GET'])
def getUsers(request):
 try:
    user=UserModel.objects.all()
    serialize=UserSerialize(user,many=True)
    return Response(serialize.data,status="200")
 except Exception as e:
    return Response({"error":str(e),"status":"failed" },status="500")

@api_view(['POST'])
def createUsers(request):
 try :
    request.POST._mutable=True
    body=request.POST
    user=UserSerialize(data=body,partial=True)
    if(user.is_valid()):
        img_src=handleFileActions(request.FILES)
        body['avatar']= img_src if img_src!=False else "N/A"
        data=UserSerialize(data=body)
        if data.is_valid():
            data.save()
        return Response({"user":body,"message": "root","status":"success"})
    else:
     return Response({"errors":user.errors,"status":"failed"},status="400")
 except Exception as e:
      return Response({"errors":str(e),"message": "error","status":"failed"},status="500")
 

@api_view(["DELETE"])
def deleteUsers():
   pass