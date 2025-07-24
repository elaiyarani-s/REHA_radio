from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def chat_page(request):
    return render(request, 'chat/chat_page.html')

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

@method_decorator(staff_member_required, name='dispatch')
class AdminChatView(TemplateView):
    template_name = "admin_chat.html"
