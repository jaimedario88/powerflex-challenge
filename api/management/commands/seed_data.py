import json
from datetime import datetime, timezone

from django.core.management.base import BaseCommand, CommandError

from api.models import Factory, FactoryProductionRecord, SprocketType


class Command(BaseCommand):
    help = "Seeds database with initial example data"

    def _seed_sprocket_types(self, sprocket_types):
        sprockets = sprocket_types["sprockets"]
        for num, sprocket in enumerate(sprockets):
            SprocketType.objects.create(name=f"{num}", **sprocket)
        self.stdout.write(self.style.SUCCESS("Successfully seeded sprocket data"))

    def _seed_factory_data(self, factory_data):
        factories = factory_data["factories"]
        for num, factory_data in enumerate(factories):
            factory_data = factory_data["factory"]
            chart_data = factory_data["chart_data"]

            factory = Factory.objects.create(name=f"{num}")

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
        try:
            with open("challenge/seed_sprocket_types.json") as sprocket_types_json:
                self._seed_sprocket_types(json.load(sprocket_types_json))
            with open("challenge/seed_factory_data.json") as factory_data_json:
                self._seed_factory_data(json.load(factory_data_json))
        except OSError as e:
            raise CommandError(e)
        except KeyError as e:
            raise CommandError(f"Invalid file structure: {e}")
