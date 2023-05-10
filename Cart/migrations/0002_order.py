# Generated by Django 4.0.2 on 2023-05-10 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('order_status', models.CharField(choices=[('Order Received', 'Order Received'), ('Order Processing', 'Order Processing'), ('On the way', 'On the way'), ('Order Completed', 'Order Completed'), ('Order Cancelled', 'Order Cancelled')], default='Order Received', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(blank=True, max_length=250)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('items', models.ManyToManyField(to='Cart.CartItem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]