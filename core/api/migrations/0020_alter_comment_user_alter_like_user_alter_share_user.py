# Generated by Django 5.1.5 on 2025-02-12 09:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_comment_user_alter_like_user_alter_share_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to='api.author'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='like_author', to='api.author'),
        ),
        migrations.AlterField(
            model_name='share',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='share_author', to='api.author'),
        ),
    ]
