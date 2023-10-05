# chatapp/views.py

from django.shortcuts import render
# from django.http import HttpResponse
# import streamlit as st
import openai

openai.api_key = "YOUR_API_KEY"


def chatbot_view(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt', '')
        if prompt:
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="512x512"
            )
            image_url = response['data'][0]['url']
            return render(request, 'chatbot.html', {'image_url': image_url})

    return render(request, 'chatbot.html')
