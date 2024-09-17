from django.db import models


class Category(models.Model):
    description = models.CharField(verbose_name='Категория выполнения', max_length=200)
    name = models.CharField(verbose_name='Название категории', max_length=100)


class Task(models.Model):
    title = models.CharField(verbose_name='Название задачи', unique_for_date=True, max_length=200)
    description = models.TextField(verbose_name='Описание задачи')
    categories = models.ManyToManyField(Category)
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done'),
    ]
    status = models.CharField(choices=STATUS_CHOICES, max_length=250, default='New')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


class SubTask(models.Model):
    description = models.CharField(verbose_name='Отдельная часть основной задачи', max_length=100)
    title = models.CharField(verbose_name='Название подзадачи', max_length=100)
    #description = models.TextField(verbose_name='Описание подзадачи', max_length=100)
    task = models.ForeignKey(Task, verbose_name='Основная задача:Один ко многим', on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('New', 'new'),
        ('In progress', 'in progress'),
        ('Pending', 'pending'),
        ('Blocked', 'blocked'),
        ('Done', 'done'),
    ]
    status = models.CharField(choices=STATUS_CHOICES, max_length=250, default='New')
    deadline = models.DateField()
    created_at = models.DateField(auto_now_add=True)


