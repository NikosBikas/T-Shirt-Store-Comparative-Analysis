
from Lib.strategy import PayByCredit,PayByBank,PayByCash
import os,platform,random

####################
# Other Functions! #
####################

# Function that Checks User OS For Clearing The Screen
def clear():
	if(platform.system() == "Windows"): #Checking User OS For Clearing The Screen
		os.system('cls') 
	else:
		os.system('clear')

# Banner! 
def print_banner(title="Welcome to my Store - Software ver:0.02 - Author: Nikolaos Bikas"):
    print("""
███████╗██╗  ██╗██╗██████╗ ████████╗    ███████╗████████╗ ██████╗ ██████╗ ███████╗
██╔════╝██║  ██║██║██╔══██╗╚══██╔══╝    ██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝
███████╗███████║██║██████╔╝   ██║       ███████╗   ██║   ██║   ██║██████╔╝█████╗  
╚════██║██╔══██║██║██╔══██╗   ██║       ╚════██║   ██║   ██║   ██║██╔══██╗██╔══╝  
███████║██║  ██║██║██║  ██║   ██║       ███████║   ██║   ╚██████╔╝██║  ██║███████╗
╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝   ╚═╝       ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
""")
    total_len = 85
    if title:
        padding = total_len - len(title) - 4
        print("= {} {}\n".format(title, "=" * padding))
    else:
        print("{}\n".format("=" * total_len)) 

