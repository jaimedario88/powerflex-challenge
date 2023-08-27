from rest_framework import serializers

from api.models import Factory, Sprocket


class FactoryDataSerializer(serializers.Serializer):
    sprocket_production_actual = serializers.ReadOnlyField()
    sprocket_production_goal = serializers.ReadOnlyField()
    time = serializers.ReadOnlyField()

    def get_sprocket_production_actual(self):
        self.factoryproductionrecord_set.values_list(
            "sprocket_production_actual", flat=True
        )

    def get_sprocket_production_goal(self):
        self.factoryproductionrecord_set.values_list(
            "sprocket_production_goal", flat=True
        )

    def get_time(self):
        self.factoryproductionrecord_set.values_list("timestamp", flat=True)


class FactorySerializer(serializers.ModelSerializer):
    chart_data = FactoryDataSerializer()

    class Meta:
        model = Factory
        fields = "__all__"


class SprocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprocket
        fields = "__all__"
