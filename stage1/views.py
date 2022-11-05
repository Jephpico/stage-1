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
        try:
            data = request.data

            operator_type = data['operator_type']
            integer1 = data['x']
            integer2 = data['y']
            slackname = 'lee'
            if operator_type == 'addition':
                result = integer1 + integer2
                deet = {}
                deet['result']= result
                deet['operation_type'] = operator_type
                deet['slackUsername'] = 'Lee'
                return Response(deet)


            elif operator_type == 'subtraction':
                result = integer1 - integer2
                deet = {}
                deet['result']= result
                deet['operation_type'] = operator_type
                deet['slackUsername'] = 'Lee'
                return Response(deet)
            else:
                operator_type == 'multiplication'
                result = integer1 * integer2
                deet = {}
                deet['result']= result
                deet['operation_type'] = operator_type
                deet['slackUsername'] = 'Lee'
                return Response(deet)
        except: raise Exception

        
        

