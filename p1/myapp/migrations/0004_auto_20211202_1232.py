# Generated by Django 3.2.9 on 2021-12-02 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20211202_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='request_page_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.page'),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('content_id', models.AutoField(primary_key=True, serialize=False)),
                ('content_content', models.CharField(max_length=255)),
                ('content_request_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.request')),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Contents',
            },
        ),
    ]
