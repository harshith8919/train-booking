from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('fare', models.FloatField()),
                ('total_seats', models.IntegerField()),
                ('available_seats', models.IntegerField()),
            ],
        ),
    ]
