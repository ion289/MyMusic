from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic
from django.forms import CharField, Textarea

from accounts.models import Profile


class SignUpForm(UserCreationForm):
    # field-urile care apar in formular din clasa de user
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    biography = CharField(widget=Textarea)

    # Suprascriem functia save() din clasa UserCreationForm
    # commit=True inseamna ca schimbarile vor fi scrise in baza de date

    # @atomic ne asigura ca se produc schimbari in baza de date
    # doar daca niciunul din modele nu a avut erori cand se salveaza
    @atomic
    def save(self, commit=True):
        # Salvam obiectul User care provine din django
        user = super().save(commit)

        data_biography = self.cleaned_data['biography']

        # Cream un obict Profile in care adaugam datele noastre extra
        profile = Profile(biography=data_biography, user=user)
        if commit:
            profile.save()

        return user
