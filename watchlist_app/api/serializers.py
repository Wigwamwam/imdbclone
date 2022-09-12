# from wsgiref.validate import validator
from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform


# model serializer

class WatchListSerializer(serializers.ModelSerializer):
    # custom serializer
    # len_names = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = "__all__"

        # for specific fields
        # fields = ['id', 'name', 'description']

        # you can use exclude when you have a lot of fields
        # exclude = ['active']

    # customm serialiser
    # def get_len_name(self, object):
    #     return len(object.name)

    # field level serializer

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value

    # # object level validation

    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Name and Description should not be different!")
    #     else:
    #         return data

# using validators function on the name

# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # update and return an exisitng 'snippet' instance, given the validated data
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save
#         return instance

#     # field level validation

#     # def validate_name(self, value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name is too short!")
#     #     else:
#     #         return value

#     # object level validation

    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Name and Description should not be different!")
    #     else:
    #         return data

class StreamPlatformSerializer(serializers.ModelSerializer):
    # custom serializer
    # len_names = serializers.SerializerMethodField()

    class Meta:
        model = StreamPlatform
        fields = "__all__"
