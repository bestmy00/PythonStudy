# Generated by Django 3.1.7 on 2021-03-30 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='유저ID')),
                ('email', models.EmailField(max_length=100, verbose_name='유저메일')),
                ('password', models.CharField(max_length=100, verbose_name='유저PW')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='가입일자')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='마지막수정일자')),
            ],
            options={
                'verbose_name': '게시판멤버',
                'verbose_name_plural': '게시판멤버',
                'db_table': 'boardmembers',
            },
        ),
    ]
