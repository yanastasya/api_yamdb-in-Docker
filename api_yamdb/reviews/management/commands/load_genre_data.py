from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import Genre


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Загрузка данных из genre.csv"

    def handle(self, *args, **options):

        if Genre.objects.exists():
            print('Данные уже загружены.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        # Show this before loading the data into the database
        print("Загрузка жанров.")

        for row in DictReader(open('./static/data/genre.csv')):
            genre = Genre(id=row['id'], name=row['name'], slug=row['slug'])
            genre.save()
