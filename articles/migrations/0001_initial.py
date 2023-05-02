# Generated by Django 3.2.18 on 2023-05-02 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('art_title', models.CharField(max_length=255)),
                ('art_content', models.TextField(blank=True)),
                ('primary_language', models.CharField(choices=[('javascript', 'JavaScript'), ('python', 'Python'), ('java', 'Java'), ('c++', 'C++'), ('c#', 'C#'), ('typescript', 'TypeScript'), ('ruby', 'Ruby'), ('swift', 'Swift'), ('go', 'Go'), ('kotlin', 'Kotlin'), ('rust', 'Rust'), ('php', 'PHP'), ('perl', 'Perl'), ('html', 'HTML'), ('css', 'CSS')], max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]