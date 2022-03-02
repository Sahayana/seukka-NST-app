from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from django.shortcuts import render, redirect
from .models import Painting, User
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.views.generic import ListView

from .models import Painting, User


# Create your views here.


def sign_up_or_in(request):
    if request.user.is_authenticated:
        return redirect(reverse("paintings:home"))

    most_liked_paint = Painting.objects.all().order_by("-like_count")
    if most_liked_paint:
        return render(request, "sign_up_or_in.html", {"paint": most_liked_paint[0].image})

    return render(request, "sign_up_or_in.html")


@method_decorator(login_required, name="dispatch")
class HomeView(ListView):
    model = Painting
    template_name = "home.html"
    paginate_by = 2

    def get_ordering(self):
        ordering = self.request.GET.get("ordering", "-created")
        # validate ordering here
        return ordering

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ordering"] = self.request.GET.get("ordering", "-created")
        return context


# def home(request):
#     paintings = Painting.objects.all()
#     return render(request, "home.html", {"paintings": paintings})


@login_required(login_url="/")
def create(request):
    if request.method == "POST":
        img_file = request.FILES["img"]
        img_file.name = request.POST["title"]
        Painting.objects.create(owner_id=request.user.id, image=img_file)
        return JsonResponse({"msg": "success"})
    return render(request, "create.html")


@login_required(login_url="/")
def mypage(request, username):
    try:
        user = User.objects.get(username=username)
        paintings = user.paintings.all().order_by("-created")
        return render(request, "mypage.html", {"paintings": paintings, "user": user})
    except User.DoesNotExist:
        return render(request, "404.html")


def log_out(request):
    print("hi")
    if request.user.is_authenticated:
        print("ho")
        logout(request)
    return redirect(reverse("paintings:sign_up_or_in"))


def avatar(request):

    image = request.FILES["img"]
    user = User.objects.get(pk=request.user.id)
    user.avatar = image
    user.save()

    return redirect(reverse("paintings:mypage", args=[user.username]))
