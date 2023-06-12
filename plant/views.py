from django.shortcuts import render,redirect
from .forms import*
from .models import*
from django.contrib import messages
from django.contrib.auth.models import Group
from django.core.files.storage import FileSystemStorage

import tensorflow as tf
import numpy as np
from tensorflow import keras
import os
import cv2
from tensorflow.keras import backend
from tensorflow.keras.models import Model,Sequential,load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tensorflow.keras.preprocessing import image

# Create your views here.
def index(request):
    return render(request,'index.html')

# Create your views here.
def result(request):
    return render(request,'result.html')

def register(request):
   form=UserForm()
   form7=custform()
   mydict={'form':form,'form7':form7}
   if request.method=="POST":
      form=UserForm(request.POST)
      form7=custform(request.POST,request.FILES)
      if form.is_valid() and form7.is_valid():
         user=form.save()
         user.set_password(user.password)
         user.save()
         messages.success(request,'registered successfully')
         Staffmodel=form7.save()
         Staffmodel.user=user
         Staffmodel.save()
         group=Group.objects.get_or_create(name="Customer")
         group[0].user_set.add(user)
         return redirect('login')
   
   return render(request, 'register.html',context=mydict)

def is_Staffmodel(user):
   return user.groups.filter(name="Customer").exists()

def login(request):
   return render(request,'login.html')

def home(request):
   return render(request,'home.html')
def afterlogin_view(request):
   if is_Staffmodel(request.user):
      return redirect('home')

def predict(request):
    result=""
    img1=""
    val=""
    if request.method== 'POST' and request.FILES['myfile']:
        myfile=request.FILES['myfile']
        print('file name',myfile)
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        uploaded=fs.url(filename)
        print('uploaded',myfile.name)
        request.session['file']=myfile.name
        
        fn=myfile.name
        fullpath="C:\\Users\\jithe\\OneDrive\\Desktop\\jithesh\\plantdiseaseprediction\\" + fn
        classifier = load_model("C:\\Users\\jithe\\OneDrive\\Desktop\\model\\plant_model1.hdf5")
        li= ['Corn','Pepper','Rice','Tomato']

        img1 = image.load_img(fullpath,target_size=(224,224))
        image_path =fullpath
        new_img = load_img(image_path, target_size=(224, 224))

        img = img_to_array(new_img)
         #cv2_imshow(img)
        img = np.expand_dims(img, axis=0)
        img = img/255
        print(img.shape)
        prediction = classifier.predict(img)
        print(prediction)
        d = prediction.flatten()
        j = d.max()
        for index,item in enumerate(d):
           if item == j:
             class_name = li[index]
        print('The matched plant type class is',class_name)
     
        
        return render(request,'result.html',{
            'uploaded':class_name
        })
        
    return render(request,'home.html') 


def predict1(request):
    result=""
    img1=""
    val=""
    if request.method== 'POST' and request.FILES['myfile']:
        myfile=request.FILES['myfile']
        print('file name',myfile)
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        uploaded=fs.url(filename)
        print('uploaded',myfile.name)
        request.session['file']=myfile.name
        
        fn=myfile.name
        fullpath="C:\\Users\\jithe\\OneDrive\\Desktop\\jithesh\\plantdiseaseprediction\\" + fn
        classifier0 = load_model("C:\\Users\\jithe\\OneDrive\\Desktop\\model\\plan_disease_model1.hdf5")
        
        li0=[' bell Bacterial spot_mildly diseased', ' bell Bacterial spot_moderately diseased', ' bell Bacterial spot_severely diseased', 'healthy', 'Bacterial leaf blight_moderately diseased', 'Bacterial leaf blight_severely diseased', 'Brown spot_moderately diseased', 'Brown spot_severely diseased', 'Leaf smut_moderately diseased', 'Leaf smut_severely diseased', ' Bacterial spot_mildly diseased', ' Bacterial spot_moderately diseased', 'Bacterial spot_severely diseased', ' Early blight_mildly diseased', ' Early blight_moderately diseased', ' Early blight_severely diseased', ' Late blight_mildly diseased', ' Late blight_moderately diseased', ' Late blight_severely diseased', ' Septoria leaf spot_mildly diseased', ' Septoria leaf spot_moderately diseased', ' Septoria leaf spot_severely diseased', 'YellowLeaf__Curl_Virus_Moderately diseased', 'YellowLeaf__Curl_Virus_mildly diseased', 'YellowLeaf__Curl_Virus_severely diseased', 'healthy', ' Common Rust_mildly diseased', ' Common Rust_moderately diseased', ' Common Rust_severely diseased', ' Gray Leaf  Spot_mildly diseased', ' Gray Leaf  Spot_moderately diseased', ' Gray Leaf  Spot_severely diseased', ' blight_moderately diseased', ' blight_severely diseased', 'Healthy']
        image_path = fullpath
        new_img = load_img(image_path, target_size=(224, 224))

        img = img_to_array(new_img)

        img = np.expand_dims(img, axis=0)
        img = img/255
        print(img.shape)
        prediction0 = classifier0.predict(img)
        prediction0
        d = prediction0.flatten()
        j = d.max()
        for index,item in enumerate(d):
          if item == j:
           class_name0 = li0[index]
        print(class_name0)

        
        print('The matched plant type disease class is',class_name0)
        return render(request,'result.html',{
            'uploaded':class_name0
        })
        
    return render(request,'home.html') 

def contact(request):
   return render(request,'contact.html')

def about(request):
   return render(request,'about.html')

def upload(request):
   return render(request,'upload.html')

def upload1(request):
   return render(request,'upload1.html')

def tomato(request):
   return render(request,'tomato.html')

def chilli(request):
   return render(request,'chilli.html')

def rice(request):
   return render(request,'rice.html')

def corn(request):
   return render(request,'corn.html')
    