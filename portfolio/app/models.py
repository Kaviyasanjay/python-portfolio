from django.db import models

class SectionContent(models.Model):
    SECTION_CHOICES = [
        ('home', 'Home'),
        ('about', 'About'),
        ('education', 'Education'),
        ('experience', 'Experience'),
        ('contact', 'Contact'),
    ]
    section = models.CharField(max_length=50, choices=SECTION_CHOICES, unique=True)
    title = models.CharField(max_length=200)
    # description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='section_images/')

    def __str__(self):
        return self.section
