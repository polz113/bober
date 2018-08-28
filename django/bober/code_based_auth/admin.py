from django.contrib import admin
from code_based_auth.models import CodeComponent, CodePart, CodeFormat, Code, CodeGenerator

# Register your models here.


class CodeComponentInline(admin.TabularInline):
    model = CodeComponent


class CodeFormatManager(admin.ModelAdmin):
    inlines = [CodeComponentInline]


class CodePartInline(admin.TabularInline):
    model = CodePart


class CodeManager(admin.ModelAdmin):
    inlines = [CodePartInline]


admin.site.register(CodeFormat, CodeFormatManager)
admin.site.register(Code, CodeManager)
admin.site.register(CodeGenerator)
