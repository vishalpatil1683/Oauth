# from pprint import pprint
# from configparser import ConfigParser
# from powerbi.client import PowerBiClient
# from powerbi.push_datasets import PushDatasets
# from powerbi.utils import Table,Dataset,Column
# from powerbi.enums import ColumnDataTypes
#
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
# male_column = Column(name='male', data_type=ColumnDataTypes.String)
# female_column = Column(name='female', data_type=ColumnDataTypes.String)
#
# test_table.add_column(column=male_column)
# test_table.add_column(column=female_column)
#
# # pprint(test_table.as_dict())
#
# # # Dataset
#
# test_dataset = Dataset(name='Datachamp-test')
# test_dataset.default_mode = "Push"
#
# # Add Table to dataset
# test_dataset.add_table(table=test_table)
#
# # pprint(
# #     push_dataset_service.post_dataset(
# #         dataset=test_dataset
# #     )
# # )
#
# data_set_id = "2a88550a-fbbb-4e0d-bd99-9d3ea9652c42"
#
# rows_ = [
#     {
#         "male":10,
#         "female":20
#     },
#     {
#         "male":200,
#         "female":300
#     }
# ]
#
# # push_dataset_service.post_dataset_rows(
# #     dataset_id=data_set_id,
# #     table_name='Test-Datachamp',
# #     rows=rows_
# # )
#
# report = power__bi_client.reports()
# report_id=report.get_reports().get("value")[0].get('id')
# # report.export_to_file(report_id=report_id,  file_format=".CSV")
# single_report = report.get_report(report_id)
# # report.export_to_file(report_id=report_id,file_format=)
