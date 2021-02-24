

from django.urls import path, include

from . import views

from .feeds import NewestFeed, FrontPageFeed

urlpatterns = [
    path('', views.index, name="index"),
    path('newest', views.newest, name="newest"),
    path('threads', views.threads, name="threads"),
    path('comments', views.comments, name="comments"),
    path('show', views.show, name="show"),
    path('ask', views.ask, name="ask"),
    path('zen', views.zen, name="zen"),
    path('item/<uuid:pk>', views.item, name="item"),
    path('item/<uuid:pk>/upvote', views.upvote, name="upvote"),
    path('item/<uuid:pk>/downvote', views.downvote, name="downvote"),
    path('item/<uuid:pk>/edit', views.item_edit, name="edit"),
    path('item/<uuid:pk>/delete', views.item_delete, name="delete"),
    path('submit', views.submit, name="submit"),

    path('newest/feed/', NewestFeed()),
    path('feed/', FrontPageFeed()),

    path('robots.txt', views.robots_txt, name="robots_txt"),
    path('humans.txt', views.humans_txt, name="humans_txt"),
    path('bookmarklet', views.bookmarklet, name="bookmarklet"),

    # Mixpanel API proxy
    path('lib.min.js', views.js_lib_minified),
    path('lib.js', views.js_lib),
    path('proxy/<str:endpoint>/', views.api_request),
]
