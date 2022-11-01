from rest_framework.views import APIView
from django.http import JsonResponse




class SlackdeetView(APIView):

    def get(self, request):
        slackdeets = {"slackUsername": "Lee", "backend": True, "age": 27, "bio":"my name is lee, and i have just one goal here; becoming a finalist!"}
        #json_slackdeet = json.dumps(slackdeets, safe=False)
        return JsonResponse(slackdeets)