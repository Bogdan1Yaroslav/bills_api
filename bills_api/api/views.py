from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from django.db import IntegrityError
from .models import Client, Organization, Bill
from .serializers import BillSerializer
from .filters import BillFilter
import csv
from .utils import is_sum_valid, is_service_provided, is_date_valid, check_bill_number, if_client_and_org_provided, \
    clean_services_data, convert_str_to_date, create_or_get_services

file_storage = FileSystemStorage(location='tmp/')


class BillViewSet(ModelViewSet):
    serializer_class = BillSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_class = BillFilter

    def get_queryset(self):
        queryset = Bill.objects.all()
        return queryset

    def get_bills_list(self, request):
        return self.list(request)

    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        file = request.FILES['file']

        content = file.read()

        file_content = ContentFile(content)

        file_name = file_storage.save('_tmp.csv', file_content)

        tmp_file = file_storage.path(file_name)

        csv_file = open(tmp_file, errors='ignore', encoding='utf-8')
        reader = csv.reader(csv_file)
        next(reader)

        for index, row in enumerate(reader, start=1):

            bill_client_name = row[0]
            bill_client_org = row[1]
            bill_num = row[2]
            bill_sum = row[3]
            bill_date = row[4]
            bill_services = row[5]

            if is_sum_valid(bill_sum) and is_service_provided(bill_services) and is_date_valid(
                    bill_date) and check_bill_number(bill_num) and if_client_and_org_provided(bill_client_name,
                                                                                              bill_client_org):
                bill_services = clean_services_data(bill_services)
                bill_date = convert_str_to_date(bill_date)

                organization, created = Organization.objects.get_or_create(name=bill_client_org)

                client, created = Client.objects.get_or_create(name=bill_client_name)

                client.organizations.add(organization.id)
                client.save()

                try:
                    bill_obj = Bill.objects.create(client_name=client,
                                                   client_org=organization,
                                                   bill_sum=bill_sum,
                                                   date=bill_date,
                                                   bill_number=bill_num,
                                                   )

                    bill_obj.services.add(*create_or_get_services(bill_services))

                except IntegrityError as e:
                    print(f'\n{e}\nError occurs in row {index}')

        return Response({'status': Response.status_code, 'message': 'Success!'})
