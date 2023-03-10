<<<<<<< HEAD
# Generated by Django 4.1.7 on 2023-02-20 06:49
=======
# Generated by Django 4.1.7 on 2023-02-20 06:52
>>>>>>> f0cf70c187a02ef13c7821c4c612dbff267fc274

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("create_date", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Answer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("create_date", models.DateTimeField()),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pybo.question"
                    ),
                ),
            ],
        ),
    ]
