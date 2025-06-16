from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This command populates the database with categories data posts."
    def handle(self, *args: Any, **options: Any):
        # data delete exisit data
        Category.objects.all().delete()
        # 

   
#  catogories

        categories = ['Sports','Technology','Science','Art','Food','Travel','History','Entertainment','Politics','Business','Health','Education','Environment','Culture','Religion','Sports','Technology','Science','Art','Food','Travel','History','Entertainment','Politics','Business','Health','Education','Environment','Culture','Religion']
        for category_name in categories:
            Category.objects.create(name=category_name)

        self.stdout.write(self.style.SUCCESS("Completed inserting data"))

