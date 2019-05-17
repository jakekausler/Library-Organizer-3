# Generated by Django 2.2.1 on 2019-05-17 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libraries', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(default='', max_length=255)),
                ('originally_published', models.DateField(default=None, null=True)),
                ('is_read', models.BooleanField(default=False)),
                ('is_reference', models.BooleanField(default=False)),
                ('is_owned', models.BooleanField(default=False)),
                ('isbn', models.CharField(default='', max_length=13)),
                ('dewey', models.CharField(max_length=10)),
                ('pages', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('depth', models.IntegerField(default=0)),
                ('weight', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('primary_language', models.CharField(default='', max_length=255)),
                ('secondary_language', models.CharField(default='', max_length=255)),
                ('original_language', models.CharField(default='', max_length=255)),
                ('series', models.CharField(default='', max_length=255)),
                ('volume', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('format', models.CharField(default='', max_length=255)),
                ('edition', models.IntegerField(default=1)),
                ('image_url', models.CharField(default='', max_length=255)),
                ('is_reading', models.BooleanField(default=False)),
                ('is_shipping', models.BooleanField(default=False)),
                ('spine_color', models.CharField(default='000000', max_length=6)),
                ('cheapest_new', models.DecimalField(decimal_places=2, default=99999999.99, max_digits=10)),
                ('cheapest_used', models.DecimalField(decimal_places=2, default=99999999.99, max_digits=10)),
                ('edition_published', models.DateField(default=None, null=True)),
                ('lexile', models.IntegerField(default=-1)),
                ('spine_color_overridden', models.BooleanField(default=False)),
                ('notes', models.TextField(default='')),
                ('lexile_code', models.CharField(default='', max_length=2)),
                ('interest_level', models.IntegerField(default=-1)),
                ('ar', models.DecimalField(decimal_places=1, default=-1.0, max_digits=2)),
                ('learning_az', models.IntegerField(default=-1)),
                ('guided_reading', models.IntegerField(default=-1)),
                ('dra', models.IntegerField(default=-1)),
                ('grade', models.IntegerField(default=-1)),
                ('founta_spinnell', models.IntegerField(default=-1)),
                ('age', models.IntegerField(default=-1)),
                ('reading_recovery', models.IntegerField(default=-1)),
                ('pm_readers', models.IntegerField(default=-1)),
                ('library_of_congress', models.CharField(default='', max_length=32)),
                ('fiction_genre', models.CharField(default='', max_length=255)),
                ('is_anthology', models.BooleanField(default=False)),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraries.Library')),
                ('loanee', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=255)),
                ('middle_names', models.CharField(default='', max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WrittenBy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default='Author', max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Person')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher_name', models.CharField(max_length=255)),
                ('city', models.CharField(default='', max_length=255)),
                ('state', models.CharField(default='', max_length=255)),
                ('country', models.CharField(default='', max_length=255)),
                ('parent', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Publisher')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Publisher'),
        ),
    ]
