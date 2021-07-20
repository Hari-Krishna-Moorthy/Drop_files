from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from upload.models import Files
from upload.form import FilesForm
# Create your views here.

@login_required(login_url='/login/')
def upload_view(request):
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
            formstatus = form.save(commit=False)
            formstatus.user = request.user
            formstatus.save()

            return redirect('home')

    form = FilesForm()
    return render(request, 'upload/upload.html', {
        "form" : form,
        "title" : "upload"
    })