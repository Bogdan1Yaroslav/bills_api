from datetime import datetime
from .models import Service


# значение sum является числом
def is_sum_valid(bill_sum: str) -> bool:
    return True if bill_sum.isdigit() and int(bill_sum) > 0 else False


# в service не пусто ( пусто так же считается, если вместо текста знак “-”)
def is_service_provided(services: str) -> bool:
    if services == '-' or services == '':
        return False
    return True


# Очистка данных об услугах
def clean_services_data(services: str) -> list:
    cleaned_data = [service.strip() for service in services.split(';')]
    return cleaned_data


# Конвертация данных о дате в соответствующий формат
def convert_str_to_date(date: str):
    return datetime.strptime(date, '%d.%m.%Y').date()


# корректная дата (дата считается корректной, если есть день, месяц и год).
def is_date_valid(date):
    try:
        datetime_object = convert_str_to_date(date)
        return datetime_object
    except ValueError:
        return False


# №(номер счет) тип  int
def check_bill_number(number: str) -> bool:
    return True if number.isdigit() else False


# указаны client_name и client_org
def if_client_and_org_provided(client: str, org: str) -> bool:
    if client and org:
        return True
    return False


# Преобразовать список из str в объекты queryset
def create_or_get_services(raw_data: list) -> list:
    result = [Service.objects.get_or_create(name=service)[0] for service in raw_data]

    return result
