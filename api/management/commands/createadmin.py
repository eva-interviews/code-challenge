"""
Command to create an admin user
"""
import logging

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Creates an admin user non-interactively if it does not exist
    """

    help = "Creates an admin user non-interactively if it does not exist"

    def add_arguments(self, parser):
        """
        Handle the arguments received from the command line

        @param parser: parser
        @return:
        """
        parser.add_argument(
            "--password",
            type=str,
            required=True,
            help="Admin password",
        )
        parser.add_argument(
            "--email",
            type=str,
            required=True,
            help="Admin email",
        )

    def handle(self, *args, **options):
        """
        Handles the params received from the command line

        @param args:
        @param options: Contains the params received in command line
        @return: stdout
        """
        user_model = get_user_model()
        user_model.objects.create_superuser(
            email=options["email"],
            password=options["password"],
        )
        logger.info("Superuser created successfully.")
