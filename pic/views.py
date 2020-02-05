from django.shortcuts import render, redirect, get_object_or_404
from .models import Photograher, Main, Model, Album
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home(request):
    dests = Photograher.objects.all()
    dams = Main.objects.all()
    return render(request, 'pic/home.html', {'dests':dests, 'dams':dams})



def create(request):
    if request.method == 'POST':

        if request.POST['Name'] and request.POST['body'] and request.FILES['icon'] and \
                request.FILES['image']:

            model = Model()

            model.Name = request.POST['Name']

            model.body = request.POST['body']

            model.icon = request.FILES['icon']

            model.image = request.FILES['image']

            model.pub_date = timezone.datetime.now()

            model.save()

            return redirect('/pic/' + str(model.id))

        else:

            return render(request, 'pic/create.html', {'error': 'All fields are required.'})

    else:

        return render(request, 'pic/create.html')


def detail(request, model_id):
    model = get_object_or_404(Model, pk=model_id)
    return render(request, 'pic/detail.html', {'model':model})


def upvote(request, model_id):
    if request.method == 'POST':
        model = get_object_or_404(Model, pk=model_id)
        model.votes_total += 1
        model.save()
        return redirect('/pic/' + str(model.id))


def modeldetail(request):
    models = Model.objects.all()
    return render(request,'pic/modeldetail.html', {'models':models})


def album(request):
    album = Album.objects.all()
    return render(request,'pic/album.html', {'album':album})
