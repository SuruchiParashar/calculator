#calculator
import art
print(art.logo)
#add
def add(n1, n2):
  return n1 + n2

#subtract
def sub(n1, n2):
  return n1 - n2

#multiply
def mul(n1, n2):
  return n1 * n2

#divide
def div(n1, n2):
  return n1 / n2

calculate = {}
calculate["+"] = add
calculate["-"] = sub
calculate["*"] = mul
calculate["/"] = div

def calculator():
  num1 = float(input("Enter first number : "))
  
  for symbol in calculate:
    print(symbol)
  
  should_continue = True
  
  while should_continue:
    user_symbol = input("Enter the operation: ")
    num2 = int(input("Enter the next number : "))
    operated = calculate[user_symbol]
    answer = operated(num1, num2)
    #print(answer)
  
    print(f"{num1} {user_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' if you want to continue calculating with {answer} : ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()  #recursion