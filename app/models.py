from django.db import models


class BaseModel(models.Model):
    date_joined = models.DateTimeField('date joined', auto_now_add=True)

    class Meta:
        abstract = True

# Расписание групповых тренировок клуба
class TrainingClass(BaseModel):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    service = models.ForeignKey('Price', on_delete=models.CASCADE)
    trainer = models.ForeignKey('Staff', on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    recurring = models.BooleanField(default=False)
    date = models.CharField(max_length=100)

# Справочник персонала клуба
class Staff(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='staff_photos/')


# Справочник помещений
class Room(BaseModel):
    name = models.CharField(max_length=100)


# Справочник прайс-листа клуба
class Price(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
