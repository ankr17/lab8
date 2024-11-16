from django.db import models

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)  # Унікальний ідентифікатор постачальника
    company_name = models.CharField(max_length=100)  # Назва компанії
    contact_person = models.CharField(max_length=100, blank=True, null=True)  # Контактна особа
    phone = models.CharField(max_length=10)  # Номер телефону (10 цифр)
    account_number = models.CharField(max_length=20, blank=True, null=True)  # Номер рахунку

    class Meta:
        db_table = 'suppliers'

    def __str__(self):
        return self.company_name

class Material(models.Model):
    material_id = models.AutoField(primary_key=True)  # Унікальний ідентифікатор матеріалу
    material_name = models.CharField(max_length=100)  # Назва матеріалу
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Ціна матеріалу

    class Meta:
        db_table = 'materials'

    def __str__(self):
        return self.material_name

class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)  # Унікальний ідентифікатор доставки
    delivery_date = models.DateField()  # Дата доставки
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='deliveries')  # Зв'язок із постачальником
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='deliveries')  # Зв'язок із матеріалом
    delivery_days = models.IntegerField()  # Кількість днів доставки (1-7)
    quantity = models.IntegerField()  # Кількість матеріалів

    class Meta:
        db_table = 'deliveries'

    def __str__(self):
        return f"Delivery {self.delivery_id} on {self.delivery_date}"


