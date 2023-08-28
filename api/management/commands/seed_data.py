import json
from datetime import datetime, timezone

from django.core.management.base import BaseCommand, CommandError

from api.models import Factory, FactoryProductionRecord, SprocketType


class Command(BaseCommand):
    help = "Seeds database with initial example data"

    def _number_to_letter(self, number: int) -> str:
        """
        Small aux function to return a letter for a given number using the alphabet order,
        just to give the created objects a more easy to use name (A, B, C) instead of a number

        Args:
            number (int): The number to map to a character

        Returns:
            str: A single character for this number
        """
        if 0 <= number <= 25:
            return chr(ord("A") + number)
        else:
            # Calculate the corresponding letter after looping back
            return chr(ord("A") + (number + 1) % 26)

    def _seed_sprocket_types(self, sprocket_types):
        sprockets = sprocket_types["sprockets"]
        for num, sprocket in enumerate(sprockets):
            SprocketType.objects.create(name=self._number_to_letter(num), **sprocket)
        self.stdout.write(self.style.SUCCESS("Successfully seeded sprocket data"))

    def _seed_factory_data(self, factory_data):
        factories = factory_data["factories"]
        for num, factory_data in enumerate(factories):
            factory_data = factory_data["factory"]
            chart_data = factory_data["chart_data"]

            factory = Factory.objects.create(name=self._number_to_letter(num))

            sprocket_production_actual = chart_data["sprocket_production_actual"]
            sprocket_production_goal = chart_data["sprocket_production_goal"]
            timestamp = chart_data["time"]

            records = zip(
                sprocket_production_actual, sprocket_production_goal, timestamp
            )

            for record in records:
                FactoryProductionRecord.objects.create(
                    factory=factory,
                    sprocket_production_actual=record[0],
                    sprocket_production_goal=record[1],
                    timestamp=datetime.fromtimestamp(record[2]).replace(
                        tzinfo=timezone.utc
                    ),
                )
        self.stdout.write(self.style.SUCCESS("Successfully seeded factory data"))

    def handle(self, *args, **options):
        """
        Opens the provided files to seed the database with initial data
        """
        if (
            FactoryProductionRecord.objects.exists() is True
            and SprocketType.objects.exists() is True
        ):
            self.stdout.write(self.style.SUCCESS("Data already exists, skipping..."))

        try:
            with open("challenge/seed_sprocket_types.json") as sprocket_types_json:
                self._seed_sprocket_types(json.load(sprocket_types_json))
            with open("challenge/seed_factory_data.json") as factory_data_json:
                self._seed_factory_data(json.load(factory_data_json))
        except OSError as e:
            raise CommandError(e)
        except KeyError as e:
            raise CommandError(f"Invalid file structure: {e}")
