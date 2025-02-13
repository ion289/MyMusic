from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.sites import requests
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from .forms import UserMessageForm, ReviewForm
from .mixins import UserIsReviewOwnerMixin
from .models import Album, News, UserMessage, Review
from django.db.models import Exists, OuterRef, Subquery


def home(request):
    # Query to fetch albums with reviews
    albums_with_reviews = Album.objects.filter(
        Exists(Review.objects.filter(album=OuterRef('pk')))
    ).annotate(
        latest_review=Subquery(
            Review.objects.filter(album=OuterRef('pk')).order_by('-published_date').values('review')[:1]
        ),
        reviewer=Subquery(
            Review.objects.filter(album=OuterRef('pk')).order_by('-published_date').values('user')[:1]
        ),
        reviewer_rating=Subquery(
            Review.objects.filter(album=OuterRef('pk')).order_by('-published_date').values('rating')[:1]
        ),
        review_published_date=Subquery(
            Review.objects.filter(album=OuterRef('pk')).order_by('-published_date').values('published_date')[:1]
        ),
    )

    context = {
        'albums': albums_with_reviews,
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create and save a new instance of User_Messages
        user_message = UserMessage(name=name, email=email, subject=subject, message=message)
        user_message.save()
        success = True
    return render(request, 'contact.html', {'success': success})


def chart(request):
    albums = Album.objects.order_by('-average_rating')
    context = {
        'albums': albums,
    }
    return render(request, 'chart.html', context)


def new_music(request):
    albums = Album.objects.order_by('-release_date')
    latest_music = {
        'albums': albums,
    }
    return render(request, 'new_music.html', latest_music)


def news(request):
    news = News.objects.order_by('-published_date')
    context = {
        'news': news
    }
    return render(request, 'news.html', context)

# class PostDetails(DetailView):
#     model = Post
#     template_name = 'posts_detail.html'

def album_detail(request, album_id):
    album = Album.objects.get(pk=album_id)
    reviews = Review.objects.filter(album=album).order_by('-pk')[:3]

    # Variabila care tine cont daca un user a postat deja un review
    # la aceasta postare
    user_already_reviewed = False

    for review in reviews:
        if review.user == request.user:
            user_already_reviewed = True

    return render(
        request,
        'album_detail.html',
        context={
            'object': album,
            'reviews': reviews,
            'user_already_reviewed': user_already_reviewed
        }
    )

class UserMessageCreateView(CreateView):
    template_name = 'usermessage.html'
    model = UserMessage
    form_class = UserMessageForm
    success_url = reverse_lazy('home')

@login_required()
def add_review_view(request, album_id):
        if request.method == 'POST':
            rating = request.POST['rating']
            review = request.POST['review']
            album = Album.objects.get(pk=album_id)

            Review.objects.create(
                rating=rating,
                review=review,
                album=album,
                user=request.user
            )

            return redirect('album-detail', album_id=album_id)
        else:
            return redirect('home')


class ReviewUpdateView(LoginRequiredMixin, UserIsReviewOwnerMixin, UpdateView):
        template_name = 'review_update.html'
        form_class = ReviewForm
        model = Review
        success_url = reverse_lazy('home')

class ReviewDeleteView(LoginRequiredMixin, UserIsReviewOwnerMixin, DeleteView):
        template_name = 'review_confirm_delete.html'
        model = Review
        success_url = reverse_lazy('home')

def see_all_reviews_view(request, post_id):
        album = Album.objects.get(pk=post_id)
        reviews = Review.objects.filter(album=album).order_by('-pk')

        return render(
            request,
            'all_review.html',
            context={
                'album': album,
                'reviews': reviews
            }
        )
class NewsDetails(DetailView):
       model = News
       template_name = 'news_details.html'