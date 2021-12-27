from django.shortcuts import render
from . models import TechnologyKPI,Technology
# Create your views here.
from pprint import pprint
from configparser import ConfigParser
# from powerbi.client import PowerBiClient
from powerbi.push_datasets import PushDatasets
from powerbi.utils import Table,Dataset,Column
from powerbi.enums import ColumnDataTypes
import pandas as pd


def bi_process(request):
    # techKpi = [field.name for field in TechnologyKPI._meta.get_fields()]
    # # print(techKpi)
    # context = {
    #     "Fields": techKpi,
    #     "Name": "Technology"
    # }
    return render(request, 'Technology/uploadfile.html')


def map_process(request):
    techKpi = [field.name for field in TechnologyKPI._meta.get_fields()]
    # print(techKpi)
    file_fields = ["name","type","storage_type","storage_cost","cost"]
    context = {
        "Template_Fields": techKpi,
        "File_Fields":file_fields,
        "Name": "Technology"
    }
    return render(request, 'Technology/map.html',context=context)

# config = ConfigParser()
# config.read('config/config.ini')
#
# client_id = config.get('power-bi-config','client_id')
# client_secret = config.get('power-bi-config','client_secret')
# redirect_uri = config.get('power-bi-config','redirect_uri')
#
#
# power__bi_client = PowerBiClient(client_id=client_id,
#                                 client_secret=client_secret,
#                                 scope=['https://analysis.windows.net/powerbi/api/.default'],
#                                 redirect_uri=redirect_uri,
#                                 credentials='config/power_bi_state.jsonc')
#
# # VIA API WE WILL PASS TechnologyKPI FIELDS (TEMPLATE_FIELD) WHICH WILL BE DIFF FOR DIFF KPI
#
# # JSON REQUEST FOR BACKEND TO MAP
# # AFTER THAT WE CAN PANDAS AND CREATE DATAFRAME.
# key_value_pairs = {
#     "name": "product_name",
#     "type": "product_type",
#     "storage_type": "storage_type_name",
#     "storage_cost": "storage_type_cost",
#     "cost": "other_cost"
# }
#
# # FOR E.G IF USER UPLOAD TestData.xlsx File
# columns = ["product_name", "product_type", "storage_type_name", "storage_type_cost", "other_cost"]
# df = pd.read_excel('TestData.xlsx')
# df.columns = columns
#
# dashboard = power__bi_client.dashboards()
#
# # pprint(dashboard.get_dashboards())
#
# # # push Dataset
#
# push_dataset_service = power__bi_client.push_datasets()
#
# # Create Table
#
# test_table = Table(name='Test-Datachamp')
#
# for c in columns:
#     c = Column(name=c, data_type=ColumnDataTypes.String)
#     test_table.add_column(column=c)
# # female_column = Column(name='female', data_type=ColumnDataTypes.String)
#
# # test_table.add_column(column=male_column)
# # test_table.add_column(column=female_column)
#
# # pprint(test_table.as_dict())
#
# # # Dataset
#
# test_dataset = Dataset(name='Datachamp-test-1')
# test_dataset.default_mode = "Push"
#
# # pprint(test_dataset)
# # Add Table to dataset
# test_dataset.add_table(table=test_table)
#
# # pprint(
# #     push_dataset_service.post_dataset(
# #         dataset=test_dataset
# #     )
# # )
#
# data_set_id = "b69dd362-b282-460c-a5a3-41ac14a0d13a"
#
# rows_ = []
# data = df.to_json(orient = 'records', lines = True).splitlines()
# for d in data:
#     rows_.append(json.loads(d))
#
# push_dataset_service.post_dataset_rows(
#     dataset_id=data_set_id,
#     table_name='Test-Datachamp',
#     rows=rows_
# )

# report = power__bi_client.reports()
# for i in range(len(report.get_reports())):
#     report_id=report.get_reports().get("value")[i].get('id')
#     single_report = report.export_report(report_id)
#     with open(file=f"reports/{report_id}.pbix",mode='wb+') as report_created:
#         report_created.write(single_report)
#
# report.export_to_file(report_id=report_id,  file_format=".CSV")
# single_report = report.get_report(report_id)
# report.export_to_file(report_id=report_id,file_format=)
