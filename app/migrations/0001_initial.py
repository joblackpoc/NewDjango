# Generated by Django 3.0.8 on 2020-07-10 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'หมวดหมู่สินค้า',
                'verbose_name_plural': 'หมวดหมู่สินค้า',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Reponse_kpi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=155)),
            ],
            options={
                'verbose_name': 'กลุ่มงาน',
                'verbose_name_plural': 'กลุ่มงาน',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Ssj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=155)),
                ('hospcode', models.CharField(default='00068', max_length=5)),
            ],
            options={
                'verbose_name': 'จังหวัด',
                'verbose_name_plural': 'จังหวัด',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('admin', 'ผู้ดูแลระดับจังหวัด'), ('input', 'ผู้รับผิดชอบตัวชี้วัด'), ('leader', 'หัวหน้าฝ่าย')], default='input', max_length=100)),
                ('user_phone', models.CharField(blank=True, max_length=100, null=True)),
                ('response_kpi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Reponse_kpi')),
                ('ssj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Ssj')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ข้อมูลผู้ใช้',
                'verbose_name_plural': 'ข้อมูลผู้ใช้',
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, upload_to='product')),
                ('stock', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
            ],
            options={
                'verbose_name': 'สินค้า',
                'verbose_name_plural': 'สินค้า',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Kpi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kpi_code', models.CharField(max_length=15, unique=True)),
                ('kpi_name', models.TextField(blank=True)),
                ('kpi_group', models.CharField(blank=True, max_length=15)),
                ('goal', models.CharField(blank=True, max_length=11)),
                ('goal_descript', models.TextField(blank=True)),
                ('cri_type', models.CharField(blank=True, max_length=15)),
                ('unit', models.CharField(blank=True, max_length=55)),
                ('formular', models.CharField(blank=True, max_length=55)),
                ('formular_type', models.CharField(blank=True, max_length=15)),
                ('descript_a', models.TextField(blank=True)),
                ('descript_b', models.TextField(blank=True)),
                ('response_kpi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Reponse_kpi')),
            ],
            options={
                'verbose_name': 'ตัวชี้วัด KPI',
                'verbose_name_plural': 'ตัวชี้วัด KPI',
                'ordering': ('kpi_code',),
            },
        ),
        migrations.CreateModel(
            name='KeyInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(choices=[('2020', '2563')], default='2019', max_length=6)),
                ('a1', models.CharField(blank=True, max_length=55)),
                ('b1', models.CharField(blank=True, max_length=55)),
                ('a2', models.CharField(blank=True, max_length=55)),
                ('b2', models.CharField(blank=True, max_length=55)),
                ('a3', models.CharField(blank=True, max_length=55)),
                ('b3', models.CharField(blank=True, max_length=55)),
                ('a4', models.CharField(blank=True, max_length=55)),
                ('b4', models.CharField(blank=True, max_length=55)),
                ('a5', models.CharField(blank=True, max_length=55)),
                ('b5', models.CharField(blank=True, max_length=55)),
                ('a6', models.CharField(blank=True, max_length=55)),
                ('b6', models.CharField(blank=True, max_length=55)),
                ('a7', models.CharField(blank=True, max_length=55)),
                ('b7', models.CharField(blank=True, max_length=55)),
                ('a8', models.CharField(blank=True, max_length=55)),
                ('b8', models.CharField(blank=True, max_length=55)),
                ('a9', models.CharField(blank=True, max_length=55)),
                ('b9', models.CharField(blank=True, max_length=55)),
                ('a10', models.CharField(blank=True, max_length=55)),
                ('b10', models.CharField(blank=True, max_length=55)),
                ('a11', models.CharField(blank=True, max_length=55)),
                ('b11', models.CharField(blank=True, max_length=55)),
                ('a12', models.CharField(blank=True, max_length=55)),
                ('b12', models.CharField(blank=True, max_length=55)),
                ('input_update', models.DateTimeField(default=django.utils.timezone.now)),
                ('hospcode', models.ForeignKey(default='00068', on_delete=django.db.models.deletion.CASCADE, to='app.Ssj')),
                ('kpi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Kpi')),
                ('response', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='app.Reponse_kpi')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'บันทึก KPI',
                'verbose_name_plural': 'บันทึก KPI',
                'ordering': ('kpi',),
            },
        ),
    ]
