# // Created by Mersad MacBook
import datetime
import os
from ClassModulus import Customer,Category,Product,Shop
def DefineFile():
    categoryfile=open("Sale System/Files/categoryfile.txt",'a')
    categoryfile.close()
    productfile=open("Sale System/Files/productfile.txt",'a')
    productfile.close()
    customerfile=open("Sale System/Files/customerfile.txt",'a')
    customerfile.close()
    storefile=open("Sale System/Files/storefile.txt",'a')
    storefile.close()
    bascketfile=open("Sale System/Files/bascketfile.txt",'a')
    bascketfile.close()
os.system('clear')
Shopname=input(" Shop Name : ")
shop1=Shop(Shopname)
Shopname=shop1.GetName()
categoryCounter=0
productCounter=0
customerCounter=0
DefineFile()
os.system('clear')
print("Hello\n")
print(f"Welcom To {Shopname} Sale System ")
wait=input("\nPress Enter to continue ... ")
os.system('clear')
MainKey=1
while MainKey!=0 :
    print("1.Define\n2.Show\n3.Change Product\n4.Buy\n5.Store\n6.Charge Wallet\n7.Exit\n")
    order=int(input("Enter Order : "))
    os.system('clear')
    match order:
        #Define
        case 1:
            print("1.Category\n2.Product\n3.Customer\n")
            order2=int(input("Enter Order : "))
            os.system('clear')
#----------------------------------------------------------------
#"1.Category 2.Product 4.Customer"
            match order2:
                #Define Category
                case 1:
                    catname=input("Enter Category Name : ")
                    cid=int(input("Enter Category ID : "))
                    cat=Category(catname,cid)
                    shop1.addcategory(cat)
                    categoryfile=open("Sale System/Files/categoryfile.txt",'a')
                    categoryfile.write(cat.__str__())
                    categoryfile.write("__________________________\n")
                    categoryfile.close()
                    categoryCounter+=1
                    os.system('clear')
                #Define Product
                case 2:
                    pname=input("Enter Product Name: ")
                    pId=int(input("Enter Product ID: "))
                    pPrice=int(input("Enter Price: "))
                    pStock=int(input("Enter Stock: "))
                    pCategory=input("Enter Category Name:")
                    pro=Product(pname,pId, pPrice, pStock, pCategory)
                    shop1.addProduct(pro)
                    productfile=open("Sale System/Files/productfile.txt",'a')
                    productfile.write(pro.ProAddFile())
                    productfile.write("__________________________\n")
                    productfile.close()
                    productCounter+=1
                    os.system('clear')
                #Define Customer
                case 3:
                    cname=input("Enter Name: ")
                    cfamily=input("Enter Family: ")
                    cId=int(input("Enter Customer ID :"))
                    caddress=input("Enter Address: ")
                    ctel=input("Enter Tel: ")
                    cwallet=int(input("Enter Wallet: "))
                    cost=Customer(cname,cId,cfamily,caddress,ctel,cwallet) 
                    shop1.addCostumers(cost)
                    customerfile=open("Sale System/Files/customerfile.txt",'a')
                    customerfile.write(cost.CustAddFile())
                    customerfile.write("__________________________\n")
                    customerfile.close()
                    customerCounter+=1
                    os.system('clear')
