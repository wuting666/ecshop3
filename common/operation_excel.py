# import pandas
# class OperationExcel():
#     def __init__(self,file_path):
#         #打开表格
#         self.table=pandas.read_excel(file_path)
#     def get_data_info(self):
#         #获取表格内的详细信息
#         data=[]
#         for i in self.table.index.values:
#             data_dict=self.table.loc[i].to_dict()
#             data.append(data_dict)
#         return data
# if __name__ == '__main__':
#     operation=OperationExcel("../data/text_data.xls")
#     print(operation.get_data_info())
#
import pandas
class OperationExcel:
    def __init__(self,file_path):
    #打开表格
        self.table=pandas.read_excel(file_path)
    def get_data_info(self):
        #获得表中的详细数据
        data=[]
        for i in self.table.index.values:
            data_dict=self.table.loc[i].to_dict()
            data.append(data_dict)
        return data

if __name__ == '__main__':
    operation=OperationExcel("../data/text_data.xls")
    print(operation.get_data_info())
