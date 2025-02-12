from django.contrib.auth.mixins import UserPassesTestMixin

from myapp.models import Review


class UserIsReviewOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        review = Review.objects.get(pk=self.kwargs['pk'])
        if self.request.user == review.user:
            return True

        return False