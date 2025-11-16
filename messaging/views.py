from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Message
from .forms import MessageForm


@login_required
def inbox(request):
    messages_qs = Message.objects.filter(receiver=request.user).select_related("sender")
    return render(request, "messaging/inbox.html", {"messages": messages_qs})


@login_required
def sent(request):
    messages_qs = Message.objects.filter(sender=request.user).select_related("receiver")
    return render(request, "messaging/sent.html", {"messages": messages_qs})


@login_required
def message_detail(request, pk):
    msg = get_object_or_404(Message, pk=pk)


    if msg.sender != request.user and msg.receiver != request.user:
        messages.error(request, "No tenés permiso para ver este mensaje.")
        return redirect("messaging:inbox")

    if msg.receiver == request.user and not msg.is_read:
        msg.is_read = True
        msg.save()

    return render(request, "messaging/message_detail.html", {"message": msg})


@login_required
def new_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            messages.success(request, "Mensaje enviado correctamente.")
            return redirect("messaging:sent")
    else:
        form = MessageForm()

    return render(request, "messaging/message_form.html", {"form": form})


@login_required
def reply_message(request, pk):
    """Responder a un mensaje existente."""
    original = get_object_or_404(Message, pk=pk)

    if original.sender != request.user and original.receiver != request.user:
        messages.error(request, "No tenés permiso para responder este mensaje.")
        return redirect("messaging:inbox")

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
          
            msg.receiver = original.sender
            msg.save()
            messages.success(request, "Respuesta enviada correctamente.")
            return redirect("messaging:sent")
    else:
        initial = {
            "receiver": original.sender,
            "subject": f"Re: {original.subject}",
        }
        form = MessageForm(initial=initial)

    return render(
        request,
        "messaging/message_form.html",
        {"form": form, "reply_to": original},
    )


@login_required
def delete_message(request, pk):
    """Eliminar un mensaje (solo remitente o destinatario)."""
    msg = get_object_or_404(Message, pk=pk)

  
    if msg.sender != request.user and msg.receiver != request.user:
        messages.error(request, "No tenés permiso para borrar este mensaje.")
        return redirect("messaging:inbox")

    if request.method == "POST":
        msg.delete()
        messages.success(request, "Mensaje eliminado correctamente.")
        return redirect("messaging:inbox")

    return render(request, "messaging/message_confirm_delete.html", {"message": msg})
