import factory.fuzzy

from .models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    role = factory.fuzzy.FuzzyChoice(User.Role)
    username = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = factory.Faker('password', length=10)


class BuyerFactory(UserFactory):
    role = User.Role.BUYER


class ReaderFactory(UserFactory):
    role = User.Role.READER