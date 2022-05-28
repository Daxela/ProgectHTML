# Generated by Django 3.2.9 on 2022-05-14 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('page_id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('page_url', models.TextField(db_column='url')),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
                'db_table': 'page',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('site_id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('site_host', models.TextField(db_column='host')),
                ('site_name', models.TextField(db_column='name')),
            ],
            options={
                'verbose_name': 'Site',
                'verbose_name_plural': 'Sites',
                'db_table': 'site',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('request_id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('request_html_content', models.TextField(db_column='htmlcontent')),
                ('request_page_id', models.ForeignKey(db_column='page_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.page')),
            ],
            options={
                'verbose_name': 'Request',
                'verbose_name_plural': 'Requests',
                'db_table': 'request',
            },
        ),
        migrations.AddField(
            model_name='page',
            name='page_site_id',
            field=models.ForeignKey(db_column='site_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.site'),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('content_id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('content_content', models.TextField(db_column='content')),
                ('content_request_id', models.ForeignKey(db_column='request_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.request')),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Contents',
                'db_table': 'pagecontent',
            },
        ),
    ]
