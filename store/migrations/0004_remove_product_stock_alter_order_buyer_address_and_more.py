# Generated by Django 5.1.3 on 2024-11-25 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_order_buyer_address_order_buyer_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.AlterField(
            model_name='order',
            name='buyer_address',
            field=models.CharField(blank=True, default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='buyer_email',
            field=models.EmailField(blank=True, default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='buyer_name',
            field=models.CharField(blank=True, default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='buyer_phone',
            field=models.CharField(blank=True, default='', max_length=60),
            preserve_default=False,
        ),
    ]
