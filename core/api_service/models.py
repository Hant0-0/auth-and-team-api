from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Назва команди')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команди'


class People(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Ім`я')
    last_name = models.CharField(max_length=100, verbose_name='Прізвище')
    email = models.EmailField(verbose_name='Email')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Команда')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Людина'
        verbose_name_plural = 'Люди'
