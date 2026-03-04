from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required


@login_required
def course_chat_room(request, course_id):
    try:
        # Pobranie kursu o identyfikatorze zgodnym z identyfikatorem kursu, do którego dołączył bieżący użytkownik.
        course = request.user.courses_joined.get(id=course_id)
    except:
        # Użytkownik nie jest uczestnikiem tego kursu lub kurs nie istnieje.
        return HttpResponseForbidden()
    return render(request, 'chat/room.html', {'course': course})