##############
## Classes! ##
##############
class Shirt_Characteristics: #This is the context class for the strategy Pattern
    color = sorted(['red','orange','yellow','green','blue','indigo','violet']) #In this line and above  are the lists with the accepted inputs for color,size,fabric and payment
    size = ['xs','s','m','l','xl','xxl','xxxl']
    fabric = sorted(['wool','cotton','polyester','rayon','linen','cashmere','silk'])
    payment = sorted(['credit','bank','cash'])

    #dictionaries with the price of each color,size and fabric
    color_prices={'red': 7 , 'orange': 5.70 , 'yellow': 5.60, 'green': 5.90 , 'blue': 6.20 , 'indigo': 7.30,'violet': 6.60 }
    size_prices={'xs': 5, 's': 5.5, 'm': 6.5, 'l': 7.2, 'xl': 7.8, 'xxl': 8, 'xxxl':8.5}
    fabric_prices={'wool' : 10, 'cotton': 13, 'polyester': 11.5, 'rayon':14, 'linen': 12, 'cashmere':16, 'silk':15.5}
    
    def __init__(self, t_color=None, t_size=None, t_fabric=None, t_payment=None, strategy=None ) : #init of Shirt_Characteristics
        self._t_color = t_color
        self._t_size = t_size
        self._t_fabric = t_fabric
        self._t_payment = t_payment
        self._strategy = strategy
        
        #Dummie data for T-shirts if no parameters are given to Tshirt
        if t_color is None:    
            self._t_color = self.color[random.randrange(len(self.color))] #random color choice
            self._t_color = self.color.index(self._t_color) #taking the indexes of colors so the sort methodrithms work with numbers and not words.
           
        if t_size is None:
            self._t_size = self.size[random.randrange(len(self.size))]
            self._t_size = self.size.index(self._t_size) #taking the indexes of sizes so the sort methodrithms work with numbers and not words.

        if t_fabric is None:
            self._t_fabric = self.fabric[random.randrange(len(self.fabric))]
            self._t_fabric = self.fabric.index(self._t_fabric) #taking the indexes of sizes so the sort methodrithms work with numbers and not words.

        if t_payment is None:
            self._t_payment = self.payment[random.randrange(len(self.payment))]
        if strategy is None:
            if self._t_payment == 'credit':
                self._strategy = PayByCredit()
            elif self._t_payment == 'bank':
                self._strategy = PayByBank()
            elif self._t_payment == 'cash':
                self._strategy = PayByCash()
                
    def __str__(self): # Overide str method for print necessary info for given assignment
        return f"T-Shirt | Size: {self.size[self._t_size]} | Color: {self.color[self._t_color]} | Material: {self.fabric[self._t_fabric]}."

    #Properties and setters for getting the protected attributes
    @property
    def t_color(self):
        return self._t_color

    @property
    def t_size(self):
        return self._t_size

    @property
    def t_fabric(self):
        return self._t_fabric

    @property
    def t_payment(self):
        return self._t_payment

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter #setter for strategy so it can be redefined outside the class
    def strategy(self,value):
        self._strategy = value

        
    def executeStrategy(self): #The function that executes the chosen strategy
        return self._strategy.dopayment(self)

    def totalCost(self): # Function that culculates the total cost of each t-shirt object
        total_cost = self.color_prices[self.t_color] + self.size_prices[self.t_size] + self.fabric_prices[self.t_fabric]
        return total_cost
    
    #function for checking if feature of t-shirt1 is greater than feature of t-shirt2.
    #It's use is for making the procedure automatic by giving for input into the function self(wich is the tshirt1), T-shirt2 and the feature or features  by wich the T-shirts need to be sorted    
    def greaterThan(self, t_shirt2, feature): 
        if type(feature) == list:
            for feat in feature:
                if getattr(self, feat) > getattr(t_shirt2, feat):
                    return True
                elif getattr(self, feat) < getattr(t_shirt2, feat):
                    return False
            return False
        else:
            return getattr(self, feature) > getattr(t_shirt2, feature)
            
    #function for checking if feature of t-shirt1 is greater than or equal to feature of t-shirt2.
    def greaterThanEqual(self, t_shirt2, feature): 
        if type(feature) == list:
            for featIndex, feat in enumerate(feature):
                if getattr(self, feat) > getattr(t_shirt2, feat):
                    return True
                elif getattr(self, feat) < getattr(t_shirt2, feat):
                    return False
                elif getattr(self, feat) == getattr(t_shirt2, feat) and featIndex == (len(feature) - 1):
                    return True
            return False
        else:
            return getattr(self, feature) >= getattr(t_shirt2, feature)

    #function for checking if feature of t-shirt1 is less than feature of t-shirt2.    
    def lessThan(self, t_shirt2, feature):
        if type(feature) == list:
            for feat in feature:
                if getattr(self, feat) < getattr(t_shirt2, feat):
                    return True
                elif getattr(self, feat) > getattr(t_shirt2, feat):
                    return False
            return False
        else:
            return getattr(self, feature) < getattr(t_shirt2, feature)

    #function for checking if feature of t-shirt1 is less than or equal to feature of t-shirt2.    
    def lessThanEqual(self, t_shirt2, feature):
        if type(feature) == list:
            for featIndex, feat in enumerate(feature):
                if getattr(self, feat) < getattr(t_shirt2, feat):
                    return True
                elif getattr(self, feat) > getattr(t_shirt2, feat):
                    return False
                elif getattr(self, feat) == getattr(t_shirt2, feat) and featIndex == (len(feature) - 1):
                    return True
            return False
        else:
            return getattr(self, feature) <= getattr(t_shirt2, feature)

    #get number of buckets for bucketSorting
    def bucketsNum(features):
        featureToArray = {'_t_color':Shirt_Characteristics.color,'_t_size':Shirt_Characteristics.size,'_t_fabric':Shirt_Characteristics.fabric,'_t_payment':Shirt_Characteristics.payment}
        return len(featureToArray[features[0]])
    
    #get bucket index for bucketSorting
    def toIndex(self,features, asc=True):
        featureToArray = {'_t_color':Shirt_Characteristics.color,'_t_size':Shirt_Characteristics.size,'_t_fabric':Shirt_Characteristics.fabric,'_t_payment':Shirt_Characteristics.payment}
        if asc:
            return getattr(self, features[0])
        else:
            return (len(featureToArray[features[0]]) - 1) - getattr(self, features[0])

