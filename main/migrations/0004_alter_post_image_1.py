# Generated by Django 4.1.2 on 2022-11-05 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_comment_user_alter_post_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_1',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
