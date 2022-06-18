# Generated by Django 2.2.19 on 2022-06-18 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('priority', models.CharField(choices=[('LW', 'Низкий'), ('MD', 'Средний'), ('HG', 'Высокий')], default='LW', max_length=2)),
                ('done', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.Category')),
            ],
        ),
    ]