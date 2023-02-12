from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import Comment, User, Review


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Загрузка данных из category.csv"

    def handle(self, *args, **options):

        for row in DictReader(
            open('./static/data/comments.csv', encoding='utf-8')
        ):
            comment = Comment(
                id=row['id'],
                review=Review.objects.get(id=row['review_id']),
                text=row['text'],
                author=User.objects.get(id=row['author']),
                pub_date=row['pub_date']
            )
            comment.save()
