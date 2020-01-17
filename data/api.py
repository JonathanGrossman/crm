from data.models import Analysis
from students.models import Student
from rest_framework import viewsets, permissions
from .serializers import DataSerializer
from django.core.exceptions import ObjectDoesNotExist as DoesNotExist
from django.db.models import Count

existing_skills_count = [
            {"name": "Alchemy",
            "count": 0
            },
            {"name": "Animation",
            "count": 0
            },
            {"name": "Conjuror",
            "count": 0
            },
            {"name": "Disintegration",
            "count": 0
            },
            {"name": "Elemental",
            "count": 0
            },
            {"name": "Healing",
            "count": 0
            },
            {"name": "Illusion",
            "count": 0
            },
            {"name": "Immortality",
            "count": 0
            },
            {"name": "Invisibility",
            "count": 0
            },
            {"name": "Invulnerability",
            "count": 0
            },
            {"name": "Necromancer",
            "count": 0
            },
            {"name": "Omnipresent",
            "count": 0
            },
            {"name": "Omniscient",
            "count": 0
            },
            {"name": "Poison",
            "count": 0
            },
            {"name": "Possession",
            "count": 0
            },
            {"name": "Self-detonation",
            "count": 0
            },
            {"name": "Summoning",
            "count": 0
            },
            {"name": "Water breathing",
            "count": 0
            }
    ]

desired_skills_count = [
            {"name": "Alchemy",
            "count": 0
            },
            {"name": "Animation",
            "count": 0
            },
            {"name": "Conjuror",
            "count": 0
            },
            {"name": "Disintegration",
            "count": 0
            },
            {"name": "Elemental",
            "count": 0
            },
            {"name": "Healing",
            "count": 0
            },
            {"name": "Illusion",
            "count": 0
            },
            {"name": "Immortality",
            "count": 0
            },
            {"name": "Invisibility",
            "count": 0
            },
            {"name": "Invulnerability",
            "count": 0
            },
            {"name": "Necromancer",
            "count": 0
            },
            {"name": "Omnipresent",
            "count": 0
            },
            {"name": "Omniscient",
            "count": 0
            },
            {"name": "Poison",
            "count": 0
            },
            {"name": "Possession",
            "count": 0
            },
            {"name": "Self-detonation",
            "count": 0
            },
            {"name": "Summoning",
            "count": 0
            },
            {"name": "Water breathing",
            "count": 0
            }
    ]

school_courses = [
        {"name": "Alchemy basics",
        "count": 0},
        {"name": "Alchemy advanced",
        "count": 0},
        {"name": "Magic for day-to-day life",
        "count": 0},
        {"name": "Magic for medical professionals",
        "count": 0},
        {"name": "Dating with magic",
        "count": 0}
    ]


