from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Clear existing data (optional)
        Listing.objects.all().delete()

        for _ in range(10):
            Listing.objects.create(
                title=fake.sentence(nb_words=3),
                description=fake.paragraph(nb_sentences=3),
                location=fake.city(),
                price_per_night=random.uniform(50, 500)
            )

        self.stdout.write(self.style.SUCCESS('✅ Seeded the database with sample listings'))
