# Generated by Django 2.2.1 on 2019-05-27 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interventi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intervento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=250)),
                ('annotazioni', models.TextField(blank=True)),
                ('segnalatore', models.CharField(blank=True, max_length=250)),
                ('data_inserimento', models.DateTimeField(auto_now_add=True)),
                ('data_ultima_modifica', models.DateTimeField(auto_now=True)),
                ('punto_vendita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interventi', to='interventi.PuntoVendita')),
            ],
            options={
                'verbose_name_plural': 'Interventi',
            },
        ),
    ]
