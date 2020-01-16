from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from datetime import datetime

class Analysis(models.Model):
    total_students = models.IntegerField(default=0)
    
    existing_alchemy = models.IntegerField(default=0)
    existing_animation = models.IntegerField(default=0)
    existing_conjuror = models.IntegerField(default=0)
    existing_disintegration = models.IntegerField(default=0)
    existing_elemental = models.IntegerField(default=0)
    existing_healing = models.IntegerField(default=0)
    existing_illusion = models.IntegerField(default=0)
    existing_immortality = models.IntegerField(default=0)
    existing_invisibility = models.IntegerField(default=0)
    existing_invulnerability = models.IntegerField(default=0)
    existing_necromancer = models.IntegerField(default=0)
    existing_omnipresent = models.IntegerField(default=0)
    existing_omniscient = models.IntegerField(default=0)
    existing_poison = models.IntegerField(default=0)
    existing_possession = models.IntegerField(default=0)
    existing_self_detonation = models.IntegerField(default=0)
    existing_summoning = models.IntegerField(default=0)
    existing_water_breathing = models.IntegerField(default=0)

    desired_alchemy = models.IntegerField(default=0)
    desired_animation = models.IntegerField(default=0)
    desired_conjuror = models.IntegerField(default=0)
    desired_disintegration = models.IntegerField(default=0)
    desired_elemental = models.IntegerField(default=0)
    desired_healing = models.IntegerField(default=0)
    desired_illusion = models.IntegerField(default=0)
    desired_immortality = models.IntegerField(default=0)
    desired_invisibility = models.IntegerField(default=0)
    desired_invulnerability = models.IntegerField(default=0)
    desired_necromancer = models.IntegerField(default=0)
    desired_omnipresent = models.IntegerField(default=0)
    desired_omniscient = models.IntegerField(default=0)
    desired_poison = models.IntegerField(default=0)
    desired_possession = models.IntegerField(default=0)
    desired_self_detonation = models.IntegerField(default=0)
    desired_summoning = models.IntegerField(default=0)
    desired_water_breathing = models.IntegerField(default=0)

    alchemy_basics = models.IntegerField(default=0)
    alchemy_advanced = models.IntegerField(default=0)
    magic_day_to_day = models.IntegerField(default=0)
    magic_for_medical = models.IntegerField(default=0)
    dating_with_magic = models.IntegerField(default=0)
    def __str__(self):
        return "Data"