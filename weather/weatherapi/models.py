from django.db import models

class Weather(models.Model):
    location =  models.CharField('Место положение', max_length=60)
    weather =  models.CharField('Погода', max_length=60)
    date =  models.DateField('Дата')
    temperature =  models.CharField('Температура', max_length=10)
    weather_feel =  models.CharField('По ощущению', max_length=60)
    parse_date =  models.DateTimeField('Время парсинга')

    def __str__(self):
        return f'{self.location} {self.weather}'

    class Meta:

        verbose_name = "Погода"
        verbose_name_plural = "Погода"
