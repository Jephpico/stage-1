from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.serializers import Serializer




class SlackdeetView(APIView):
    slackdeets = {"slackUsername": "Lee", "backend": True, "age": 27, "bio":"my name is lee, and i have just one goal here; becoming a finalist!"}

    def get(self, request):
        slackdeets = {"slackUsername": "Lee", "backend": True, "age": 29, "bio":"my name is lee, and i have just one goal here; becoming a finalist!"}
        #json_slackdeet = json.dumps(slackdeets, safe=False)
        return Response(slackdeets)
    def post(self, request):
    
            data = request.data

            op_type = data['operator_type']
            integer1 = int(data['x'])
            integer2 = int(data['y'])

            if op_type in ['addition', 'add', 'plus', '+', 'sum']:
                result = integer1+integer2

            elif op_type in ['subtraction', 'minus','-' ]:
                result = integer1-integer2
            
            elif op_type in ['multiplication', 'times', 'multiply', '*' ]:
                result = integer1*integer2
             
            else:
                 op_type = "invalid operation type"
                

            computed_data = {
                "slackUsername":"lee",
                "result": result,
                "operator_type": op_type
            }
            return Response(computed_data, status=status.HTTP_200_OK)



        
        

