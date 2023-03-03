from rest_framework import serializers

from snack.models import Snack


class SnackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snack
        fields = ['id', 'name', 'image', 'url', 'description', 'is_accepted',
                  'supply_year', 'supply_month', 'create_dt']
