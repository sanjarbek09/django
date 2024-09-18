from django.shortcuts import render, redirect
from django.urls import reverse
from httpx import post
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

from apps.models import (
    User,
    Skills,
    Service,
    Priz,
    Portfolio,
    BlogSingle,
    Blog,
    Opinion,
)


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        full_message = f"{email} dan sizga quyidagi habar keldi:\n\n\n{message}"

        try:
            send_mail(
                f"{name} sizga habar yubordi.",
                full_message,
                settings.EMAIL_HOST_USER,
                [
                    settings.EMAIL_HOST_USER,
                ],
                fail_silently=False,
            )
            return redirect("home")
        except Exception as e:
            print(f"Email yuborishda xato: {e}")
            return HttpResponse(f"Xato yuz berdi: {e}")

    users = User.objects.first()
    skills = Skills.objects.all()
    services = Service.objects.all()
    priz = Priz.objects.all()
    portfolio = Portfolio.objects.all()
    blog = Blog.objects.all()
    opinions = Opinion.objects.all()
    # all_users = User.objects.all()
    return render(
        request,
        "index.html",
        {
            "user": users,
            "skills": skills,
            "services": services,
            "prizs": priz,
            "portfolios": portfolio,
            "blogs": blog,
            "opinions": opinions,
        },
    )


def PortfolioDetailsView(request, id):
    portfolios = Portfolio.objects.all()
    portfolio = Portfolio.objects.filter(id=id).first()

    return render(
        request,
        "portfolio-details.html",
        {"portfolio": portfolio, "portfolios": portfolios},
    )


def BlogSingleView(request, id):
    blog_singles = BlogSingle.objects.all()
    blog_single = BlogSingle.objects.filter(id=id).first()
    blog = Blog.objects.first()
    users = User.objects.first()

    return render(
        request,
        "blog-single.html",
        {
            "blog_singles": blog_singles,
            "blog_single": blog_single,
            "blogs": blog,
            "user": users,
        },
    )
