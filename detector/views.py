from django.shortcuts import render

from .models import ImageModel
from .ml_utils import detect
import os
import shutil
import tensorflow as tf
from pneumonia_detector_web.settings import BASE_DIR, MEDIA_ROOT
# Create your views here.
def index(request):
    return render(request, 'detector/index.html')

def analyze(request):
    is_post_request = False
    answer = 0
    if request.method == 'POST':
        # print(request.POST)
        # print(request.FILES)
        instances = ImageModel.objects.all()
        for instance in instances:
            instance.delete()
        shutil.rmtree(os.path.join(BASE_DIR, 'uploads'))
        files = request.FILES
        image = files.get("img")
        instance = ImageModel()
        instance.image = image
        instance.save()
        model = tf.keras.models.load_model(os.path.join(BASE_DIR, 'model/pneumonia_detector.h5'))
        answer = detect(model, os.path.join(MEDIA_ROOT, str(instance.image)))
        is_post_request = True

        context = {
            "instance":instance,
            "answer" : answer,
            "is_post_request":is_post_request,
        }

        return render(request, 'detector/analysisform.html', context)
    else:
        context = {
            "instance": None,
            "answer" : answer,
            "is_post_request":is_post_request,
        }
        return render(request, 'detector/analysisform.html', context)
