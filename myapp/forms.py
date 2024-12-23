from django import forms
from .models import TeamMember

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name', 'game_name', 'unique_game_id']
        labels = {
            'name': "Name (Govt ID Proof)",
            'game_name': "Game Name",
            'unique_game_id': "Unique Game ID"
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'game_name': forms.TextInput(attrs={'class': 'form-control'}),
            'unique_game_id': forms.TextInput(attrs={'class': 'form-control'}),
        }
