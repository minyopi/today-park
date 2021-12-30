# Generated by Django 4.0 on 2021-12-29 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0002_equipment_parkequipment'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkequipment',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='운동기구 이름'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_type',
            field=models.CharField(max_length=50, verbose_name='운동기구 유형'),
        ),
        migrations.AlterField(
            model_name='park',
            name='dong_address',
            field=models.CharField(max_length=50, verbose_name='동'),
        ),
        migrations.AlterField(
            model_name='park',
            name='full_address',
            field=models.TextField(verbose_name='주소'),
        ),
        migrations.AlterField(
            model_name='park',
            name='gu_address',
            field=models.CharField(max_length=50, verbose_name='구'),
        ),
        migrations.AlterField(
            model_name='park',
            name='gu_id',
            field=models.IntegerField(verbose_name='구ID'),
        ),
        migrations.AlterField(
            model_name='park',
            name='park_image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='공원사진'),
        ),
        migrations.AlterField(
            model_name='park',
            name='park_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='공원이름'),
        ),
        migrations.AlterField(
            model_name='park',
            name='si_address',
            field=models.CharField(max_length=50, verbose_name='시'),
        ),
        migrations.AlterField(
            model_name='parkequipment',
            name='equipment_id',
            field=models.ForeignKey(db_column='equipment_id', on_delete=django.db.models.deletion.CASCADE, related_name='equipment', to='park.equipment'),
        ),
        migrations.AlterField(
            model_name='parkequipment',
            name='park_id',
            field=models.ForeignKey(db_column='park_id', on_delete=django.db.models.deletion.CASCADE, related_name='park', to='park.park'),
        ),
    ]
