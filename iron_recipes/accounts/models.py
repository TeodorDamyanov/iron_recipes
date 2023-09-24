from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import models as auth_models
from django.utils.translation import gettext_lazy as _

# Create your models here.


def only_alpha_validator(value):
    if not value.isalpha():
        raise ValidationError('Name must include only letters!')


class IronRecipeUser(auth_models.AbstractUser):
    NAMES_MIN_LENGTH = 2
    NAMES_MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=NAMES_MAX_LENGTH,
        validators=(validators.MinLengthValidator(NAMES_MIN_LENGTH), only_alpha_validator,)
    )

    last_name = models.CharField(
        max_length=NAMES_MAX_LENGTH,
        validators=(validators.MinLengthValidator(NAMES_MIN_LENGTH), only_alpha_validator,)
    )

    email = models.EmailField(
        unique=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    is_employee = models.BooleanField(
        _("employee status"),
        default=False,
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name or self.last_name:
            return self.first_name or self.last_name
        else:
            return self.username
