from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import User


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Загрузка данных из users.csv"

    def handle(self, *args, **options):

        for row in DictReader(
            open('./static/data/users.csv', encoding='utf-8')
        ):
            user = User(
                id=row['id'],
                username=row['username'],
                email=row['email'],
                role=row['role'],
                bio=row['bio'],
                first_name=row['first_name'],
                last_name=row['last_name']
            )
            user.save()
