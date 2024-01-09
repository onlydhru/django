# Generated by Django 4.2.5 on 2023-11-30 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Freshman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_graduated', models.CharField(max_length=100, null=True)),
                ('year_grad', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('student_number', models.IntegerField()),
                ('lrn', models.IntegerField()),
                ('age', models.IntegerField()),
                ('grade_level', models.CharField(max_length=50, null=True)),
                ('Course_and_Strand', models.CharField(choices=[('HM', 'HOSPITALITY MANAGEMENT'), ('CS', 'COMPUTER SCIENCE'), ('IT', 'ICT'), ('AB', 'ABM')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.CharField(max_length=50, null=True)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('student_num', models.IntegerField()),
                ('tuition', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transferee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_level', models.IntegerField()),
                ('previous_school', models.CharField(max_length=100, null=True)),
                ('student_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='as.student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='as.teacher'),
        ),
    ]