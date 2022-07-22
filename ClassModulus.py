class Category:
    def __init__(self,catName,catId):
        self.catName = catName
        self.catId = catId
    def __str__(self):
        return f"Category Name:{self.catName}\nCategory ID :{self.catId}\n"
    def Getid(self):
        return self.catId
#----------------------------------------------------------------
class Customer():
    def __init__(self,cName,cid,cFamily,cAddress,cTel,cWallet):
        self.cName = cName
        self.cid=cid
        self.cFamily = cFamily
        self.cAddress = cAddress
        self.cTel = cTel
        self.cWallet = cWallet
    def __str__(self):
        return f"Name :{self.cName}\nFamily :{self.cFamily}\nID : {self.cid}\nAddress :{self.cAddress}\nTel :{self.cTel}\nWallet :{self.cWallet}\n"     
    def Getid(self):
        return self.cid
    def GetWallet(self):
        return self.cWallet 
    def ChangeWallet(self,input):
        self.cWallet += input  
    def Addbascket(self,product,name,unit,cost,time):
        bascketfile=open("Sale System/Files/bascketfile.txt",'a')
        bascketfile.write(name+product+unit+cost+time)
        bascketfile.close()
    def CustAddFile(self):
        return f"Name :{self.cName}\nFamily :{self.cFamily}\nID : {self.cid}\nAddress :{self.cAddress}\nTel :{self.cTel}\n"     
#----------------------------------------------------------------
class Product(Category):
    def __init__(self,pName,pId,pPrice,pStock,catName):
        self.pName = pName
        self.pId = pId
        self.pPrice = pPrice
        self.pStock = pStock
        self.pCategory = catName
    def __str__(self):
        return f"Name : {self.pName}\nPrice :{self.pPrice}\nStock :{self.pStock}\nCategory :{self.pCategory}\n"
    def GetName(self):
        return f"Product Name : {self.pName}\n"
    def Getid(self):
        return self.pId
    def GetPrice(self):
        return self.pPrice
    def GetStock(self):
        return self.pStock
    def ChangeStock(self,input):
        self.pStock +=input
    def ChangePrice(self,input):
        self.pPrice +=input
    def ProAddFile(self):
        return f"Name : {self.pName}\nPrice :{self.pPrice}\nCategory :{self.pCategory}\n"
#----------------------------------------------------------------  
class Shop(Product,Category,Customer):
    def __init__(self,shopname):
        self.shopname = shopname
        self.categoryList=[]
        self.productsList = []
        self.CostumersList = []
    def GetName(self):
        return self.shopname
    def getPname(self,idp):
        for product in self.productsList:
            if idp==product.Getid():
                return product.GetName()    
    ################################
    # Add 
    def addcategory(self,category)  :
        self.categoryList.append(category)   
    def addProduct(self,product):
        self.productsList.append(product)  
    def addCostumers(self,costumer):
        self.CostumersList.append(costumer) 
    def addbascket(self,idcu,productname,unit,cost,time):
        for customer in self.CostumersList:
            if idcu == customer.Getid():
                name=customer.CustAddFile()
                customer.Addbascket(productname,name,unit,cost,time)
    ################################  
    # Show the list of
    def ShowProductList(self):
        for p in self.productsList: 
            print (p)
    def ShowCategoryList(self):
        for cat in self.categoryList: 
            print(cat)
    def ShowCostumerList(self):
        for cus in self.CostumersList: 
            print(cus)
    ################################ 
    # Show Selected 
    def ShowProduct(self,idp):
        for product in self.productsList:
            if idp==product.Getid():
                print(product)   
    def ShowCategory(self,idcat):
        for category in self.categoryList:
            if idcat==category.Getid():
                print(category) 
    def ShowCustomer(self,idcus):
        for customer in self.CostumersList:
            if idcus==customer.Getid():
                print(customer) 
    def ShowBascket(self):
        bascketfile=open("Sale System/Files/bascketfile.txt",'r')
        print(bascketfile.read())
        bascketfile.close()
    ################################
    # Change Stock
    def ChangeProductStock(self,input,idp):
        for product in self.productsList:
            if idp==product.Getid():
                product.ChangeStock(input)
    # Change Price
    def ChangeProductPrice(self,input,idp):
        for product in self.productsList:
            if idp==product.Getid():
                product.ChangePrice(input)
    # Change Wallet
    def ChangeWallets(self,input,idcu):
        for customer in self.CostumersList:
            if idcu==customer.Getid():
                customer.ChangeWallet(input)
    ################################
    # Sell  
    def getPricep(self,idp): 
        for product in self.productsList:
            if idp==product.Getid():
                return product.GetPrice()
    def getstock(self,idp):
        for product in self.productsList:
            if idp==product.Getid():
                return product.GetStock()
    def getwallet(self,idp): 
        for customer in self.CostumersList:
            if idp==customer.Getid():
                return customer.GetWallet()
#----------------------------------------------------------------  