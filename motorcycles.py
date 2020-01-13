motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles.insert(0,'ducati')
print(motorcycles)
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
dod_motorcycles=motorcycles.pop()
print(motorcycles)
print(dod_motorcycles)
print("我买的最后一辆摩托车是"+dod_motorcycles.title()+".")
first_motorcycle=motorcycles.pop(0)
print("我买的第一辆摩托车是"+first_motorcycle.title()+".")
print(motorcycles)
motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+" is too exprnsive for me")
