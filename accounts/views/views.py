from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from auth_backend import JWTBackend, BaseSurveyAdminManager
from accounts.models import SurveyAdmin
from rest_framework.views import APIView
from accounts.repository import SurveyAdminRepository
from auth_backend.backends import JWTBackend, login_admin
from accounts.serializers import SurveyAdminSerializer
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, GenericAPIView
from accounts.serializers import SurveyAdminSerializer
# from django.
# Create your views here.


sa_repo = SurveyAdminRepository


class RegisterView(APIView):
    parser_classes = [FormParser]
    
    serializer_class = SurveyAdminSerializer
    
    def get(self, request, *args, **kwargs):
        return render(request, "sa_register.html")
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                username = serializer.validated_data.get('username')
                password = serializer.validated_data.get('password')
                confirm_password = serializer.validated_data.get('confirm_password')
                
                
                if sa_repo.get_by_username(username) is not None:
                    context = {"message": "username already"}
                    return render(request, "htmx_components/error_message.html", context)
            
                if not (password == confirm_password):
                    context = {"message": "password not matching"}
                    return render(request, "htmx_components/error_message.html", context)
        
        except ValidationError as ve:
            print(ve.detail)
            context = {"message": ve.default_detail}
            return render(request, "htmx_components/error_message.html", context)
    

# def signup(request: HttpRequest) -> HttpResponse:
#     print(request.COOKIES)
#     request.COOKIES["auth"] = "jsjsj"
#     if request.method == "POST":


#       
#         try:
#          
            
#             BaseSurveyAdminManager.create_survey_admin(username=username, password=password)
#             survey_admin = JWTBackend.authenticate(
#                                     request=request,
#                                     username=username,
#                                     password=password
#                                     )
            
#             if survey_admin is not None:
#                 login_admin(request, survey_admin)
            
#             print("ssd", request.session.get("auth_session"))
#             response = HttpResponse()
#             response.set_cookie('auth_session', request.session.get("auth_session"))
#             response['HX-Redirect'] = f'/sa/sa-dashboard/'
#             # return render(request, 'sa_dashboard.html')
#             return redirect()
        
#         except Exception as ec:
#             print(ec)
#             context = {"message": "Error occured"}
#             return render(request, "htmx_components/error_message.html", context)
        
#     return render(request, "sa_register.html")


class LoginView(APIView):
    def get(self, request, *args, **kwargs):
        
        return render(request, "sa_login.html")




    



