from django.db import models


class Organization(models.Model):
    """Модель: Организация"""

    name = models.CharField(max_length=36, verbose_name="Название организации")

    class Meta:
        verbose_name_plural = 'organizations'
        verbose_name = 'organization'

    def __str__(self):
        return self.name


class Client(models.Model):
    """Модель: Клиент"""

    name = models.CharField(unique=True, max_length=36, verbose_name="Имя клиента")
    organizations = models.ManyToManyField(Organization, related_name='clients', verbose_name="Организации")

    class Meta:
        verbose_name_plural = 'clients'
        verbose_name = 'client'

    def __str__(self):
        return self.name


class Bill(models.Model):
    """Модель: Счет"""

    client_name = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    client_org = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name="Организация")
    created_at = models.DateField(auto_now_add=True)
    bill_sum = models.PositiveIntegerField(verbose_name="Сумма счета")
    date = models.DateField(verbose_name="Счет от")
    bill_number = models.CharField(max_length=10, null=True, verbose_name="Номер счета")
    services = models.ManyToManyField('Service', related_name='bills', verbose_name="Услуга(и)")

    class Meta:
        verbose_name_plural = 'bills'
        verbose_name = 'bill'

        unique_together = ('client_name', 'client_org', 'bill_number',)

    def __str__(self):
        return f"Счет №{self.bill_number}"


class Service(models.Model):
    """Модель: Услуга"""

    name = models.CharField(unique=True, max_length=36, verbose_name="Наименование услуги")
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'services'
        verbose_name = 'service'

    def __str__(self):
        return self.name
