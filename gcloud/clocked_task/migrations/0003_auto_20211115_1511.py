# Generated by Django 2.2.24 on 2021-11-15 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clocked_task", "0002_auto_20210924_1626"),
    ]

    operations = [
        migrations.AddField(
            model_name="clockedtask",
            name="notify_receivers",
            field=models.TextField(default="{}", help_text="计划任务事件通知人"),
        ),
        migrations.AddField(
            model_name="clockedtask",
            name="notify_type",
            field=models.CharField(default="[]", help_text="计划任务事件通知方式", max_length=128),
        ),
    ]