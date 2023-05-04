from email.policy import default
from enum import auto

from django.db import models


NULLABLE = {'blank': True, 'null': True}


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    deleted = models.BooleanField(default=False, verbose_name='Удален')

    class Meta:
        abstract = True
        ordering = ('-created_at',)


class NewsManager(models.Manager):
    def delete(self):
        pass

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class News(BaseModel):
    objects = NewsManager()

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    preamble = models.CharField(max_length=1000, verbose_name='Вступление')
    body = models.TextField(verbose_name='Содержимое')
    body_as_markdown = models.BooleanField(default=False, verbose_name='Способ разметки')

    def __str__(self) -> str:
        return f'#{self.pk} {self.title}'

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'


class CoursesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class Course(BaseModel):
    objects = CoursesManager()

    name = models.CharField(max_length=256, verbose_name='Name')
    description = models.TextField(verbose_name='Description', **NULLABLE)
    description_as_markdown = models.BooleanField(verbose_name='As markdown', default=False)
    cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Cost', default=0)
    cover = models.CharField(max_length=25, default='no_image.svg', verbose_name='Cover')

    def __str__(self) -> str:
        return f'{self.pk} {self.name}'

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    num = models.PositiveIntegerField(verbose_name='Lesson number')
    title = models.CharField(max_length=256, verbose_name='Name')
    description = models.TextField(verbose_name='Description', **NULLABLE)
    description_as_markdown = models.BooleanField(verbose_name='As markdown', default=False)

    def __str__(self) -> str:
        return f'{self.course.name} | {self.num} | {self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ('course', 'num')


class CourseTeachers(models.Model):
    course = models.ManyToManyField(Course)
    name_first = models.CharField(max_length=128, verbose_name='Name')
    name_second = models.CharField(max_length=128, verbose_name='Surname')
    day_birth = models.DateField(verbose_name='Birth date')
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return '{0:0>3} {1} {2}'.format(self.pk, self.name_second, self.name_first)

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta:
        verbose_name = 'учитель'
        verbose_name_plural = 'учителя'
