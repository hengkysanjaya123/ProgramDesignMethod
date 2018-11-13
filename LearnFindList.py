class ReportData:

    def __init__(self,name, age):
        self.name = name
        self.age = age


def main():
    rd1 = ReportData('test', 12)
    rd2 = ReportData('coba', 15)
    rd3 = ReportData('coba', 17)
    rd4 = ReportData('coba', 18)

    list = []
    list.append(rd2)
    list.append(rd1)
    list.append(rd3)
    list.append(rd4)


    list.sort(key= lambda x:x.age, reverse=True)

    for i in list:
        print(f'Name : {i.name} , Age : {i.age}')





main()