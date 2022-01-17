# Generated by Django 3.2.7 on 2021-12-29 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_gradeattendance_created_by'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['first_name', 'grade'], 'verbose_name_plural': 'Students'},
        ),
        migrations.CreateModel(
            name='MessageTeacherToGrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('message_subject', models.CharField(max_length=50, null=True, verbose_name='Message Subject')),
                ('message_text', models.TextField(null=True, verbose_name='')),
                ('grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.grade', verbose_name='Grade')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.teacher', verbose_name='Teacher')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
