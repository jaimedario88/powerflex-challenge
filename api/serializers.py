from typing import Any
from rest_framework import serializers

from api.models import Factory, Sprocket, SprocketType


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


class SprocketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SprocketType
        fields = "__all__"


class SprocketSerializer(serializers.ModelSerializer):
    sprocket_type = serializers.PrimaryKeyRelatedField(
        queryset=SprocketType.objects.all()
    )

    def to_representation(self, instance: Any) -> Any:
        ret = super().to_representation(instance)
        ret["sprocket_type"] = SprocketTypeSerializer(
            instance=instance.sprocket_type, context=self.context
        ).data
        return ret

    class Meta:
        model = Sprocket
        fields = "__all__"
