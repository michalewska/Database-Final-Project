from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.db import connection, transaction
from .models import Meeting, Course, Project, Activity
from .forms import RegisterForm,  CourseCreateForm, MeetingCreateForm, ProjectCreateForm, ActivityCreateForm
from django.db.models import Q

cursor = connection.cursor()

# Create your views here.


def home(request):
    context = {}
    return render(request, 'base/home.html', context)


def about(request):
    context = {}
    return render(request, 'base/about.html', context)


def contact(request):
    context = {}
    return render(request, 'base/contact.html', context)


def dashboard(request):
    meetings = Meeting.objects.all()
    courses = Course.objects.all()
    projects = Project.objects.all()
    activities = Activity.objects.all()

    context = {
        "meetings": meetings,
        "courses": courses,
        "projects": projects,
        "activities": activities,
    }

    return render(request, 'base/dashboard.html', context)


def course_index(request):

    courses = Course.objects.filter(user=request.user, )

    context = {
        "courses": courses,
    }

    return render(request, 'base/course_index.html', context)


def course_filter(request):

    f = request.GET.get('f')
    q = request.GET.get('q')

    if f:
        if f == 'name':
            courses = Course.objects.filter(
                name__contains=q, user=request.user)
        elif f == 'start_time':
            courses = Course.objects.filter(
                start_time__contains=q, user=request.user)
        elif f == 'end_time':
            courses = Course.objects.filter(
                end_time__contains=q, user=request.user)
    else:
        courses = Course.objects.filter(user=request.user)

    context = {
        'courses': courses,
    }

    return render(request, 'base/course_filter.html', context)


def course_create(request):

    if request.method == "POST":
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            user = request.user
            new_course = Course(user=user, name=name, start_time=start_time, end_time=end_time)
            new_course.save()
            # query = f'INSERT INTO base_course (user, name, start_time, end_time) VALUES ({user}, "{name}", "{start_time}", "{end_time}")'
            # cursor.execute(query)  # Save to Database
            # transaction.commit()
            return HttpResponseRedirect('../')
    else:
        form = CourseCreateForm()

        context = {
            "form": form,
        }

        return render(request, 'base/course_create.html', context)


def course_detail(request, pk):
    course = Course.objects.get(pk=pk)

    context = {
        "course": course,
    }

    return render(request, 'base/course_detail.html', context)


def course_update(request, pk):
    course = Course.objects.get(pk=pk)
    course_queryset = Course.objects.filter(pk=pk)

    if request.method == "POST":
        form = CourseCreateForm(request.POST, instance=course)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            course_queryset.update(name=name, start_time=start_time, end_time=end_time)
            # query = f'UPDATE base_course SET name = "{name}", start_time = "{start_time}", end_time = "{end_time}" WHERE (id="{pk}")'
            # cursor.execute(query)  # Save to Database
            # transaction.commit()
        else:
            print(form.errors)
        return HttpResponseRedirect('../')
    else:
        form = CourseCreateForm(instance=course)

        context = {
            "form": form,
        }

        return render(request, 'base/course_update.html', context)


def course_delete(request, pk):
    course = Course.objects.get(pk=pk)
    course.delete()
    return HttpResponseRedirect('../../')


def meeting_index(request):
    meetings = Meeting.objects.filter(user=request.user)

    context = {
        "meetings": meetings,
    }

    return render(request, 'base/meeting_index.html', context)


def meeting_filter(request):

    f = request.GET.get('f')
    q = request.GET.get('q')

    if f:
        if f == 'name':
            meetings = Meeting.objects.filter(
                name__contains=q, user=request.user)
        elif f == 'start_time':
            meetings = Meeting.objects.filter(
                start_time__contains=q, user=request.user)
        elif f == 'end_time':
            meetings = Meeting.objects.filter(
                end_time__contains=q, user=request.user)
    else:
        meetings = Meeting.objects.filter(user=request.user)

    context = {
        'meetings': meetings,
    }

    return render(request, 'base/meeting_filter.html', context)


def meeting_create(request):

    if request.method == "POST":
        form = MeetingCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            user = request.user
            new_meeting = Meeting(user=user, name=name, start_time=start_time, end_time=end_time)
            new_meeting.save()
            # query = f'INSERT INTO base_meeting (user, name, start_time, end_time) VALUES ({user}, "{name}", "{start_time}", "{end_time}")'
            # cursor.execute(query)  # Save to Database
            # transaction.commit()
            return HttpResponseRedirect('../')
    else:
        form = MeetingCreateForm()

        context = {
            "form": form,
        }

        return render(request, 'base/meeting_create.html', context)


def meeting_detail(request, pk):
    meeting = Meeting.objects.get(pk=pk)

    context = {
        "meeting": meeting,
    }

    return render(request, 'base/meeting_detail.html', context)


