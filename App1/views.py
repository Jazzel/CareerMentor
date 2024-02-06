# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
import numpy as np
import joblib 
from knox.auth import TokenAuthentication
from django.db import transaction

from .models import Profile

#fun1 fun2 fun3 fun4 fun 5 fun 6 are just for understanding, they have no use in the actual proj

def fun1(request):
     return render (request,'HomePage.html')

def fun2(request):
     a=request.GET.get("a")
     b=request.GET.get("b")
     print(a)
     print(b)
     #return render (request,'Form.html')
     return render (request,'Form.html',{'Answer1':a,'Answer2':b})
   # str = "<h1 style = 'color: #663300' >Test Page</h1>"
    #return HttpResponse (str)

def fun3(request):
    return render (request,'About.html')	
    #return render (request,'test.html',{'MyValue':'My Website','MyValue2':'My Website'})

def fun4(request):
    return render (request,'Blogs.html')	

def fun5(request):
    return render (request,'Login.html')

def fun6(request):
    return render (request,'Register.html')


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        city = request.POST["city"]
        country = request.POST["country"]

        profile = Profile(user=user, city=city, country=country)
        profile.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

#Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

def marking(request):
    #dict={request}
    dict = request.GET.get('answers')   #Answer is the Dictionary coming from Frontend 

    for keys in dict:
        if keys in ['mbti-I/E-question1','mbti-I/E-question2','mbti-I/E-question3',
                    'mbti-I/E-question4','mbti-I/E-question5','mbti-I/E-question6',
                    'mbti-I/E-question7']:
            introvert += dict[keys]
        
        
        elif keys in ['mbti-S/N-question8','mbti-S/N-question9','mbti-S/N-question10',
                      'mbti-S/N-question11','mbti-S/N-question12','mbti-S/N-question13',
                      'mbti-S/N-question14']:
            sensing += dict[keys]
        

        elif keys in ['mbti-J/P-question15','mbti-J/P-question16','mbti-J/P-question17',
                      'mbti-J/P-question18','mbti-J/P-question19','mbti-J/P-question20',
                      'mbti-J/P-question21'] :
            Judging += dict[keys]
        

        elif keys in ['mbti-T/F-question22','mbti-T/F-question23','mbti-T/F-question24',
                      'mbti-T/F-question25','mbti-T/F-question26','mbti-T/F-question27',
                      'mbti-T/F-question28'] :
             Thinking += dict[keys]
        
        
        elif keys in ['mi-question9','mi-question10','mi-question11','mi-question12'] :
             logical_intelligence += dict[keys]
         
        
        elif keys in ['mi-question29','mi-question30','mi-question31','mi-question32'] :
             Nature_intelligence += dict[keys]
         
        
        elif keys in ['mi-question5','mi-question6','mi-question7','mi-question8'] :
             Visual_intelligence += dict[keys]
         
        
        elif keys in ['mi-question21','mi-question22','mi-question23','mi-question24'] :
              Musical_intelligence += dict[keys]
          
        
        elif keys in ['mi-question25','mi-question26','mi-question27','mi-question28'] :
              Body_intelligence += dict[keys]
          
        
        elif keys in ['mi-question13','mi-question14','mi-question15','mi-question16'] :
              Interpersonal_intelligence += dict[keys]
          
        
        elif keys in ['mi-question17','mi-question18','mi-question19','mi-question20'] :
              Intrapersonal_intelligence += dict[keys]
          
        
        elif keys in ['mi-question1','mi-question2','mi-question3','mi-question4'] :
              Verbal_intelligence += dict[keys]
          
        
        elif keys in ['mi-question33','mi-question34','mi-question35','mi-question36'] :
              Existential_intelligence += dict[keys]
          
        elif (keys == 'self_question1'):
            gender=dict[keys]

        elif (keys == 'self_question2'):
            income_group=dict[keys]

    introvert = introvert/7  
    sensing = sensing/7 
    Judging = Judging/7 
    Thinking =  Thinking/7

    logical_intelligence =  logical_intelligence/5
    Nature_intelligence =  Nature_intelligence/5
    Visual_intelligence =  Visual_intelligence/5
    Musical_intelligence =   Musical_intelligence/5
    Body_intelligence =   Body_intelligence/5
    Interpersonal_intelligence =   Interpersonal_intelligence/5
    Intrapersonal_intelligence =  Intrapersonal_intelligence/5
    Verbal_intelligence =  Verbal_intelligence/5
    Existential_intelligence =  Existential_intelligence/5

    X_TEST=np.array(gender,income_group,sensing,introvert,Judging,Thinking,
                    logical_intelligence,Nature_intelligence,Visual_intelligence,
                    Musical_intelligence,Body_intelligence,Interpersonal_intelligence,
                    Intrapersonal_intelligence,Verbal_intelligence,Existential_intelligence)
    
    X_TEST=X_TEST.reshape(1,15)

    labels=['Biomedical Engineering', 'Chemical Engineering',
        'Civil Engineering',
        'Computer and Information Systems Engineering',
        'Electrical Engineering', 'Mechanical Engineering',
        'Software Engineering', 'Telecommunications Engineering']

    if dict['button']==0:
        filename1 = 'final_model.sav'
        loaded_model = joblib.load(filename1)
        predicted_results=loaded_model.predict_proba(X_TEST)
        predicted_results = predicted_results.tolist()[0]
        predicted_results = [round(num*100, 2) for num in predicted_results]
        print(predicted_results)
        
        res = {}
        
        for i in range(len(predicted_results)):
            res[labels[i]] = predicted_results[i]
        print(res)

        from collections import Counter

        final_res = dict(Counter(res).most_common(5))

        for k, v in final_res.items():
            final_res[k] = str(v) + '%'

        final_res=list(final_res.keys())
        print(final_res)
 
    elif dict['button']==1:
        filename2 = 'medical_model.sav'
        loaded_model2 = joblib.load(filename2)
        predicted_results2=loaded_model2.predict_proba(X_TEST)
        predicted_results2 = predicted_results2.tolist()[0]
        predicted_results2 = [round(num*100, 2) for num in predicted_results2]
        print(predicted_results2)
    
        res2 = {}
        
        for j in range(len(predicted_results2)):
            res2[labels[j]] = predicted_results2[i]
        print(res2)

        final_res = dict(Counter(res2).most_common(5))

        for a, b in final_res.items():
            final_res[a] = str(b) + '%'
        
        final_res=list(final_res.keys())
        print(final_res)

    elif dict['button']==2:
        filename1 = 'final_model.sav'
        loaded_model = joblib.load(filename1)
        predicted_results=loaded_model.predict_proba(X_TEST)
        predicted_results = predicted_results.tolist()[0]
        predicted_results = [round(num*100, 2) for num in predicted_results]
        print(predicted_results)
        
        res = {}
        
        for i in range(len(predicted_results)):
            res[labels[i]] = predicted_results[i]
        print(res)

        from collections import Counter

        final_res1 = dict(Counter(res).most_common(5))

        for k, v in final_res1.items():
            final_res1[k] = str(v) + '%'

        filename2 = 'medical_model.sav'
        loaded_model2 = joblib.load(filename2)
        predicted_results2=loaded_model2.predict_proba(X_TEST)
        predicted_results2 = predicted_results2.tolist()[0]
        predicted_results2 = [round(num*100, 2) for num in predicted_results2]
        print(predicted_results2)
    
        res2 = {}
        for j in range(len(predicted_results2)):
            res2[labels[j]] = predicted_results2[i]
        print(res2)

        final_res2 = dict(Counter(res2).most_common(5))

        for a, b in final_res2.items():
            final_res2[a] = str(b) + '%'

        #final_res = list(final_res.keys()) + list(final_res2.keys())
        final_res = {}
        final_res.update(final_res1)
        final_res.update(final_res2)
        print(final_res)
