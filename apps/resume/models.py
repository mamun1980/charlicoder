from typing import Any
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


SKILLTYPE = (
    ('frontend', 'FrontEnd'),
    ('backend', 'BackEnd'),
    ('devops', 'DevOps'),
    ('other', 'Other')
)


class TopicManager(models.Manager):
    def create_or_new(self, title):
        title = title.strip()
        qs = self.get_queryset().filter(title__iexact=title)
        if qs.exists():
            return qs.first(), False
        return Topic.objects.create(title=title), True

    def comma_to_qs(self, topics_str):
        final_ids = []
        for topic in topics_str.split(','):
            obj, created = self.create_or_new(topic)
            final_ids.append(obj.id)
        qs = self.get_queryset().filter(id__in=final_ids).distinct()
        return qs


class Topic(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)

    objects = TopicManager()

    def __str__(self):
        return self.title


class Skill(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, null=False)
    rating = models.IntegerField(default=0, validators=[
                                 MaxValueValidator(10), MinValueValidator(0)])
    description = models.CharField(max_length=200, blank=True, null=True)
    skill_type = models.CharField(
        max_length=50, choices=SKILLTYPE, default='backend')

    def __str__(self):
        return self.name


class CandyProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=True)
    career_summary = RichTextField(blank=True, null=True)
    skype = models.CharField(max_length=50, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    github = models.URLField(max_length=200, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    codepen = models.URLField(blank=True, null=True)
    hackerrank = models.URLField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    nationality = CountryField(blank_label="(select country)")
    image = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def image_src(self):
        src = self.image.split('src="')[-1]
        src = src.split('" />')[0]
        return f"{src}"

    @property
    def full_name(self):
        first_name = self.user.first_name
        last_name = self.user.last_name
        return f"{first_name} {last_name}"

    @property
    def email(self):
        return f"{self.user.email}"

    @property
    def mobile(self):
        return f"{self.user.mobile}"

    @property
    def linkedin_username(self):
        url = self.linkedin.split('/in/')[-1] if self.linkedin else 'no data'
        return f"{url}"

    @property
    def github_username(self):
        url = self.github.split('/')[-1] if self.github else 'no data'
        return f"{url}"

    @property
    def codepen_username(self):
        url = self.codepen.split('/')[-1] if self.codepen else 'no data'
        return f"{url}"

    @property
    def hackerrank_username(self):
        url = self.hackerrank.split('/')[-1] if self.hackerrank else 'no data'
        return f"{url}"


class Education(models.Model):
    profile = models.ForeignKey(CandyProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False, null=False)
    institute_name = models.CharField(max_length=100, blank=False, null=False)
    enroll_year = models.DateField(blank=True, null=True)
    passing_year = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.profile.full_name}: {self.title}"


class WorkExperience(models.Model):
    profile = models.ForeignKey(CandyProfile, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50, blank=False, null=False)
    company_name = models.CharField(max_length=50, blank=False, null=False)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    is_currently_working = models.BooleanField(default=False)
    roles = models.TextField(max_length=1000, blank=True, null=True)
    achievements = RichTextField(max_length=1000, blank=True, null=True)
    technologies = models.ManyToManyField(Topic, blank=True)

    class Meta:
        ordering = ('from_date',)

    def __str__(self):
        return f"{self.profile.full_name}: {self.company_name}({self.job_title})"
