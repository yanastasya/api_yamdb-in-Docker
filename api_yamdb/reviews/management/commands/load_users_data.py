from csv import DictReader
from django.core.management import BaseCommand

# Import the model 
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
    
        # Show this if the data already exist in the database
        ##if User.objects.exists():
          #  print('Данные уже загружены.')
           # print(ALREDY_LOADED_ERROR_MESSAGE)
            #return
            
        # Show this before loading the data into the database
        print("Загрузка пользователей.")


        #Code to load the data into database
        for row in DictReader(open('./static/data/users.csv', encoding='utf-8')):
            user=User(
                id=row['id'],
                username=row['username'],
                email=row['email'],
                role=row['role'],
                bio=row['bio'],
                first_name=row['first_name'],
                last_name=row['last_name']
            )  
            user.save()