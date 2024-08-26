from django.shortcuts import render


def sp_dashboard(request, url_id):
    return render(request, "sp_response.html")
