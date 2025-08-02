from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth import get_user_model
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **kwargs):
        # تأكد من وجود مستخدم لاستخدامه كـ owner
        if not User.objects.exists():
            self.stdout.write(self.style.ERROR("No users found. Please create a user first."))
            return
        
        user = User.objects.first()

        titles = [
            "Cozy Apartment in Downtown",
            "Luxury Villa with Pool",
            "Budget Room Near Airport",
            "Modern Loft in City Center",
            "Rustic Cabin in the Woods"
        ]

        for i in range(10):
            listing = Listing.objects.create(
                title=random.choice(titles),
                description="This is a sample listing description number {}".format(i + 1),
                price_per_night=random.randint(30, 300),
                owner=user
            )
            self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))
