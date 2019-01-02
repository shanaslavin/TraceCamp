from django.core.management.base import BaseCommand
import csv
from Kick.models import Kickstarter_camp


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('path', help='Path to CSV')

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, encoding="utf8") as csv_file:
            info = csv.reader(csv_file, delimiter=',')
            line = 0
            for row in info:
                if line != 0:
                    data = Kickstarter_camp.objects.create(
                        backers_count = int(row[0]),
                        blurb = row[1],
                        goal = row[11],
                        pledged = row[17])   
                line += 1

