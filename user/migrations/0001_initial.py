# Generated by Django 4.2 on 2025-04-22 15:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import user.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('address', models.TextField()),
                ('job_title', models.CharField(max_length=250)),
                ('joined_date', models.DateField(null=True)),
                ('salary', models.PositiveBigIntegerField(default=0)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=250)),
                ('date_of_birth', models.DateField(null=True)),
                ('employment_type', models.CharField(choices=[('full_time', 'full_time'), ('part_time', 'part_time'), ('contract', 'contract')], max_length=250)),
                ('contact', models.CharField(max_length=50)),
                ('note', models.TextField()),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='user/profile_image')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='user.department')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', user.models.CustomUserManager()),
            ],
        ),
    ]
