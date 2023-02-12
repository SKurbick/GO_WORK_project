from django.forms import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

from reg_users.models import Profile, Report, Language


def create_profile(request):
    if request.method == "POST":
        profile = Profile()
        profile.first_name = request.POST.get("first_name")
        profile.last_name = request.POST.get("last_name")
        profile.telegram_link = request.POST.get("telegram_link")
        profile.save()
        print(profile.id)
        return HttpResponseRedirect(f"report/?profile_id={profile.id}")

    return render(request, "index.html")


def create_report(request):
    profile_id = request.GET.get("profile_id")
    context = {"profile_id": profile_id}
    if request.method == "POST":
        language = Language()
        report = Report()
        report.theme = request.POST.get("theme")
        report.description = request.POST.get("description")
        report.conclusion = request.POST.get("conclusion")
        report.what_learned = request.POST.get("what_learned")
        report.save()
        Language.objects.create(
            programming_language=request.POST.get("programming_language"),
            profile_id=int(profile_id),
            report_id=report.id
        )
        # language.programming_language = request.POST.get("programming_language")
        # language.profile = int(profile_id)
        # language.report = report.id
        # language.save()
        print(report.id)

    return render(request, "report.html", context)

# def add_language(request):
#     if request.method == "POST":
#         language = Language()
#         language.programming_language = request.POST.get("language")
#         language.save()
#     return render(request, "add_language.html")

# def get_id(request, get_id):
#     profiles = Profile.objects.filter(id=get_id)
#     context = {
#         "profiles": profiles
#     }
#     return render(request, "id.html", context)
