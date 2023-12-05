from django.shortcuts import render
from django.http import HttpResponse

def numbers(request):
    return render(request, 'maths/numbers.html')
    
def numbers_result(request):
    inputtext = int(request.GET["inputnumber"])
    x=1
    z=[]
    while x<=inputtext:
        z.append(x)
        x=x+1
    result = ' '.join(map(str, z))
    return render(request, 'maths/numbers.html', {'result': result})
 
def tables(request):
    return render(request, 'maths/tables.html')

def tables_result(request):
    x=int(request.GET['inputnumber1'])
    a=int(request.GET['inputnumber2'])
    y=1
    b=[]
    while y<=a:
        z=x*y
        b.append(f"{x} × {y} = {z}")
        y+=1
    result = '\n '.join(b)
    return render(request, 'maths/tables.html', {'result': result})

def factorial(request):
    return render(request, 'maths/factorial.html')
    
def factorial_result(request):
    inputtext = int(request.GET["inputnumber"])
    y=1
    while inputtext>1:
                    y=inputtext*y
                    inputtext-=1
    result = y
    return render(request, 'maths/factorial.html',{'result':result})

def decimal_binary_conversation(request):
    return render(request, 'maths/decimal_binary_conversation.html')

def decimal_binary_conversation_result(request):
    inputtext = int(request.GET["inputnumber"])
    goto = int(request.GET["goto"])
    
    def decimal_binary():
        no = inputtext
        binary = ""
        if no == 0:
            return "0" 
        else:
            while no > 0:
                reminder = no % 2
                binary = str(reminder) + binary
                no = no // 2
            return binary
    
    def binary_decimal():
        x = inputtext
        y = 0
        b = 0
        while x > 0:
            a = x % 10
            z = x // 10
            x = z
            if a == 1:
                c = 2 ** b
                y += c
            b += 1
        return y        
    
    if goto == 1:
        result_text = decimal_binary()
    elif goto == 2:
        result_text = str(binary_decimal()) 
    else:
        result_text = ""
        
    return render(request, 'maths/decimal_binary_conversation.html', {'result': result_text}) 

# Create your views here.
