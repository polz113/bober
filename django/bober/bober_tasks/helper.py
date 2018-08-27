__author__ = 'Peter'
from bober_tasks.models import Category, AgeGroup, DifficultyLevel


def all_cat():
    return Category.objects.distinct()


def all_ages():
    return AgeGroup.objects.distinct()


def all_dif():
    return DifficultyLevel.objects.all()
