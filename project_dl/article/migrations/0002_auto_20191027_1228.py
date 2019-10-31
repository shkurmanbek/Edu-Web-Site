# Generated by Django 2.2.6 on 2019-10-27 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Commands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('comments_article', models.ForeignKey(on_delete='on_delete', to='article.Article')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
    ]
