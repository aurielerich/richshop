from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_project' : "Rich Shop",
        'npm' : '2406428806',
        'name': 'Auriel Erich Ibrahim Nst',
        'class': 'PBP F',
    }

    return render(request, "main.html", context)