# libraries
import stock_info

BMO = stock_info.Stock_Object("BMO")
BMO.Update()
BMO.History()
print(BMO.price)

# TSLA = stock_info.Stock_Object("TSLA")
# TSLA.Update()
# print(TSLA.price)

print("done")