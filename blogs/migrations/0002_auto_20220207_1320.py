# Generated by Django 3.1.7 on 2022-02-07 19:20

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_at'], 'verbose_name': 'Artículo', 'verbose_name_plural': 'Artículos'},
        ),
        migrations.AddField(
            model_name='article',
            name='description',
            field=ckeditor.fields.RichTextField(default=ckeditor.fields.RichTextField(verbose_name='Contenido'), verbose_name='Decripción breve del articulo'),
        ),
        migrations.AlterField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='articles', to='blogs.Category', verbose_name='Categorias'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='null', upload_to='articles', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
