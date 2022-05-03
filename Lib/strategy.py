import abc

#interface creation for the strategy
class Strategy (metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def dopayment(self):
        pass

#concrete strategy classes creation

class PayByCredit(Strategy): #concrete strategy class for payment via credit card

    def dopayment(self,product): 
        return (f"Color:      {product.t_color.upper()} (with price tag {product.color_prices[product.t_color]}€)" \
                f"\nSize:       {product.t_size.upper()} (with price tag {product.size_prices[product.t_size]}€) \nFabric:     {product.t_fabric.upper()} (with price tag {product.fabric_prices[product.t_fabric]}€)" \
                f"\nTotal cost: {product.totalCost()}€"\
                f"\nPayment method: Credit Card")
    
class PayByBank(Strategy): #concrete strategy class for payment via Bank transfer

    def dopayment(self,product):
        return (f"Color:      {product.t_color.upper()} (with price tag {product.color_prices[product.t_color]}€)" \
                f"\nSize:       {product.t_size.upper()} (with price tag {product.size_prices[product.t_size]}€) \nFabric:     {product.t_fabric.upper()} (with price tag {product.fabric_prices[product.t_fabric]}€)" \
                f"\nTotal cost: {product.totalCost()}€"\
                f"\nPayment method: Bank Transfer")

class PayByCash(Strategy): #concrete strategy class for payment via cash 

    def dopayment(self,product):
        return (f"Color:      {product.t_color.upper()} (with price tag {product.color_prices[product.t_color]}€)" \
                f"\nSize:       {product.t_size.upper()} (with price tag {product.size_prices[product.t_size]}€) \nFabric:     {product.t_fabric.upper()} (with price tag {product.fabric_prices[product.t_fabric]}€)" \
                f"\nTotal cost: {product.totalCost()}€"\
                f"\nPayment method: Cash")


