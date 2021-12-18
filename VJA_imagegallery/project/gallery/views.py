from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .models import Image, Gallery
from .forms import ImageForm, GalleryForm
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.views.generic import DeleteView, TemplateView, UpdateView
from django.urls import reverse_lazy
from .functions import galleryimagepairs
from django.contrib.auth.decorators import login_required
import os
from django.core.exceptions import ValidationError


@login_required(login_url='login')
def add_gallery_view(request):
    ImageFormSet = modelformset_factory(Image, form=ImageForm)

    if request.method == "GET":
        gallery_form = GalleryForm()
        formset = ImageFormSet(queryset=Image.objects.none())
        return render(request, 'gallery/add_gallery.html', {"gallery_form": gallery_form, "formset": formset})

    elif request.method == "POST":
        gallery_form = GalleryForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES)
        files = request.FILES.getlist('form-0-image')

        if gallery_form.is_valid() and formset.is_valid():
            gallery_obj = gallery_form.save(commit=False)
            gallery_obj.owner = request.user
            gallery_obj.save()

            for form in formset.cleaned_data:
                if files:
                    for image in files:
                        Image.objects.create(image=image, gallery=gallery_obj)
            return HttpResponseRedirect('/')
        else:
            print(gallery_form.errors)
            print(formset.errors)
            return render(request, 'gallery/add_gallery.html', {"gallery_form": gallery_form,"formset": formset})



@login_required(login_url='login')
def gallery_administration_view(request):
    if(request.method == 'GET'):


        list_of_galleries = Gallery.objects.filter(owner_id=request.user)
        list_of_images = Image.objects.filter(Q(gallery__in=list_of_galleries))
        pairs = galleryimagepairs(list_of_galleries, list_of_images)
        context = {
        'list_of_galleries': pairs }

        #galleries = Gallery.objects.filter(owner_id = request.user.id)
        return render(request, 'gallery/gallery_administration.html', context)


    elif(request.method == 'POST'):
        pass


@login_required(login_url='login')
def gallery_image_administration_view(request, pk):
    if(request.method == 'GET'):
        images = Image.objects.select_related('gallery').filter(gallery__owner=request.user.id).filter(gallery__id=pk)
        galleryowner = Gallery.objects.filter(id=pk, owner=request.user.id)

        return render(request,'gallery/gallery_image_administration.html', {'images' : images, 'galleryowner' : galleryowner})
    elif(request.method == 'POST'):
        return render(request, '/')

@login_required(login_url='login')
def deleteimage(request, **kwargs):
    if(request.method == 'POST'):
        image_pk = kwargs.get('pkimg','')
        gallery_pk = kwargs.get('pkgal','')

        galleries = Gallery.objects.filter(owner=request.user.id)
        image = Image.objects.get(Q(gallery__in=galleries, id=image_pk))
        if(image): #The user is the owner of the picture
            #image_path = image.image
            #os.remove(str(image_path)) #Does not work, path is wrong --> starts with images... should by media/images....
            image.delete()
            return redirect('/gallery/gallery_image_administration/'+str(gallery_pk))
        else:
            return redirect('/')
    elif(request.method == 'GET'): #DO NOT ACCEPT GET
        return redirect('/')

@login_required(login_url='login')
def gallery_view(request, pk):
    try:
        gallery = Gallery.objects.get(Q(id=pk, owner=int(request.user.id)) | Q(id=pk, ispublic=True))
    except Gallery.DoesNotExist:
        gallery = {}
    return render(request, 'gallery/gallery.html', {"gallery": gallery})

@login_required(login_url='login')
def home(request):
    list_of_galleries = {}
    list_of_images = {}
    context = {}
    if(request.user.is_authenticated):
        list_of_galleries = Gallery.objects.filter(owner_id=request.user) | Gallery.objects.filter(ispublic=True)
        list_of_images = Image.objects.filter(Q(gallery__in=list_of_galleries))
        pairs = galleryimagepairs(list_of_galleries, list_of_images)
        context = {
        'list_of_galleries': pairs
    }
    return render(request, 'gallery/home.html', context)

class DeleteGalleryView(DeleteView):
    model = Gallery
    template_name = 'gallery/delete_gallery.html'
    success_url = reverse_lazy('gallery_administration')

class UpdateGalleryView(UpdateView):
    model = Gallery
    template_name = 'gallery/update_gallery.html'
    fields = ['name', 'title', 'ispublic', 'description']
    success_url = reverse_lazy('gallery_administration')

@login_required(login_url='login')
def addPhoto(request, pk):
    form = ImageForm()
    gallery = Gallery.objects.get(id=int(pk))

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        images = request.FILES.getlist('image')

        if form.is_valid():
            print(images)
            for image in images:
                image = Image.objects.create(
                    image = image,
                    gallery = gallery
                )
            return redirect('/gallery/'+str(pk))
        print(form.errors)

    context = {'form': form, 'gallery':gallery}
    return render(request, 'gallery/add_images.html', context)


