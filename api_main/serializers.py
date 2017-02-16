from rest_framework import serializers

class magic_box_all_serializer(serializers.Serializer):
	product_name = serializers.CharField()
	product_cost = serializers.CharField()
	product_url = serializers.URLField()