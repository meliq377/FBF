from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'slider'
        verbose_name_plural = 'sliders'


class WhatWeDo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'what_we_do'


class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'about'


class OurServices(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'our_services'


class OurFinishedProjects(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'our_finished-projects'


class TeamPerson(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=500)
    img = models.ImageField(upload_to='media')
    skill = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'team_person'
        verbose_name_plural = 'team_persons'


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'team_persons'


class Experts(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=500)
    img = models.ImageField(upload_to='media')
    skill = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'team_person'
        verbose_name_plural = 'team_persons'
