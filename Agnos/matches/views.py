from django.http import JsonResponse
from .models import match
from .serializers import matchSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])

def match_list(request):

    if request.method == 'GET':
        message = request.GET.get('message')
        pattern = request.GET.get('pattern')
        if(pattern is None or message is None):
            if message is None and pattern is None:
                return Response( {'error': 'need message and pattern'},status = status.HTTP_400_BAD_REQUEST)
            elif(pattern is None):
                return Response( {'error': 'need pattern'},status = status.HTTP_400_BAD_REQUEST)
            else :
                return Response( {'error': 'need message'},status = status.HTTP_400_BAD_REQUEST)
        else:
            new_pattern = transform(pattern)
            print(new_pattern)
            return Response({'is_match' : is_really_match(message,new_pattern)}, status = status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = matchSerializer(data = request.data)
        if serializer.is_valid():
            mes = serializer.data.get('message')
            pat = serializer.data.get('pattern')
            new_pattern = transform(pattern)
            return Response({'is_match' : is_really_match(mes,new_pattern)}, status = status.HTTP_200_OK)
        else :
            return Response(status = status.HTTP_400_BAD_REQUEST)

def is_really_match(message,pattern):
    t = False
    count = 0
    if(pattern == '*'):
        return True
    else:
            for i in range(len(pattern)):
                if(pattern[i] == '*'):
                    count+=1
            if pattern[0]=='*' and count==1 :
                length = len(pattern)-1
                return message[len(message)-length:]==pattern[1:]
            elif pattern[-1]=='*' and count==1 :
                length = len(pattern)-1
                return message[:length]==pattern[:len(pattern)-1]
            elif count == 0 :
                if(len(pattern)!=len(message)):
                    return False
                check = True
                for i in range(len(pattern)):
                    if(pattern[i] != message[i]):
                        if(pattern[i] == '?'):
                            continue
                        else:
                            check = False
                            break
                t = check
            elif count==2 and pattern[-1]=='*' and pattern[0]=='*':
                length = len(pattern)-2
                print(pattern[1:-1])
                return pattern[1:-1] in message
            else:
                idx=0
                target=''
                length = 0
                trig = False
                for i in range(len(pattern)):
                    if pattern[i]=='*':
                        if(trig):
                            print('target : '+target)
                            x,y = find_str(length,message,target,idx)
                            if(x==False) :
                                print('wrong : '+target)
                                return False
                            idx = y
                            length = 0
                            target = ''
                        else:
                            trig = True     
                    else:
                        if(i == len(pattern)-1):  
                            return message[-1] == pattern[-1]
                        target += pattern[i]
                        length += 1
                        trig = True
                return True
    return t

def transform(pattern):
    trig = False
    new_pattern = ''
    for i in range(len(pattern)):
        if pattern[i]=='*':
            if(i == len(pattern)-1):
                new_pattern+='*'
            trig = True
            continue
        else :
            if trig==True:
                new_pattern+='*'
                new_pattern+=pattern[i]
                trig = False
            else:
                new_pattern+=pattern[i]
    return new_pattern

        
def find_str(length,message,target,idx):
    for i in range(len(message)):
        print('target: '+target+' message: '+message[i+idx:i+length+idx])
        if(i+length+idx > len(message)):
            return (False,-1)
        if(message[i+idx:i+length+idx] == target):
            return (True,i+idx+length)
        if('?' in target):
            count = 0
            for ch in message[i+idx:i+length+idx]:
                if ch in target:
                    count+=1
            if count == length-1:
                return (True,i+idx+length)
         
            
    return (False,-1)

