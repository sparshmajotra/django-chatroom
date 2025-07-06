from django.shortcuts import render, redirect
from .models import Message



def join_chat(request):
    if request.method == "POST":
        username = request.POST.get("username")
        if username:
            request.session["username"] = username
            return redirect("chatroom")
    return render(request, "chat/join.html")



def chatroom(request):
    username = request.session.get("username", None)
    if not username:
        return redirect("join_chat")

    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            Message.objects.create(username=username, text=text)
        return redirect("chatroom")

    messages = Message.objects.order_by('-timestamp')[:50]
    return render(request, "chat/chatroom.html", {"messages": messages, "username": username})



def logout_chat(request):
    request.session.flush()
    return redirect('join_chat')