#################################################xxxxxxxx
        final_res = dict(sorted(final_res.items(), key=lambda x: float(x[1][:-1]), reverse=True)[:5])
        final_res=list(final_res.keys())        

   

    redirect_url = '/results?predictions=' + json.dumps(final_res)
    return redirect(redirect_url)








##Today##
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from .serializers import CustomUserSerializer

# class CustomUserView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         serializer = CustomUserSerializer(request.user)
#         return Response(serializer.data)



# class ScoreCreateView(generics.CreateAPIView):
#     serializer_class = ScoreSerializer
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (permissions.IsAuthenticated,)
#     model_path = 'path_to_your_model_file.joblib'  # Replace with the actual path to your model file

#     def _init_(self, *args, **kwargs):
#         super()._init_(*args, **kwargs)
#         self.model = joblib.load(self.model_path)

#     @transaction.atomic
#     def post(self, request, *args, **kwargs):
#         data = request.data.copy()
#         data['user'] = request.user.id

#         serializer = self.get_serializer(data=data)
#         serializer.is_valid(raise_exception=True)

#         # Extract the necessary fields for the prediction
#         prediction_data = {
#             'field1': data['field1'],
#             'field2': data['field2'],
#             # Add more fields as needed...
#         }

#         # Run the machine learning model to predict the score
#         score = self.model.predict(prediction_data)

#         # Save the score along with the other fields
#         serializer.save(score=score)

#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=201, headers=headers)
# #path('scores/', ScoreCreateView.as_view(), name='create-score')

    # def post(self, request, *args, **kwargs):
    #     data = request.data.copy()
    #     data['user'] = request.user.id

    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)

    #     # Extract the necessary fields for the prediction
    #     prediction_data = {
    #         'field1': data['field1'],
    #         'field2': data['field2'],
    #         # Add more fields as needed...
    #     }

    #     # Run the machine learning model to predict the score
    #     #score = self.model.predict(prediction_data)

    #     # Save the score along with the other fields
    #     serializer.save(score=100)

    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=201, headers=headers)

##
# from .models import User

# def user_create(request):
#     # Assuming you have received the user data from the request
#     username = request.POST.get('username')
#     email = request.POST.get('email')
#     password = request.POST.get('password')

#     # Create a new User instance
#     user = User(username=username, email=email, password=password)

#     # Save the user instance to the database
#     user.save()