class User_Input:
    @staticmethod
    def checkChoices(message,options,errorMessage): ##function for checking the inputs (use for many cases. message for the user, options for values to check and errorMessage if something goes wrong
        inputVal = input(message).upper()
        while inputVal not in options:
            print(errorMessage)
            print()
            inputVal = input(message).upper()
        return inputVal
    
    @staticmethod
    def tshirt_buy(tshirt_list,case=False): #function for t-shirt transaction
        if case:
            print('Please give the info for the t-shirt you want to buy.\n')
        clear()
        print_banner("- Here you can add one or more T-shirts to the shopping Cart -")
        print("T-shirt's availabe Colors: "+','.join([color.capitalize() for color in Shirt_Characteristics.color])+".")
        Tshirt_color = User_Input.checkChoices("Give T-shirt's color: ",[color.upper() for color in Shirt_Characteristics.color],'Wrong color.Please give one of: '+','.join([color.capitalize() for color in Shirt_Characteristics.color])+'.').lower()
        clear()
        print_banner("- Here you can add one or more T-shirts to the shopping Cart -")
        print("T-shirt's availabe sizes: "+','.join([size.capitalize() for size in Shirt_Characteristics.size])+".")
        Tshirt_size = User_Input.checkChoices("Give T-shirt's size: ",[size.upper() for size in Shirt_Characteristics.size],'Wrong size.Please give one of: '+','.join([size.capitalize() for size in Shirt_Characteristics.size])+'.').lower()
        clear()
        print_banner("- Here you can add one or more T-shirts to the shopping Cart -")
        print("T-shirt's availabe fabric: "+','.join([fabric.capitalize() for fabric in Shirt_Characteristics.fabric])+".")
        Tshirt_fabric = User_Input.checkChoices("Give T-shirt's fabric: ",[fabric.upper() for fabric in Shirt_Characteristics.fabric],'Wrong fabric.Please give one of: '+','.join([fabric.capitalize() for fabric in Shirt_Characteristics.fabric])+'.').lower()
        clear()
        print_banner("- Here you can add one or more T-shirts to the shopping Cart -")
        print("Please choose a payment method from the following list: "+','.join([payment.capitalize() for payment in Shirt_Characteristics.payment])+".")
        Tshirt_payment = User_Input.checkChoices("Give payment method: ",[payment.upper() for payment in Shirt_Characteristics.payment],'Wrong payment method.Please give one of: '+','.join([payment.capitalize() for payment in Shirt_Characteristics.payment])+'.').lower()

        new_Tshirt = Shirt_Characteristics ( t_color = Tshirt_color, t_size = Tshirt_size, t_fabric = Tshirt_fabric , t_payment = Tshirt_payment, strategy=None )
        tshirt_list.append(new_Tshirt) #fill the tshirt list with as many as tshirt user likes
        clear()
        print_banner("- Here you can add one or more T-shirts to the shopping Cart -") 
        anotherDec = User_Input.checkChoices("Want to add another t-shirt to the Cart? Type 'y' for yes and 'n' for no.",['Y','N'],'Wrong choice!') #ask user for adding another t-shirt
        if anotherDec == 'Y': #if yes fill inputs for another t-shirt
            User_Input.tshirt_buy(tshirt_list,case=True) 
        else:
            clear()
            print_banner("- Here you can add one or more T-shirts to the shopping Cart -")
            print("T-shirt('s) added succesfully to the Cart.")
            print("\nPress Enter to return at the main menu...")
        return tshirt_list #return tshirt list to main module.

