from django.shortcuts import render, redirect
from .models import User, Trip
from django.contrib import messages
from django.db.models import Count

# Create your views here.
def index(request):
    return render(request, 'pythonBeltExam1_app/index.html')

def register(request):
    if request.method == 'POST':
        data_stuff = {
        'fname':request.POST['first'],
        'lname':request.POST['last'],
        'email':request.POST['mail'],
        'password':request.POST['pass'],
        'pass_conf':request.POST['conf']
        }
        result = User.objects.register(data_stuff)
        if result['errors'] == None:
            request.session['id'] = result['user'].id
            request.session['fname'] = result['user'].first_name
            return redirect('/trips')
        else:
            for error in result['errors']:
                messages.error(request, error, extra_tags='register')
            return redirect ('/')

def login(request):
    if request.method == "POST":
        login_stuff = {
        'email':request.POST['mail'],
        'password':request.POST['pass']
        }
    login_result = User.objects.login(login_stuff)
    if login_result['errors'] == None:
        request.session['fname'] = login_result['user'].first_name
        request.session['id'] = login_result['user'].id
        return redirect('/trips')
    else:
        for error in login_result['errors']:
            messages.error(request, error, extra_tags='login')
        return redirect ('/')

def logout(request):
    request.session.pop('id')
    return redirect ('/')

def trips(request):
    current_user = User.objects.get(id=request.session['id'])
    all_trips = Trip.objects.all().order_by('-created_at')
    trips_list = []
    for trip in all_trips:
        # trip.joined=True
        # try:
        #     Join.objects.get(user=current_user, trip=trip)
        # except:
        #     Trip.joined=False
        trips_list.append(trip)
    context = {
    "input":User.objects.all(),
    "trips":trips_list,
    'user': User.objects.get(id=request.session['id']),
    }
    return render(request, 'pythonBeltExam1_app/trips.html', context)

def join(request):
    return redirect('/trips')

def destination(request):
    return redirect('/trips')

def add_trip(request):
    current_user = User.objects.get(id=request.session['id'])
    a_trip = Trip.objects.create(destination=request.POST['location'], plan=request.POST['description'], trip_from=request.POST['from'], trip_to=request.POST['to'], trip_user=current_user)
    return redirect('/trips')

def add_trip_page(request):
    return render(request, 'pythonBeltExam1_app/add_trip.html')





# end
