from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw



# Create your models here.

class Familia(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.name}'

class Producto(models.Model):
    name         = models.CharField(max_length=200,null=False,blank=False)
    description  = models.TextField(max_length=500, blank=True, null=True)
    tipo         = models.ForeignKey(Familia,on_delete=models.CASCADE, null=False, blank=False)
    pu           = models.IntegerField(default=0)
    image        = models.ImageField(upload_to='images/products/', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

class Website(models.Model):
    name = models.CharField(max_length=200)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return f'{self.name}'
    
    def save(self, *args, **kwargs):
        qrcode_img  = qrcode.make(self.name)
        canvas      = Image.new('RGB',(290,290),'white')
        draw        = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname       = f'qr_code-{self.name}.png'
        buffer      = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname,File(buffer),save=False)
        canvas.close()
        super().save(*args, **kwargs)
