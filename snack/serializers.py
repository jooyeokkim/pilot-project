from rest_framework import serializers

from snack.models import Snack, SnackRequest, SnackEmotion


class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snack
        fields = ['id', 'name', 'image', 'url']


class SnackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snack
        fields = ['name', 'image', 'url']


class SnackRequestSerializer(serializers.ModelSerializer):
    snack = SnackSerializer(read_only=True)

    class Meta:
        model = SnackRequest
        fields = ['id', 'likes', 'dislikes', 'user', 'snack', 'description', 'is_accepted', 'supply_year',
                  'supply_month', 'create_dt']


class SnackRequestManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnackRequest
        fields = ['description', 'is_accepted', 'supply_year', 'supply_month']

    def validate(self, attrs):
        instance = self.instance
        try:
            if attrs['is_accepted'] and instance.likes < instance.dislikes:
                raise serializers.ValidationError(
                    {'detail': '싫어요 수가 더 많은 신청은 승인할 수 없습니다.'}
                )
        except KeyError:
            pass
        return attrs


class SnackRequestEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnackRequest
        fields = ['snack', 'description']

    def validate(self, attrs):
        snack = attrs['snack']
        if SnackRequest.objects.filter(is_accepted=False, snack=snack):
            raise serializers.ValidationError(
                {'snack': '이미 주문 대기중인 간식입니다.'}
            )
        return attrs


class SnackRequestNewEnrollSerializer(serializers.ModelSerializer):
    snack = SnackCreateSerializer()

    class Meta:
        model = SnackRequest
        fields = ['snack', 'description']

    def create(self, validated_data):
        snack = validated_data.pop('snack')
        snack = Snack.objects.create(**snack)
        snackRequest = SnackRequest.objects.create(snack=snack, **validated_data)
        return snackRequest


class SnackEmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnackEmotion
        fields = ['snack_request', 'name']

    def create(self, validated_data):
        request = self.context.get('request', None)
        validated_name = validated_data['name']
        emotion, is_created = SnackEmotion.objects.get_or_create(snack_request=validated_data['snack_request'], user=request.user, defaults={'name': validated_name}) # defaults는 생성시에만 동작
        if not is_created:
            if emotion.name == validated_name:
                emotion.delete()
            else:
                emotion.name = validated_name
                emotion.save()
        return emotion