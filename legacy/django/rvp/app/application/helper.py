__author__ = 'Peter'
from models import Category, AgeGroup, Language, DifficultyLevel

def all_cat():
    return Category.objects.distinct()

def all_ages():
    return AgeGroup.objects.distinct()

def all_lang():
    return Language.objects.all()

def all_dif():
    return DifficultyLevel.objects.all()