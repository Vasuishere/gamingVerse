from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .forms import TeamMemberForm
from .models import Header, Tournament,TeamMember,Winner,User,game
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages  
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login



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
        # Use `authenticate` to validate the credentials
        user = authenticate(request, username=user_email, password=user_password)
        if user is not None:
            auth_login(request, user)
            request.session['isloggedin'] = True
            request.session['user_email'] = user_email
            return redirect("/index")
        else:
            error_message = "Invalid email or password."
            return render(request, "login.html", {"error_message": error_message})
    return render(request, "login.html")

def signup(request):
    if request.POST:
        user_name = request.POST['user_name']
        user_lastname = request.POST['user_lastname']
        user_email = request.POST['user_email']
        user_password = request.POST['user_password']
        # Create a new user with the email as the username
        user = User.objects.create_user(
            username=user_email,
            email=user_email,
            password=user_password,
            first_name=user_name,
            last_name=user_lastname
        )
        user.save()
        return redirect("/")
    return render(request, "signup.html")

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def logout_view(request):
    # Remove a custom session key, if it exists
    request.session.pop('isloggedin', None)
    logout(request)  # Django's built-in logout function
    return redirect('index')