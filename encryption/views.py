from django.shortcuts import render
from django.http import HttpResponse

def encryption(request):
    
    return render(request, 'encryption/index.html')

def result(request):
    goto = request.GET["goto"]
    textbox = request.GET["textbox"]
    code=request.GET["code"]
    if code=="":
        a=[0,0]
    else:
        a = [int(digit) for digit in str(code)]
    
    digit_count = len(a)-1
    option = int(goto)
        

    def ascii(text):
        y = 0
        xascii = []
        output = ""
        for i in text:
            ascii_val = ord(i)
            xascii.append(ascii_val)
        for i in xascii:
            m = a[y]
            if y < digit_count:
                y += 1
            else:
                y = 0
            z = i + m
            output += chr(z)  # Convert back to character
        return output

    def dascii(text):
        y = 0
        xascii = []
        output = ""
        for i in text:
            ascii_val = ord(i)
            xascii.append(ascii_val)
        for i in xascii:
            m = a[y]
            if y < digit_count:
                y += 1
            else:
                y = 0
            z = i - m
            output += chr(z)  # Convert back to character
        return output

    if option == 1:
        result_text = ascii(textbox)
    elif option == 2:
        result_text = dascii(textbox)
    else:
        result_text = ""

    return render(request, 'encryption/index.html', {'result': result_text})

# Create your views here.
