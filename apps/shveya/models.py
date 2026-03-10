from django.db import models

# Create your models here.

class Party(models.Model):
    batch_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    design = models.CharField(max_length=100)

    def __str__(self):
        return f"Batch {self.batch_number} - {self.design}"

class Material(models.Model):
    party = models.ForeignKey(
        Party,
        on_delete=models.CASCADE,
        related_name="materials"
    )

    color = models.CharField(max_length=50)
    quantity_line = models.IntegerField()
    tshirt_count = models.IntegerField()

    four_x = models.CharField(max_length=50, blank=True)
    four_x_count = models.IntegerField(null=True, blank=True)

    raspash = models.CharField(max_length=50, blank=True)
    raspash_count = models.IntegerField(null=True, blank=True)

    beika = models.CharField(max_length=50, blank=True)
    beika_count = models.IntegerField(null=True, blank=True)

    strochka =  models.CharField(max_length=50, blank=True)
    strochka_count = models.IntegerField(null=True, blank=True)

    gorlo = models.CharField(max_length=50, blank=True)
    gorlo_count = models.IntegerField(null=True, blank=True)

    ytyg = models.CharField(max_length=50, blank=True)
    ytyg_count = models.IntegerField(null=True, blank=True)

    otk = models.CharField(max_length=50, blank=True)
    otk_count = models.IntegerField(null=True, blank=True)

    ypakovka = models.CharField(max_length=50, blank=True)
    ypakovka_count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.party.batch_number} - {self.color}"