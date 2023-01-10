from rest_framework import serializers
from .models import Dispenser, Usage

class UsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usage
        fields = ["opened_at", "closed_at", "flow_volume", "total_spent"]

class DispenserSerializer(serializers.ModelSerializer):
    usages = UsageSerializer(many=True, read_only=True)
    amount = serializers.FloatField(read_only=True)
    
    class Meta:
        model = Dispenser
        fields = ["amount", "usages"]

class DispenserSerializerCreation(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True, source="unique_id")
    class Meta:
        model = Dispenser
        fields = ["id", "flow_volume"]
        read_only = ["id"]

class DispenserStatusSerializer(serializers.Serializer):
    STATUS_CHOICES = ['open', 'close']
    status = serializers.ChoiceField(choices=STATUS_CHOICES)
    updated_at = serializers.DateTimeField()

    def update(self, instance, validated_data):
        new_status = validated_data.get('status', instance.status)
        updated_at = validated_data.get('updated_at')

        
        if new_status == 'open':
            Usage.objects.create(opened_at=updated_at, flow_volume=instance.flow_volume, 
                                total_spent=0, dispenser=instance)
        elif new_status == 'close':
            last_usage = instance.usages.last()
            last_usage.closed_at = updated_at
            time_gap = last_usage.closed_at - last_usage.opened_at
            time_gap = time_gap.total_seconds()
            last_usage.total_spent = time_gap * last_usage.flow_volume * Dispenser.BEER_PRICE_PER_LITRE
            last_usage.save()

        return instance

    def validate_status(self, status):
        last_usage = self.instance.usages.last()

        if last_usage is not None and self.instance.status == status:
            raise serializers.ValidationError('Dispenser is already opened/closed')
        if last_usage is None and status == 'close':
            raise serializers.ValidationError('Dispenser is already opened/closed')
        return status

    def validate_updated_at(self, updated_at):
        last_usage = self.instance.usages.last()

        if last_usage is not None and self.instance.status == 'open' and updated_at <= last_usage.opened_at:
            raise serializers.ValidationError('Closed time must be after opened time')
        return updated_at