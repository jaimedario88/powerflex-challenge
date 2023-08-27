from django.db import models


class Factory(models.Model):
    name = models.CharField(
        verbose_name=("name"),
        max_length=1023,
    )

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "factories"


class Sprocket(models.Model):
    factory = models.ForeignKey(to=Factory, on_delete=models.CASCADE)
    teeth = models.IntegerField(verbose_name=("teeth"))
    pitch_diameter = models.DecimalField(
        verbose_name=("pitch diameter"), max_digits=10, decimal_places=4
    )
    outside_diameter = models.DecimalField(
        verbose_name=("pitch diameter"), max_digits=10, decimal_places=4
    )
    pitch = models.IntegerField(verbose_name=("pitch"))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]


class FactoryProductionRecord(models.Model):
    factory = models.ForeignKey(to=Factory, on_delete=models.CASCADE)
    sprocket_production_actual = models.IntegerField(
        verbose_name=("current sprocket production")
    )
    sprocket_production_goal = models.IntegerField(
        verbose_name=("sprocket production goal")
    )
    timestamp = models.DateTimeField()
