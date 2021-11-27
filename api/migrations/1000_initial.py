from django.db import migrations 
from api.user.models import CustomUser 

class Migration(migrations.Migration):
    def seed_data(apps,schema_editor):
        user=CustomUser(name="ashish",
            email="ashishjha050198@gmail.com",
            is_staff=True,
            is_superuser=True,
            phone='7543889258',
            gender='Male'
            )
        user.set_password('ashish007') 
        user.save() 
    dependencies=[

    ]
    operations=[
        migrations.RunPython(seed_data),
    ]
       