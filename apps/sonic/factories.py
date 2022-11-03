import factory
from django.contrib.auth.hashers import make_password
from .models import Interest, User

class SonicUserFactory(factory.django.DjangoModelFactory):
    """
    Creates a standard active user.
    """
    class Meta:
        model = SonicUser

    first_name = 'Rafin '
    last_name = 'Irfan'
    # Emails must be unique - so use a sequence here:
    email = factory.Sequence(lambda n: 'user.{}@test.test'.format(n))
    # password = make_password('pass')
    is_active = True

    @factory.post_generation
    def interests(self, create, extracted, **kwargs):
        """
        Where 'interests' are defined, add them to this user.
        """
        if not create:
            return

        if extracted:
            for interest in extracted:
                self.interest.add(interest)

class InterestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Interest

    name = factory.Sequence(lambda n: 'interest{}'.format(n))


# Create a User with the default settings
user = SonicUserFactory() # Will generate a user with the name 'Standard User'

# Create a User with a custom name
major_tom = SonicUserFactory(first_name='Major', last_name='Tom')

# Create a User with Interests
django = InterestFactory(name='Django')
public_speaking = InterestFactory(name='Public Speaking')
lucy_diamond = SonicUserFactory(first_name='Lucy', last_name='Diamond',
                           interests=(django, public_speaking))