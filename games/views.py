from django.shortcuts import render,redirect
from django.http import HttpResponse

def rock_paper_scissor(request):
    return render(request, 'games/rock_paper_scissor.html')
current_image="rock.png"
def change_image(request):
    global current_image
    if request.method == 'POST':
        print("post====", request.POST)
        if 'button' in request.POST:
            new_image = request.POST['button']
            current_image = new_image
            return redirect(request,'game/rock_paper_scissor.html',{'result': current_image})
        else:
            return HttpResponse("No new_image parameter found in the POST data.")
    return HttpResponse("Invalid request method.")
# Create your views here.
