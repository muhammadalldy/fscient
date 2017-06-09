from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from mahasiswa.models import Mahasiswa
from mahasiswa.serializers import MahasiswaSerializer
from .models import Mahasiswa
from .models import Profile

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from forms import SignUpForm

def index(request):
    mahasiswa_list  = Profile.objects.all()
    # mhs             = Mahasiswa.objects.get(pk=id)
    context = {'latest_question_list': mahasiswa_list}
    # output = ', '.join([q.nama for q in latest_question_list])
    return render(request, 'mahasiswa/index.html', context)
    # latest_question_list = Mahasiswa.objects.order_by('-created')[:5]
    # output = ', '.join([q.nama for q in latest_question_list])
    # return HttpResponse(output)

def detail(request, id):
    mhs   = Profile.objects.get(pk=id)
    context = {'nama': mhs.user, 'noreg': mhs.noreg, 'angkatan': mhs.angkatan, 'peminatan': mhs.peminatan}
    # output = ', '.join([q.nama for q in latest_question_list])
    return render(request, 'mahasiswa/mahasiswa_detail.html', context)

    # return HttpResponse("You're looking at question %s." % id)

def results(request, nama_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % nama_id)

def vote(request, nama_id):
    return HttpResponse("You're voting on question %s." % nama_id)

def daftar(request):
    return render(request, 'mahasiswa/daftar.html')

def masuk(request):
    return render(request, 'mahasiswa/masuk.html')



@csrf_exempt
def mahasiswa_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        mahasiswa = Mahasiswa.objects.all()
        serializer = MahasiswaSerializer(mahasiswa, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MahasiswaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def mahasiswa_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        mahasiswa = Mahasiswa.objects.get(pk=pk)
    except Mahasiswa.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MahasiswaSerializer(mahasiswa)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MahasiswaSerializer(mahasiswa, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        mahasiswa.delete()
        return HttpResponse(status=204)

        


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registrasi/signup.html', {'form': form})





def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal

            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.noreg = form.cleaned_data.get('noreg')
            user.profile.angkatan = form.cleaned_data.get('angkatan')
            user.profile.peminatan = form.cleaned_data.get('peminatan')



            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})