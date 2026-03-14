import datetime
from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.mail import send_mass_mail
from django.contrib.auth.models import User
from django.db.models import Count


class Command(BaseCommand):
    help = 'Wysyła wiadomość e-mail do użytkowników zarejestrowanych co najmniej od N dni z przypomnieniem ' \
            'o konieczności zapisania się na dowolny kurs.'

    def add_arguments(self, parser):
        parser.add_argument('--days', dest='days', type=int)

    def handle(self, *args, **options):
        emails = []
        subject = 'Zapisz się na kurs'
        date_joined = datetime.date.today() - datetime.timedelta(days=options['days'])
        users = User.objects.annotate(course_count=Count('courses_joined')).filter(
            course_count=0, date_joined__date__lte=date_joined)
        for user in users:
            message = f'Witaj, {user.first_name}!\n\nZauważyliśmy, że jeszcze nie zapisałeś się na żaden kurs.' \
                       f'Na co jeszcze czekasz?'
            emails.append((subject, message, settings.DEFAULT_FROM_EMAIL, [user.email]))
        send_mass_mail(emails)
        self.stdout.write(f'Wysłano {len(emails)} przypomnień.')
