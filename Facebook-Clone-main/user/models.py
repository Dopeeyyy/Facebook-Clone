from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='default.jpg', 
        upload_to='profile_pics',  # Changed to a more standard upload path
        blank=True,  # Allow blank uploads
        null=True   # Allow null values
    )

    def save(self, *args, **kwargs):
        # Only try to resize if an image exists
        super().save(*args, **kwargs)
        
        try:
            if self.image:
                img = Image.open(self.image.path)
                # Your existing image resizing logic
                if img.height > 300 or img.width > 300:
                    output_size = (300, 300)
                    img.thumbnail(output_size)
                    img.save(self.image.path)
        except FileNotFoundError:
            # Handle case where image file is missing
            pass