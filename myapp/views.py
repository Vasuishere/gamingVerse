from django.shortcuts import render,redirect
from .forms import TeamMemberForm
from .models import Header, Tournament,TeamMember,Winner

# Create your views here.
def index(request):
    data = Header.objects.all
    data1 = Tournament.objects.all
    data2 = Winner.objects.all
    return render(request,"index.html",{"data":data,"data1":data1,"data2":data2})

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



def team_summary(request):
    # Example: Fetch the current team ID from session and display its members
    team_id = request.session.get('team_id', 1)
    team_members = TeamMember.objects.filter(team_id=team_id)

    return render(request, 'team_summary.html', {'team_members': team_members})


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

def delete_member(request, member_id):
    # Get the team member or return 404 if not found
    team_member = get_object_or_404(TeamMember, id=member_id)
    team_member.delete()  # Delete the member

    # Optionally add a success message
    messages.success(request, "Team member deleted successfully.")
    return redirect('team_summary')  # Redirect back to the summary page