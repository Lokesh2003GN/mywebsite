from django.shortcuts import render
from django.http import HttpResponse
def resistor(request):
    return render(request, 'ECE/resistor.html')

def  resistor_result(request):
     inputcode = request.GET["inputcode"]
     nothing=""
     input_words = inputcode.split()
     if len(input_words) != 4:
        result1 = "please enter only 4 colors "
        result2 = "please enter only 4 colors "
        result3 = "please enter only 4 colors"
        return render(request, 'ECE/resistor.html', {'result1': result1, 'result2': result2, 'result3': result3, 'input': nothing})
     a,b,c,d=inputcode.split()

     m=a
     n=b
     o=c
     p=d
     if a=="black":
         a=0
     elif a=="brown":
         a=1
     elif a=="red":
         a=2
     elif a=="orange":
         a=3
     elif a=="yellow":
         a=4
     elif a=="green":
         a=5
     elif a=="blue":
         a=6
     elif a=="violet":
         a=7
     elif a=="gray":
         a=8
     elif a=="white":
         a=9
     elif a=="gold":
         a=10
     elif a=="silver":
         a=11
     elif a=="no_color":
         a=12
     if b=="black":
         b=0
     elif b=="brown":
         b=1
     elif b=="red":
         b=2
     elif b=="orange":
         b=3
     elif b=="yellow":
         b=4
     elif b=="green":
         b=5
     elif b=="blue":
         b=6
     elif b=="violet":
         b=7
     elif b=="gray":
         b=8
     elif b=="white":
         b=9
     elif b=="gold":
         b=10
     elif b=="silver":
         b=11
     elif b=="no_color":
         b=12
     if c=="black":
         c=0
     elif c=="brown":
         c=1
     elif c=="red":
         c=2
     elif c=="orange":
         c=3
     elif c=="yellow":
         c=4
     elif c=="green":
         c=5
     elif c=="blue":
         c=6
     elif c=="violet":
         c=7
     elif c=="gray":
         c=8
     elif c=="white":
         c=9
     elif c=="gold":
         c=10
     elif c=="silver":
         c=11
     elif c=="no_color":
         c=12
     if d=="gold":
         d=5
     elif d=="brown":
         d=1
     elif d=="red":
         d=2
     elif d=="orange":
         d=3
     elif d=="yellow":
         d=4
     elif d=="green":
         d=0.5
     elif d=="blue":
         d=0.25
     elif d=="violet":
         d=0.1
     elif d=="gray":
         d=0.05
     elif d=="silver":
         d=10
     elif d=="black":
         d=11
     elif d=="white":
         d=12
     elif d=="no_color":
         d=20
     
     value1=(10*a+b)
     value2=(10**c)
     value3=d
     multiple=value1*value2
     
     result1=str(multiple)+"±"+str(value3)+"%"
     c1=str(c)
     result2=str(value1)+"×"+"10^"+c1+"±"+str(value3)+"%"
     percent=multiple*d/100
     final1=multiple+percent
     final2=multiple-percent
     result3=str(final1)+"-"+str(final2)
     if a == 10 or b == 10 or c == 10 or a == 11 or b == 11 or c == 11 or a == 12 or b == 12 or c == 12 or d==11 or d==12:
         result1 = "invalid color code"
         result2 = "invalid color code"
         result3 = "invalid color code"

     return render(request, 'ECE/resistor.html', {'result1': result1,'result2':result2,'result3':result3,'input':inputcode,'color1':m,'color2':n,'color3':o,'color4':p})
 

# Create your views here.
