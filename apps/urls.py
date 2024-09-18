from django.urls import path
from apps.views import home, PortfolioDetailsView, BlogSingleView

urlpatterns = [
    path("", home, name="home"),
    path("portfolio_details/<int:id>", PortfolioDetailsView, name="portfolio_details"),
    path("blog_single/<int:id>", BlogSingleView, name="blog"),
]