###############
## Algorithms #       
###############
class Algorithms:
    '''BucketSort Algorithm'''
    def insertionSort(b,features,asc=True): #insertionSort algorithm for sorting the buckets/ b is the bucket / features is by wich feature to be sorted / asc is for ascending if true and descending if false
        for i in range(1, len(b)):
            up = b[i]
            j = i - 1
            while ( j >= 0 and b[j].greaterThan(up,features) and  asc) or (j >= 0 and b[j].lessThan(up,features) and not asc): 
                b[j + 1] = b[j]
                j -= 1
            b[j + 1] = up    
        return b    

    # The main function that implements bucketSort 
    def bucketSort(x, features, asc=True): # x is the array to be sorted / features is by wich feature to be sorted / asc is for ascending if true and descending if false
        slot_num = Shirt_Characteristics.bucketsNum(features) 
        arr = [[] for i in range(slot_num)]
        
        # Put array elements in different buckets
        for j in x:
            index_b = j.toIndex(features, asc)
            arr[index_b].append(j)
        
        # Sort individual buckets
        for i in range(len(arr)):
            arr[i] = Algorithms.insertionSort(arr[i],features,asc)
            
        # concatenate the result
        k = 0
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                x[k] = arr[i][j]
                k += 1
        return x

    '''BubbleSort Algorithm'''
    def bubbleSort(data,features,asc=True): #data is the data to be sorted / features is by wich feature to be sorted / asc is for ascending if true and descending if false
        n = len(data)
        for i in range(n-1):
            for j in range(0,n-i-1):
                if (data[j].greaterThan(data[j+1],features) and asc) or (data[j].lessThan(data[j+1],features) and not asc): 
                    data[j], data[j+1] = data[j+1], data[j]

    '''Quick sort algorithm'''
    # This Function handles sorting part of quick sort
    # start and end points to first and last element of
    # an array respectively
    def partition(array, features, asc, start, end):
        pivot_index = start 
        pivot = array[pivot_index]
        while start < end:
            while start < len(array) and ((array[start].lessThanEqual(pivot,features) and asc) or (array[start].greaterThanEqual(pivot,features) and not asc)):
                start += 1
            while (array[end].greaterThan(pivot,features) and asc) or (array[end].lessThan(pivot,features) and not asc):
                end -= 1
            if(start < end):
                array[start], array[end] = array[end], array[start]
        array[end], array[pivot_index] = array[pivot_index], array[end]
        return end
      
    # The main function that implements QuickSort 
    def quick_sort(array, features, asc=True, start=0, end=None): #array is the data to be sorted / features is by wich feature to be sorted / asc is for ascending if true and descending if false / start is starting point of array / end is end point of array
        if end is None: end = len(array)-1
        if (start < end):
            p = Algorithms.partition(array, features, asc, start, end)
            Algorithms.quick_sort(array, features, asc, start, p - 1)
            Algorithms.quick_sort(array, features, asc, p + 1, end)