def meeting_update(request, pk):

    if request.method == "POST":
        form = MeetingCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            query = f'UPDATE base_meeting SET name = "{name}", start_time = "{start_time}", end_time = "{end_time}" WHERE (id="{pk}")'
            cursor.execute(query)  # Save to Database
            transaction.commit()
        return HttpResponseRedirect('../')
    else:
        meeting = Meeting.objects.get(pk=pk)
        form = MeetingCreateForm(instance=meeting)

        context = {
            "form": form,
        }

        return render(request, 'base/meeting_update.html', context)


def meeting_delete(request, pk):

    meeting = Meeting.objects.get(pk=pk)
    meeting.delete()

    return HttpResponseRedirect('../../')


def project_index(request):
    projects = Project.objects.filter(user=request.user)

    context = {
        "projects": projects,
    }

    return render(request, 'base/project_index.html', context)


def project_filter(request):

    f = request.GET.get('f')
    q = request.GET.get('q')

    if f:
        if f == 'name':
            projects = Project.objects.filter(
                name__contains=q, user=request.user)
        elif f == 'deadline':
            projects = Project.objects.filter(
                deadline__contains=q, user=request.user)
        elif f == 'course':
            projects = Project.objects.filter(
                course__name__contains=q, user=request.user)
    else:
        projects = Project.objects.filter(user=request.user)

    context = {
        'projects': projects,
    }

    return render(request, 'base/project_filter.html', context)


def project_create(request):

    if request.method == "POST":
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            deadline = form.cleaned_data['deadline']
            course = Course.objects.get(pk=request.POST.get('course'))
            new_project = Project(user=request.user, name=name, deadline=deadline, course=course)
            new_project.save()
            # query = f'INSERT INTO base_project (name, deadline) VALUES ("{name}", "{deadline}")'
            # cursor.execute(query)  # Save to Database
            # transaction.commit()
        return HttpResponseRedirect('../')
    else:
        form = ProjectCreateForm()

        courses = Course.objects.filter(user = request.user)

        context = {
            "form": form,
            "courses": courses,
        }

        return render(request, 'base/project_create.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)

    context = {
        "project": project,
    }

    return render(request, 'base/project_detail.html', context)


def project_update(request, pk):

    if request.method == "POST":
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            deadline = form.cleaned_data['deadline']
            user = request.user
            # query = f'UPDATE base_project SET name = "{name}", deadline = "{deadline}" WHERE (id="{pk}")'
            # cursor.execute(query)  # Save to Database
            # transaction.commit()
        return HttpResponseRedirect('../')
    else:
        project = Project.objects.get(pk=pk)
        form = ProjectCreateForm(instance=project)

        context = {
            "form": form,
        }

        return render(request, 'base/project_update.html', context)


def project_delete(request, pk):

    project = Project.objects.get(pk=pk)
    project.delete()

    return HttpResponseRedirect('../../')


def activity_index(request):
    activities = Activity.objects.filter(user=request.user)

    context = {
        "activities": activities,
    }

    return render(request, 'base/activity_index.html', context)


def activity_filter(request):

    f = request.GET.get('f')
    q = request.GET.get('q')

    if f:
        if f == 'name':
            activities = Activity.objects.filter(name__contains=q, user=request.user)
        elif f == 'start_time':
            activities = Activity.objects.filter(start_time__contains=q, user=request.user)
        elif f == 'end_time':
            activities = Activity.objects.filter(end_time__contains=q, user=request.user)
    else:
        activities = Activity.objects.filter(user=request.user)

    context = {
        'activities': activities,
    }

    return render(request, 'base/activity_filter.html', context)


def activity_create(request):

    if request.method == "POST":
        form = ActivityCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            user = request.user
            new_activity = Activity(user=user, name=name, start_time=start_time, end_time=end_time)
            new_activity.save()
            # query = f'INSERT INTO base_activity (name, start_time, end_time) VALUES ("{name}", "{start_time}", "{end_time}")'
            # cursor.execute(query)  # Save to Database
            # transaction.commit()
            return HttpResponseRedirect('../')
    else:
        form = ActivityCreateForm()

        context = {
            "form": form,
        }

        return render(request, 'base/activity_create.html', context)


def activity_detail(request, pk):
    activity = Activity.objects.get(pk=pk)

    context = {
        "activity": activity,
    }

    return render(request, 'base/activity_detail.html', context)


def activity_update(request, pk):

    if request.method == "POST":
        form = ActivityCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            query = f'UPDATE base_activity SET name = "{name}", start_time = "{start_time}", end_time = "{end_time}" WHERE (id="{pk}")'
            cursor.execute(query)  # Save to Database
            transaction.commit()
        return HttpResponseRedirect('../')
    else:
        activity = Activity.objects.get(pk=pk)
        form = ActivityCreateForm(instance=activity)

        context = {
            "form": form,
        }

        return render(request, 'base/activity_update.html', context)


def activity_delete(request, pk):

    activity = Activity.objects.get(pk=pk)
    activity.delete()

    return HttpResponseRedirect('../../')



class CreateAccount(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('base:dashboard')
    template_name = 'registration/create-account.html'

    def form_valid(self, form):
        view = super(CreateAccount, self).form_valid(form)
        username, password = form.cleaned_data.get(
            'username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view
