from rest_framework import serializers

from .models import Task

#serializers for update task
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


# serializer for task status
class TaskStatusSerializer(serializers.ModelSerializer):
   class Meta:
        model = Task
        fields = ('task_status',)

   def update(self, instance, validated_data): 
        instance.task_status = validated_data.get('task_status', instance.task_status)
        instance.save()
        return instance