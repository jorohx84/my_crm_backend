from django.db import models, transaction
from django.conf import settings
import random

COLOR_PALETTE = [
    "#1F77B4", "#FF7F0E", "#2CA02C", "#D62728", "#9467BD",
    "#8C564B", "#E377C2", "#7F7F7F", "#BCBD22", "#17BECF",
    "#393B79", "#637939", "#8C6D31", "#843C39", "#7B4173",
    "#3182BD", "#31A354", "#756BB1", "#E6550D", "#636363",
    "#9C9EDE", "#F7B6D2", "#CEDB9C", "#FF9896", "#C5B0D5",
    "#C49C94", "#F7B174", "#A1D99B", "#A6CEE3", "#FDBF6F",
    "#B2DF8A", "#FB9A99", "#CAB2D6", "#6A3D9A", "#FF7F00",
    "#B15928", "#8DD3C7", "#FFFFB3", "#BEBADA", "#FB8072",
    "#80B1D3", "#FDB462", "#B3DE69", "#FCCDE5", "#D9D9D9"
]

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=255, blank=True, default="")
    last_name = models.CharField(max_length=255, blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, null=True, default="")
    email = models.EmailField(max_length=50, blank=True, default="")
    department = models.CharField(default="", null=True, blank=True)
    last_logout = models.CharField(default='1900-01-01T00:00:00.000Z')
    last_inbox_check = models.CharField(default='1900-01-01T00:00:00.000Z')
    color = models.CharField(max_length=7, unique=True)
    
    @staticmethod
    def _generate_random_hex_color():
        return "#" + ''.join(random.choices("0123456789ABCDEF", k=6))

    @classmethod
    def _get_unique_color(cls):
        with transaction.atomic():
            used_colors = set(
                cls.objects.select_for_update().values_list("color", flat=True)
            )

            # Zuerst Palette verwenden
            for color in COLOR_PALETTE:
                if color not in used_colors:
                    return color

            # Wenn Palette voll → unendlich neue Farben generieren
            while True:
                new_color = cls._generate_random_hex_color()
                if new_color not in used_colors:
                    return new_color

    def save(self, *args, **kwargs):
        if not self.color:
            self.color = self._get_unique_color()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip()