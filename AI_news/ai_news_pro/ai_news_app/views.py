from django.shortcuts import render
from django.http import JsonResponse
import requests

def index(request):
    return render(request, "index.html")

def get_news(request):
    category = request.GET.get("category", "technology")  # business, sports, health, etc.
    api = "9fbb7f2d49c04c2795b339f9a5ed6c65"
    url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={api}"

    try:
        r = requests.get(url)
        r.raise_for_status()
        articles = r.json().get("articles", [])
        simplified = [
            {"title": a.get("title"), "url": a.get("url")}
            for a in articles if a.get("title")
        ]
        return JsonResponse({"articles": simplified})
    except Exception as e:
        return JsonResponse({"error": str(e)})
