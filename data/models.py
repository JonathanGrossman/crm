from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from datetime import datetime

class Analysis(models.Model):
    total_students = models.IntegerField()
    
    existing_alchemy = models.IntegerField()
    existing_animation = models.IntegerField()
    existing_conjuror = models.IntegerField()
    existing_disintegration = models.IntegerField()
    existing_elemental = models.IntegerField()
    existing_healing = models.IntegerField()
    existing_illusion = models.IntegerField()
    existing_immortality = models.IntegerField()
    existing_invisibility = models.IntegerField()
    existing_invulnerability = models.IntegerField()
    existing_necromancer = models.IntegerField()
    existing_omnipresent = models.IntegerField()
    existing_omniscient = models.IntegerField()
    existing_poison = models.IntegerField()
    existing_possession = models.IntegerField()
    existing_self_detonation = models.IntegerField()
    existing_summoning = models.IntegerField()
    existing_water_breathing = models.IntegerField()

    desired_alchemy = models.IntegerField()
    desired_animation = models.IntegerField()
    desired_conjuror = models.IntegerField()
    desired_disintegration = models.IntegerField()
    desired_elemental = models.IntegerField()
    desired_healing = models.IntegerField()
    desired_illusion = models.IntegerField()
    desired_immortality = models.IntegerField()
    desired_invisibility = models.IntegerField()
    desired_invulnerability = models.IntegerField()
    desired_necromancer = models.IntegerField()
    desired_omnipresent = models.IntegerField()
    desired_omniscient = models.IntegerField()
    desired_poison = models.IntegerField()
    desired_possession = models.IntegerField()
    desired_self_detonation = models.IntegerField()
    desired_summoning = models.IntegerField()
    desired_water_breathing = models.IntegerField()

    alchemy_basics = models.IntegerField()
    alchemy_advanced = models.IntegerField()
    magic_day_to_day = models.IntegerField()
    magic_for_medical = models.IntegerField()
    dating_with_magic = models.IntegerField()
    def __str__(self):
        return "Data"