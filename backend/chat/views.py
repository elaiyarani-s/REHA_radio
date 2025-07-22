from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def chat_page(request):
    return render(request, 'chat/chat_page.html')
