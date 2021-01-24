import phonenumbers
from phonenumbers import carrier
from tabulate import tabulate
def number_scan(phone):
    number=phonenumbers.parse(phone)
    des=geocoder.descriptiong_for_number(number,'en')
    sup=carrier.name_for_number(number,'en')
    info=[['Country','Supplier']],[des,sup]
    data=str(tabulate(info,headers='firstrow',tablefmt='github'))
    return data
if __name__ =='__main__':
    number=input("Enter Number:")
    print(number_scan(number))
