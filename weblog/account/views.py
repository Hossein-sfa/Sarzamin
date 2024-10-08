from django.shortcuts import render, HttpResponse

def profile(request, username):
    return render(request, 'profile.html', context={'username': username})


users_list = [
    {'name': 'Ali', 'last_name': 'Khamis'},
    {'name': 'Hossein', 'last_name': 'Shamsaei'},
    {'name': 'Reza', 'last_name': 'Akbari'},
]

def users(request):
    return render(request, 'users.html', context={'users_list': users_list})