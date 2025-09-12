from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatGroup
from .forms import ChatmessageCreateForm   # 👈 fixed import


@login_required
def chat_view(request):   
    chat_group = get_object_or_404(ChatGroup, group_name="public-chat")
    chat_messages = chat_group.chat_messages.all()[:30] 

    if request.htmx:   # 👈 fixed
        form = ChatmessageCreateForm(request.POST)   # 👈 fixed
        if form.is_valid():        # 👈 fixed
            message = form.save(commit=False)
            message.author = request.user   # 👈 fixed
            message.group = chat_group
            message.save()
            context ={
                'message' : message,
                'user' : request.user

            }
            return render(request, 'a_rtchat/partials/chat_message_p.html', context)

    else:
        form = ChatmessageCreateForm()

    return render(request, 'a_rtchat/chat.html', {
        'chat_messages': chat_messages,
        'form': form
    })
