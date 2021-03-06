from django.shortcuts import render, redirect
from time import gmtime, strftime
import random

# Create your views here.
def index(request):
    if "gold" not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request, "index.html")


def process(request):
    time = strftime("%Y-%m-%d %H:%M:%S %p", gmtime())
    print(request.POST['location'])
    if request.POST['location'] == "farm":
        amount_to_add = random.randint(10,20)
        activity = f"Earned {amount_to_add} from Farm at {time}"

    elif request.POST['location']  == "house":
        amount_to_add = random.randint(2,5)
        activity = f"Earned {amount_to_add} from House at {time}"

    elif request.POST['location']  == "cave":
        amount_to_add = random.randint(5,10)
        activity = f"Earned {amount_to_add} from Cave at {time}"

    elif request.POST['location']  == "casino":
        amount_to_add = random.randint(-50, 50)
        if amount_to_add <= 0:
            activity = f"Lost {amount_to_add} from Casino at {time}; better luck next time!"
        if amount_to_add > 0:
            activity = f"Earned {amount_to_add} from Casino at {time}; good job!"

    request.session['gold'] += amount_to_add
    request.session['activities'].append(activity)
    print(amount_to_add)
    return redirect("/")
