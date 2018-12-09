from django.db import models
# Create your models here.

class Topic(models.Model):
    '''Topic which usser lerning'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        ''' Returns models text '''
        return self.text

class Entry(models.Model):
    ''' Post by the Topic '''
    #topic = models.ForeignKey(Topic)
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        '''Returns sring view '''
        if len(self.text) > 50:
            return self.text[:50] + '...'
        else:
            return self.text    