class Call(User_Input,Shirt_Characteristics,Algorithms):

    def bubble_sort(shirts_list):
        if len(shirts_list) == 0:            
            print('You have to create the dummy list first in order to continue!\n')
        else:
            for case in range(1,9):
                if case == 1:#Case1 --> Size in ascending
                    features=['_t_size'] # sorting variables
                    Algorithms.bubbleSort(shirts_list,features)
                    print('Size in ascending order using BubbleSort Method!')
                    print('-------------------------------------------------')
                elif case == 2:#Case2 --> Size in descending
                    features=['_t_size']
                    Algorithms.bubbleSort(shirts_list,features,asc=False)
                    print('Size in descending order using BubbleSort Method!')
                    print('--------------------------------------------------')
                elif case == 3:#Case3 --> Color in ascending
                    features=['_t_color'] # sorting variables
                    Algorithms.bubbleSort(shirts_list,features)
                    print('Color in ascending order using BubbleSort Method!')
                    print('--------------------------------------------------')
                elif case == 4:#Case3 --> Color in descending
                    features=['_t_color']
                    Algorithms.bubbleSort(shirts_list,features,asc=False)
                    print('Color in descending order using BubbleSort Method!')
                    print('---------------------------------------------------')
                elif case == 5:#Case5 --> Fabric in ascending
                    features=['_t_fabric'] # sorting variables
                    Algorithms.bubbleSort(shirts_list,features)
                    print('Fabric in ascending order using BubbleSort Method!')
                    print('---------------------------------------------------')
                elif case == 6:#Case6 --> Fabric in descending
                    features=['_t_fabric']
                    Algorithms.bubbleSort(shirts_list,features,asc=False)
                    print('Fabric in descending order using BubbleSort Method!')
                    print('----------------------------------------------------')
                elif case == 7:#Case7 --> Size and Color and Fabric in ascending
                    features=['_t_size','_t_color','_t_fabric']
                    Algorithms.bubbleSort(shirts_list,features)
                    print('Size, Color and Fabric in ascending order using BubbleSort Method!')
                    print('-------------------------------------------------------------------')
                elif case == 8:
                    features=['_t_size','_t_color','_t_fabric']
                    Algorithms.bubbleSort(shirts_list,features,asc=False)
                    print('Size, Color and Fabric in descending order using BubbleSort Method!')
                    print('--------------------------------------------------------------------')
                x=1
                for shirt in shirts_list:
                    print(f"{x}: {shirt}")
                    x=x+1
                print()
        
    def bucket_sort(shirts_list):
        if len(shirts_list) == 0:            
            print('You have to create the dummy list first in order to continue!\n')
        else:
            for case in range(1,9):
                if case == 1:#Case1 --> Size in ascending
                    features=['_t_size'] # sorting variables
                    Algorithms.bucketSort(shirts_list,features,asc=True)
                    print('Size in ascending order using BucketSort Method!')
                    print('-------------------------------------------------')
                elif case == 2:#Case2 --> Size in descending
                    features=['_t_size']
                    Algorithms.bucketSort(shirts_list,features,asc=False)
                    print('Size in descending order using BucketSort Method!')
                    print('--------------------------------------------------')
                elif case == 3:#Case3 --> Color in ascending
                    features=['_t_color'] # sorting variables
                    Algorithms.bucketSort(shirts_list,features)
                    print('Color in ascending order using BucketSort Method!')
                    print('--------------------------------------------------')
                elif case == 4:#Case3 --> Color in descending
                    features=['_t_color']
                    Algorithms.bucketSort(shirts_list,features,asc=False)
                    print('Color in descending order using BucketSort Method!')
                    print('---------------------------------------------------')
                elif case == 5:#Case5 --> Fabric in ascending
                    features=['_t_fabric'] # sorting variables
                    Algorithms.bucketSort(shirts_list,features)
                    print('Fabric in ascending order using BucketSort Method!')
                    print('---------------------------------------------------')
                elif case == 6:#Case6 --> Fabric in descending
                    features=['_t_fabric']
                    Algorithms.bucketSort(shirts_list,features,asc=False)
                    print('Fabric in descending order using BucketSort Method!')
                    print('----------------------------------------------------')
                elif case == 7:#Case7 --> Size and Color and Fabric in ascending
                    features=['_t_size','_t_color','_t_fabric']
                    Algorithms.bucketSort(shirts_list,features)
                    print('Size, Color and Fabric in ascending order using BucketSort Method!')
                    print('-------------------------------------------------------------------')
                elif case == 8:
                    features=['_t_size','_t_color','_t_fabric']
                    Algorithms.bucketSort(shirts_list,features,asc=False)
                    print('Size, Color and Fabric in descending order using BucketSort Method!')
                    print('--------------------------------------------------------------------')
                x=1
                for shirt in shirts_list:
                    print(f"{x}: {shirt}")
                    x=x+1
                print()
    
    def quick_sort(shirts_list):
        if len(shirts_list) == 0:            
            print('You have to create the dummy list first in order to continue!\n')
        else:
            for case in range(1,9):
                if case == 1:#Case1 --> Size in ascending
                    features=['_t_size'] # sorting variables
                    Algorithms.quick_sort(shirts_list,features)
                    print('Size in ascending order using QuickSort')
                    print('-------------------------------------------------')
                elif case == 2:#Case2 --> Size in descending
                    features=['_t_size']
                    Algorithms.quick_sort(shirts_list,features,asc=False)
                    print('Size in descending order using QuickSort')
                    print('--------------------------------------------------')
                elif case == 3:#Case3 --> Color in ascending
                    features=['_t_color'] # sorting variables
                    Algorithms.quick_sort(shirts_list,features)
                    print('Color in ascending order using QuickSort')
                    print('--------------------------------------------------')
                elif case == 4:#Case3 --> Color in descending
                    features=['_t_color']
                    Algorithms.quick_sort(shirts_list,features,asc=False)
                    print('Color in descending order using QuickSort')
                    print('---------------------------------------------------')
                elif case == 5:#Case5 --> Fabric in ascending
                    features=['_t_fabric'] # sorting variables
                    Algorithms.quick_sort(shirts_list,features)
                    print('Fabric in ascending order using QuickSort')
                    print('---------------------------------------------------')
                elif case == 6:#Case6 --> Fabric in descending
                    features=['_t_fabric']
                    Algorithms.quick_sort(shirts_list,features,asc=False)
                    print('Fabric in descending order using QuickSort')
                    print('----------------------------------------------------')
                elif case == 7:#Case7 --> Size and Color and Fabric in ascending
                    features=['_t_size','_t_color','_t_fabric']
                    Algorithms.quick_sort(shirts_list,features)
                    print('Size, Color and Fabric in ascending order using QuickSort')
                    print('-------------------------------------------------------------------')
                elif case == 8:
                    features=['_t_size','_t_color','_t_fabric']
                    Algorithms.quick_sort(shirts_list,features,asc=False)
                    print('Size, Color and Fabric in descending order using QuickSort')
                    print('--------------------------------------------------------------------')
                x=1
                for shirt in shirts_list:
                    print(f"{x}: {shirt}")
                    x=x+1
                print()

    @staticmethod
    def ViewCart(tshirt_list):
        if len(tshirt_list) == 0:
            print ("Shopping Cart is empty!")
            input('\nPress Enter to return at the main menu...')
            return
        else:      
            list_len= len(tshirt_list)
            print(f"Total items in the Cart:{list_len} \nWith the following characteristics:\n ")  
            for tshirt in tshirt_list: #for loop for printing all the t-shirts_list and check what strategy plan to apply depending on user's payment method choice.
                if tshirt.t_payment == 'credit' :
                    tshirt.strategy = PayByCredit() #apply the right strategy plan
                    print(tshirt.executeStrategy()) # call the right strategy plan
                    print('')
                elif tshirt.t_payment == 'bank' :               
                    tshirt.strategy = PayByBank()
                    print(tshirt.executeStrategy())
                    print('')
                else:
                    tshirt.strategy = PayByCash()
                    print(tshirt.executeStrategy())
                    print('')    
            input('\nPress Enter to return at the main menu...')
    
    @staticmethod
    def Transaction(tshirt_list):
        if len(tshirt_list) == 0:
            print ("Shopping Cart is empty!")
            input('\nPress Enter to return at the main menu...')
            return  
        else:      
            list_len= len(tshirt_list)
            print(f"Total items in the Cart:{list_len} \nWith the following characteristics:\n ")  
            for tshirt in tshirt_list: #for loop for printing all the t-shirts_list and check what strategy plan to apply depending on user's payment method choice.
                if tshirt.t_payment == 'credit' :
                    tshirt.strategy = PayByCredit() #apply the right strategy plan
                    print(tshirt.executeStrategy()) # call the right strategy plan
                    print('')
                elif tshirt.t_payment == 'bank' :               
                    tshirt.strategy = PayByBank()
                    print(tshirt.executeStrategy())
                    print('')
                else:
                    tshirt.strategy = PayByCash()
                    print(tshirt.executeStrategy())
                    print('')
            tshirt_list.clear()
            print('\nT-shirt transaction completed succesfully.')
            input('\nPress Enter to return at the main menu...')

    @staticmethod
    def createDummyData(dummy_tshirt_list):
        if len(dummy_tshirt_list) == 0: 
            shirts_list = [Shirt_Characteristics() for i in range(40)]
            print()
            x=1
            for shirt in shirts_list: #print Dummy T-shirts before use of methodrithms
                #print(f"{x}: {shirt}")
                x=x+1
                dummy_tshirt_list.append(shirt)
            print('Dummy List Created Succesfully!\n')
        else:
            print('Dummy List allready exists!\n')

    
    @staticmethod
    def listBeforeSort(dummy_tshirt_list):
        if len(dummy_tshirt_list) == 0:
            print('You have to create the dummy list first in order to continue!\n')
        else:
            x=1
            for shirt in dummy_tshirt_list:
                print(f"{x}: {shirt}")
                x=x+1
        
    





                    