class DataViewSet(viewsets.ModelViewSet):
    global existing_skills_count
    def existing_skills_loop(skills):
        for type in skills:
            for item in existing_skills_count:
                if type["selectedName"] == item["name"]:
                    item["count"] += 1
    
    def set_existing_skills_loop(skills):
        data = Analysis.objects.get(pk=3)
        for type in skills:
            for item in existing_skills_count:
                if item["name"] == "Alchemy":
                    data.existing_alchemy = item["count"]
                    data.save()
                if item["name"] == "Animation":
                    data.existing_animation = item["count"]
                    data.save()
                if item["name"] == "Conjuror":
                    data.existing_conjuror = item["count"]
                    data.save()
                if item["name"] == "Disintegration":
                    data.existing_disintegration = item["count"]
                    data.save()
                if item["name"] == "Elemental":
                    data.existing_elemental = item["count"]
                    data.save()
                if item["name"] == "Healing":
                    data.existing_healing = item["count"]
                    data.save()
                if item["name"] == "Illusion":
                    data.existing_illusion = item["count"]
                    data.save()
                if item["name"] == "Immortality":
                    data.existing_immortality = item["count"]
                    data.save()
                if item["name"] == "Invisibility":
                    data.existing_invisibility = item["count"]
                    data.save()
                if item["name"] == "Invulnerability":
                    data.existing_invulnerability = item["count"]
                    data.save()
                if item["name"] == "Necromancer":
                    data.existing_necromancer = item["count"]
                    data.save()
                if item["name"] == "Omnipresent":
                    data.existing_omnipresent = item["count"]
                    data.save()
                if item["name"] == "Omniscient":
                    data.existing_omniscient = item["count"]
                    data.save()
                if item["name"] == "Poison":
                    data.existing_poison = item["count"]
                    data.save()
                if item["name"] == "Possession":
                    data.existing_possession = item["count"]
                    data.save()
                if item["name"] == "Self-detonation":
                    data.existing_self_detonation = item["count"]
                    data.save()
                if item["name"] == "Summoning":
                    data.existing_summoning = item["count"]
                    data.save()
                if item["name"] == "Water breathing":
                    data.existing_water_breathing = item["count"]
                    data.save()

    def desired_skills_loop(skills):
            for type in skills:
                for item in desired_skills_count:
                    if type["selectedName"] == item["name"]:
                        item["count"] += 1

    def set_desired_skills_loop(skills):
        data = Analysis.objects.get(pk=3)
        for type in skills:
            for item in desired_skills_count:
                if item["name"] == "Alchemy":
                    data.desired_alchemy = item["count"]
                    data.save()
                if item["name"] == "Animation":
                    data.desired_animation = item["count"]
                    data.save()
                if item["name"] == "Conjuror":
                    data.desired_conjuror = item["count"]
                    data.save()
                if item["name"] == "Disintegration":
                    data.desired_disintegration = item["count"]
                    data.save()
                if item["name"] == "Elemental":
                    data.desired_elemental = item["count"]
                    data.save()
                if item["name"] == "Healing":
                    data.desired_healing = item["count"]
                    data.save()
                if item["name"] == "Illusion":
                    data.desired_illusion = item["count"]
                    data.save()
                if item["name"] == "Immortality":
                    data.desired_immortality = item["count"]
                    data.save()
                if item["name"] == "Invisibility":
                    data.desired_invisibility = item["count"]
                    data.save()
                if item["name"] == "Invulnerability":
                    data.desired_invulnerability = item["count"]
                    data.save()
                if item["name"] == "Necromancer":
                    data.desired_necromancer = item["count"]
                    data.save()
                if item["name"] == "Omnipresent":
                    data.desired_omnipresent = item["count"]
                    data.save()
                if item["name"] == "Omniscient":
                    data.desired_omniscient = item["count"]
                    data.save()
                if item["name"] == "Poison":
                    data.desired_poison = item["count"]
                    data.save()
                if item["name"] == "Possession":
                    data.desired_possession = item["count"]
                    data.save()
                if item["name"] == "Self-detonation":
                    data.desired_self_detonation = item["count"]
                    data.save()
                if item["name"] == "Summoning":
                    data.desired_summoning = item["count"]
                    data.save()
                if item["name"] == "Water breathing":
                    data.desired_water_breathing = item["count"]
                    data.save()

    def interested_courses_loop(skills):
            for type in skills:
                for item in school_courses:
                    if type["selectedName"] == item["name"]:
                        item["count"] += 1

    def set_interested_courses_loop(skills):
        data = Analysis.objects.get(pk=3)
        for type in skills:
            for item in school_courses:
                if item["name"] == "Alchemy basics":
                    data.alchemy_basics = item["count"]
                    data.save()
                if item["name"] == "Alchemy advanced":
                    data.alchemy_advanced = item["count"]
                    data.save()
                if item["name"] == "Magic for day-to-day life":
                    data.magic_day_to_day = item["count"]
                    data.save()
                if item["name"] == "Magic for medical professionals":
                    data.magic_for_medical = item["count"]
                    data.save()
                if item["name"] == "Dating with magic":
                    data.dating_with_magic = item["count"]
                    data.save()
                    
    try:
        # RETRIEVE FROM STUDENTS TABLE
        students = Student.objects.all()

        for i in range(len(students)):
            existing_skills_loop(students[i].existing_skills)
            set_existing_skills_loop(students[i].existing_skills)
            desired_skills_loop(students[i].desired_skills)
            set_desired_skills_loop(students[i].desired_skills)
            interested_courses_loop(students[i].interested_courses)
            set_interested_courses_loop(students[i].interested_courses)

        data = Analysis.objects.get(pk=3)
        data.total_students = len(students)
        data.save()
        queryset = Analysis.objects.all()

        permission_classes = [
            permissions.AllowAny
        ]

    except Student.DoesNotExist:
        queryset = None
        permission_classes = [
            permissions.AllowAny
        ]

    except Analysis.DoesNotExist:
        queryset = None
        permission_classes = [
            permissions.AllowAny
        ]

    serializer_class = DataSerializer