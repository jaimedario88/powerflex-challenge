from rest_framework import serializers

from api.models import Factory, Sprocket


class FactoryDataSerializer(serializers.Serializer):
    sprocket_production_actual = serializers.SerializerMethodField()
    sprocket_production_goal = serializers.SerializerMethodField()
    time = serializers.SerializerMethodField()

    def get_sprocket_production_actual(self, obj):
        return obj.factoryproductionrecord_set.values_list(
            "sprocket_production_actual", flat=True
        )

    def get_sprocket_production_goal(self, obj):
        return obj.factoryproductionrecord_set.values_list(
            "sprocket_production_goal", flat=True
        )

    def get_time(self, obj):
        return obj.factoryproductionrecord_set.values_list("timestamp", flat=True)


class FactorySerializer(serializers.ModelSerializer):
    chart_data = FactoryDataSerializer(source="*")

    class Meta:
        model = Factory
        fields = "__all__"


class SprocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprocket
        fields = "__all__"