#----------------------------------------------------------------
        #Show
        case 2:
            print("1.Show List\n2.Show Selected \n3.Show Files\n4.Show History")
            order4=int(input("Enter your order :"))
            os.system('clear')
            match order4:
                # Show List :
                case 1:
                        print("1.Category List\n2.Product List\n3.Customer List\n")
                        order3=int(input("Enter Order : "))
                        os.system('clear')
                        match order3:
                #"1.Category List 2.Product List 3.Customer List"
                        #Show Category List:
                            case 1:
                                shop1.ShowCategoryList()
                                wait=input("\nPress Enter to continue ... ")
                                os.system('clear')
                        #Show Product List:
                            case 2:
                                shop1.ShowProductList()
                                wait=input("\nPress Enter to continue ... ")
                                os.system('clear')
                        #Show Customer List: 
                            case 3: 
                                shop1.ShowCostumerList()
                                wait=input("Press Enter to continue ... ")
                                os.system('clear')
                # Show Selected:
                case 2: 
                    print("1.Category\n2.Product\n3.Customer\n")
                    order5=int(input("Enter Order : "))
                    os.system('clear')
                    match order5:
                        # Show Selected Category
                        case 1:  
                            selectedid=int(input("Enter  Category ID : "))
                            shop1.ShowCustomer(selectedid)
                            wait=input("Press Enter to continue ... ")
                            os.system('clear')
                        # Show Selected Product                           
                        case 2:
                            selectId=int(input("Enter Product ID: "))
                            shop1.ShowProduct(selectId)
                            wait=input("Press Enter to continue ... ")
                            os.system('clear')
                        # Show Selected Customer
                        case 3:
                                selectId=int(input("Enter Customer ID: "))
                                shop1.ShowCustomer(selectId)
                                wait=input("Press Enter to continue ... ")
                                os.system('clear')
                # Show Files
                case 3:
                    print("1.Category\n2.Product\n3.Customer\n")
                    order9=int(input("Enter Order : "))
                    os.system('clear')
                    match order9:
                        case 1:
                            categoryfile=open("Sale System/Files/categoryfile.txt",'r')
                            print(categoryfile.read())
                            categoryfile.close()
                            wait=input("Press Enter to continue ... ")
                            os.system('clear')
                        case 2:
                            productfile=open("Sale System/Files/productfile.txt",'r')
                            print(productfile.read())
                            productfile.close()
                            wait=input("Press Enter to continue ... ")
                            os.system('clear')
                        case 3:
                            customerfile=open("Sale System/Files/customerfile.txt",'r')
                            print(customerfile.read())
                            customerfile.close()
                            wait=input("Press Enter to continue ... ")
                            os.system('clear')
                # Show Selected Bascekt
                case 4:
                    os.system('clear')
                    shop1.ShowBascket()
                    wait=input("Press Enter to continue ... ")
                    os.system('clear')
        #----------------------------------------------------------------
        #Change 
        case 3:
            print("1.Change Stock\n2.Change Price\n")
            order11=int(input("Enter Order Number: "))
            match order11:
                # Change Stock
                case 1:
                    IDp=int(input("Enter Product ID: "))
                    shop1.ShowProduct(IDp)
                    new_Stock=int(input("Enter New Stock : ")) 
                    shop1.ChangeProductStock(new_Stock,IDp)
                    wait1=input("\tTask Done!\n")
                    wait=input("Press Enter to continue ... ")
                    os.system('clear')
                # Change Price
                case 2:
                    IDp=int(input("Enter Product ID: "))
                    shop1.ShowProduct(IDp)
                    new_Price=int(input("Enter New Price : "))
                    shop1.ChangeProductPrice(new_Price,IDp)
                    wait1=input("\tTask Done!\n")
                    wait=input("Press Enter to continue ... ")
                    os.system('clear')
        #----------------------------------------------------------------
        #Sell
        case 4:
            key=1
            while key!=0:
                selectIdc=int(input("Enter Customer ID: "))
                shop1.ShowCustomer(selectIdc)
                selectIdp=int(input("Enter Product ID: "))
                shop1.ShowProduct(selectIdp)
                unit=int(input("Enter Unit: "))
                stockf=int(shop1.getstock(selectIdp))
                if unit <=stockf:
                    cost=int(unit*shop1.getPricep(selectIdp))
                    print(f"Cost: {cost} \n")
                    ch=input("Do You Want to Continue ? y/n :  ")
                    while True:
                        if ch=='y':
                                unitf=unit*-1
                                if cost<=shop1.getwallet(selectIdc):
                                    costf=cost*-1
                                    shop1.ChangeProductStock(unitf,selectIdp)
                                    shop1.ChangeWallets(costf,selectIdc)
                                    pname=shop1.getPname(selectIdp)
                                    saveunit=f"Unit = {unit}\n"
                                    costsave=f"Cost = {cost}\n"
                                    now = datetime.datetime.now()
                                    time=now.strftime("Time : %Y-%m-%d %H:%M:%S\n________________________\n")
                                    shop1.addbascket(selectIdc,pname,saveunit,costsave,time)
                                    print("\tTask Done !")
                                    wait=input("Press Enter to continue ... ")
                                    os.system('clear')
                                    key=0
                                    break;
                                else :
                                    print("You Dont have Enough money")
                                    os.system('clear')
                                    key=0
                                    break;
                        elif ch=='n' : 
                            wait=input("Press Enter to continue ... ")
                            key=0
                            os.system('clear')
                            break;
                else : 
                    print("Stock Not Enough")
                    ch=int(input("Countinue=1  \t  Extit=0 \n"))
                    if ch ==1:
                        os.system('clear')
                    elif ch ==0:
                        wait=input("Press Enter to Exit ... ")
                        key=0
                        os.system('clear')
                        break;   
        #----------------------------------------------------------------
        #Store Information
        case 5:
            wait=input("Save To Store")
            os.system('clear')
            storefile=open("Sale System/Files/storefile.txt",'w')
            storefile.write(f"""{Shopname} Store Information
Category = {categoryCounter}
Customer = {customerCounter}
Product  = {productCounter}""")
            storefile.close()
            storefile=open("Sale System/Files/storefile.txt",'r')
            print(storefile.read())
            storefile.close()
            wait=input("Press Enter to Exit ... ")
            os.system('clear')
        #----------------------------------------------------------------
        # Charge Wallet
        case 6:
            selectId=int(input("Enter Customer ID: "))
            shop1.ShowCustomer(selectId)
            new_wallet=int(input("Charge amount : "))
            shop1.ChangeWallets(new_wallet,selectId)
            print("\tTask Done !")
            wait=input("\nPress Enter to Exit ... ")
            os.system('clear')
        #----------------------------------------------------------------
        #Exit
        case 7:
            print("GOOD LUCK ! <3")
            wait=input("Press Enter to Exit ... ")
            os.system('clear')
            MainKey=0
            break; 
# THE END        