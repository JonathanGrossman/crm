from data.models import Analysis
from students.models import Student
from rest_framework import viewsets, permissions
from .serializers import DataSerializer
from django.core.exceptions import ObjectDoesNotExist as DoesNotExist
from django.db.models import Count

magic_skills = [
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
        "Alchemy basics",
        "Alchemy advanced",
        "Magic for day-to-day life",
        "Magic for medical professionals",
        "Dating with magic"
    ]


class DataViewSet(viewsets.ModelViewSet):
    global magic_skills
    def skills_loop(skills):
        for type in skills:
            print(type)
            for item in magic_skills:
                if type["selectedName"] == item["name"]:
                    item["count"] += 1
                    print(item["count"], item["name"])
    
    
    try:
        # RETRIEVE FROM STUDENTS TABLE
        students = Student.objects.all()
        ## EXISTING SKILLS
        for i in range(len(students)):
            print(students[i].existing_skills)
            skills_loop(students[i].existing_skills)

        # SAVE TO DATA TABLE    
        data = Analysis.objects.get(pk=3)
        data.total_students = len(students)
        data.save()
        queryset = Analysis.objects.all()
        # print(queryset[0].total_students)
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