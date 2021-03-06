# Generated by Django 3.2 on 2021-05-24 01:30

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoverageInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], default=2021)),
                ('model', models.CharField(max_length=30)),
                ('make', models.CharField(max_length=30)),
                ('number', models.CharField(max_length=12)),
                ('price', models.DecimalField(decimal_places=2, default=100000.0, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('30000.00'), message='Values below 30000 are not permitted.')])),
            ],
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_preference', models.BooleanField(default=False)),
                ('quote_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('coverage', models.ManyToManyField(to='quoteapp.CoverageInfo')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quoteapp.customer')),
                ('vehicle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quoteapp.vehicle')),
            ],
        ),
    ]
