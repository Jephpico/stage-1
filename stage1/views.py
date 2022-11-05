from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.serializers import Serializer




class SlackdeetView(APIView):
    slackdeets = {"slackUsername": "Lee", "backend": True, "age": 27, "bio":"my name is lee, and i have just one goal here; becoming a finalist!"}

    def get(self, request):
        slackdeets = {"slackUsername": "Lee", "backend": True, "age": 27, "bio":"my name is lee, and i have just one goal here; becoming a finalist!"}
        #json_slackdeet = json.dumps(slackdeets, safe=False)
        return JsonResponse(slackdeets)
    def post(self, request):

            data = request.data

            operator_type = data['operator_type']
            integer1 = data["x"]
            integer2 = data["y"]
            if operator_type == ('addition', 'add', 'plus', '+', 'sum'):
                result = integer1 + integer2
                deet = {}
                deet['slackUsername'] = 'Lee'
                deet['result']= result
                deet['operation_type'] = operator_type
                return Response(deet)


            elif operator_type == ('subtraction', 'minus','-' ):
                result = integer1 - integer2
                deet = {}
                deet['slackUsername'] = 'Lee'
                deet['result']= result
                deet['operation_type'] = operator_type
                return Response(deet)

            else:
                operator_type == ('multiplication', 'times', 'multiply', '*' , 'x', 'X')
                result = integer1 * integer2
                deet = {}
                deet['slackUsername'] = 'Lee'
                deet['result']= result
                deet['operation_type'] = operator_type
                return Response(deet)

        
        

