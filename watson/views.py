from django.shortcuts import render
from watson_developer_cloud import VisualRecognitionV3 as vr

# Create your views here.


def image_recognition(request):
    query = request.GET.get("q")
    args = {}
    if query:
        instance = vr(api_key='119030bac8e38e1721e61e0f6a295e18e5d9ecdf', version='2016-05-20')
        img = instance.classify(images_url=query)
        args = {'images': img['images'][0]['classifiers'][0]['classes']}
    return render(request, 'watson/image_recognition.html', args)
