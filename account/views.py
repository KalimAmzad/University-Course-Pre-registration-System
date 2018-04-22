from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, UserRegistrationForm, UserEditForm, StudentProfileEditForm, TeacherProfileEditForm
from .models import StudentProfile, TeacherProfile

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['student_id'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
        return render(request,'account/home.html',{'section':'home'})
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            user_id = user_form.cleaned_data['username']
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # new_user.set_mobile(user_form.cleaned_data['mobile'])
            mobile = user_form.cleaned_data['mobile']
            # new_user.set_address(user_form.cleaned_data['address'])
            address  = user_form.cleaned_data['address']
            # new_user.set_email(user_form.cleaned_data['email'])
            email = user_form.cleaned_data['email']
            semester = user_form.cleaned_data['semester']
            section = user_form.cleaned_data['section']
            sex = user_form.cleaned_data['sex']
            # Save the User object

            new_user.save()
            # Create the user profile
            if((user_id[0]=='C' or user_id[0]=='c') and len(user_id)==7 ):
                student_profile = StudentProfile.objects.create(user=new_user,mobile=mobile,email=email,address=address,
                                                                semester=semester,section=section,sex=sex)
            else:
                teacher_profile = TeacherProfile.objects.create(user=new_user,mobile=mobile,email=email,address=address)

            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def edit(request):
    user  = request.user
    user_id = user.username
    if((user_id[0]=='C' or user_id[0]=='c') and len(user_id)==7):
        if request.method == 'POST':
            user_form = UserEditForm(instance=request.user,
                                     data=request.POST)
            profile_form = StudentProfileEditForm(instance=request.user.studentprofile,
                                           data=request.POST,
                                           files=request.FILES)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Profile updated successfully')
            else:
                messages.error(request, 'Error updating your profile')
        else:
            user_form = UserEditForm(instance=request.user)
            profile_form = StudentProfileEditForm(instance=request.user.studentprofile)
        return render(request, 'account/edit.html', {'user_form': user_form,
                                                     'profile_form': profile_form})
    else:
        if request.method == 'POST':
            user_form = UserEditForm(instance=request.user,
                                     data=request.POST)
            profile_form = TeacherProfileEditForm(instance=request.user.teacherprofile,
                                           data=request.POST,
                                           files=request.FILES)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Profile updated successfully')
            else:
                messages.error(request, 'Error updating your profile')
        else:
            user_form = UserEditForm(instance=request.user)
            profile_form = TeacherProfileEditForm(instance=request.user.teacherprofile)
        return render(request, 'account/edit.html', {'user_form': user_form,
                                                     'profile_form': profile_form})

@login_required
def home(request):
    return render(request,'account/home.html',{'section':'home'})