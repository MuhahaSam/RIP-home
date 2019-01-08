from django.db import models
class user(models.Model):
    nickname = models.CharField(max_length = 20, unique=True)
    password = models.CharField(max_length=20, null=False)
    check = models.CharField(max_length=20, null=False)
    channel_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return '{}'.format(self.id)



class posts(models.Model):
    title = models.CharField(max_length = 20)
    contents = models.CharField(max_length=200)
    userid = models.ForeignKey(user,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=False)


    def __str__(self):
        return '{}'.format([self.title, self.contents, self.date, self.image])

    class Meta:
        ordering = ['-date']



class channel(models.Model):
    channel_name = models.CharField(max_length = 20)
    userid = models.ManyToManyField(user)

    def __str__(self):
        return '{}'.format(self.channel_name)


# Create your models here.
