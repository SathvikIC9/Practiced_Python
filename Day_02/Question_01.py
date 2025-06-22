# Write a function filter_even(numbers) that takes a list of integers and returns a dictionary with:
# Key: original number

b = {
    "even":[],
    "odd":[]
}
n = [2,3,4,5,7]
i = 0 
  
def  filter_op(n):
    if n % 2 == 0:
         b["even"].append(n) 
    else:
        b["odd"].append(n) 
while i < len(n):
    filter_op(n[i])
    i +=1
print(f"The final dictionary is : {b} ")