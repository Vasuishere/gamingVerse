from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .forms import TeamMemberForm
from .models import Header, Tournament,TeamMember,Winner,User,game

# Create your views here.
def index(request):
    data = Header.objects.all
    data1 = Tournament.objects.all
    data2 = Winner.objects.all
    data3 = game.objects.all
    context = {
        'data': data,
        'data1': data1,
        'data2': data2,
        'data3': data3
    }
    return render(request,"index.html",context)

def contact(request):
    return render(request,"contact.html")

def winners(request):
    return render(request,"winners.html")

def deposit(request):
    return render(request,"deposit.html")

def Tournaments(request):
    return render(request,"Tournaments.html")

def service(request):
    return render(request,"service.html")

def team(request):
    data = TeamMember.objects.all
    form = TeamMemberForm()
    if request.method == 'POST':
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            form.save()
        if 'submit' in request.POST:
                return redirect('/team')  # Reload form for the next member
        else:
            return redirect('/team')
        
    return render(request,"team.html",{"data":data,"form":form})

def about(request):
    return render(request,"about.html")



def create_team(request):
    # Determine the next member number (based on current team size)
    team_size = TeamMember.objects.count()
    next_member_number = team_size + 1

    # Handle form submission
    if request.method == 'POST':
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database

            # Check which button was clicked
            if 'next' in request.POST:
                return redirect('create_team')  # Reload form for the next member
            elif 'submit' in request.POST:
                return redirect('team_summary')  # Redirect to team summary page
    else:
        form = TeamMemberForm()

    return render(request, 'create_team.html', {
        'form': form,
        'next_member_number': next_member_number
    })



# def team_summary(request,id):
#     # Example: Fetch the current team ID from session and display its members
#     id = request.session.get('id', 1)
#     team_members = TeamMember.objects.filter(id=id)

#     return render(request, 'team_summary.html', {'team_members': team_members})


from django.shortcuts import get_object_or_404, redirect

def edit_member(request, member_id):
    # Get the specific member
    team_member = get_object_or_404(TeamMember, id=member_id)

    if request.method == 'POST':
        form = TeamMemberForm(request.POST, instance=team_member)
        if form.is_valid():
            form.save()
            return redirect('team_summary')  # Redirect back to the summary page
    else:
        form = TeamMemberForm(instance=team_member)  # Pre-fill the form with existing data

    return render(request, 'edit_member.html', {'form': form})


from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages  # To show a success message after deletion

def delete_member(request, id):
    print(f"Deleting team member with ID: {id}")
    team_member = get_object_or_404(TeamMember, id=id)
    team_member.delete()
    messages.success(request, "Team member deleted successfully.")
    return redirect('team')


def login(request):
    if request.session.get("isloggedin"):
        return redirect("/index")
    if request.POST:
        user_email = request.POST["user_email"]
        user_password = request.POST["user_password"]
        user = User.objects.filter(user_email=user_email,user_password=user_password).count()
        if user>0:
            request.session['isloggedin'] = True
            request.session['user_email'] = user_email
            return redirect("/index")
    return render(request,"login.html")


def signup(request):
    if request.POST:
        user_name = request.POST['user_name']
        user_email = request.POST['user_email']
        user_password = request.POST['user_password']
        obj = User(user_name=user_name,user_email=user_email,user_password=user_password)
        obj.save()
        return redirect("/")
    return render(request,"signup.html")


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    if 'isloggedin' in request.session:
        del request.session['isloggedin']  # Remove the session key
    logout(request)  # Log out the user
    return redirect('index')  # Redirect to the login page (or any desired URL)
