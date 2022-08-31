from rest_framework import serializers
from plane_removal.models import PCFile, ConfigFile


class PCFileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    file = serializers.FileField()

    def create(self, validated_data):
        """
        Create and return a new `PCFile` instance, given the validated data.
        """
        return PCFile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `PCFile` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.code = validated_data.get('code', instance.code)
        instance.file = validated_data.get('file', instance.file)
        instance.save()
        return instance


class ConfigFileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    file = serializers.FileField()

    def create(self, validated_data):
        """
        Create and return a new `PCFile` instance, given the validated data.
        """
        return ConfigFile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `PCFile` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.code = validated_data.get('code', instance.code)
        instance.file = validated_data.get('file', instance.file)
        instance.save()
        return instance