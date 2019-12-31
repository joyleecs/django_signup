# Generated by Django 3.0.1 on 2019-12-19 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fcuser', '0005_auto_20191219_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='title')),
                ('contents', models.TextField(verbose_name='contents')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='registered_time')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fcuser.Fcuser', verbose_name='writer')),
            ],
            options={
                'verbose_name': '패스트캠퍼스 게시글',
                'verbose_name_plural': '패스트캠퍼스 게시글',
                'db_table': 'fccommunity_board',
            },
        ),
    ]
