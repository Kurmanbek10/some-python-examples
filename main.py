print("Hello Batch 25c")

batch = "Hello 25c"
microphone = ["Team", '25c', "Saturday", 14, "February"]
print(batch)

microphone.append("Valentine's Day")
print(microphone)
print(type(microphone))

name = "Alex"
job_title = "Software Developer"
years_experience = 7
print(f"Hi, my name is {name}. I work as a {job_title}. I have {years_experience} years of experience")
print("Hi, my name is " + name + ". I work as a " + job_title)

city = "Chicago"
print(city[0:2]+city[5:])
print(city[-3:])
print(city[:3])
print(city[1:3])

numbers = "0123456789"
print(numbers[1:8:2])

#Dictionaries
car = {"make": "toyota", "model":"rav4", "year": "2026", "color": "pink", "model": "camry"}

print(car["make"],car["model"],car["year"]+" "+car["color"])
print(car)

#Lists
services = ["Git", "EC2", "Docker", "kubernetes", "IAM", "S3", "EFS"]
platform = "AWS"
print(type(services))
print(services[3])
print(services[-4])
print(services[2:5])
print(len(services))
print(len(platform))

item = "Melon"
price = 6
item = input("the name of the item: ")
price = input("price for an item: ")
print("The price for Melon is $6")
print(f"The price for {item} is ${price}")

# String methods

name = "gerald is a nice guy"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.split())

# List methods
# Append
services = ["Git", "EC2", "Docker", "kubernetes", "IAM", "S3", "EFS"]
services.append("Bash")

print(services)


# Extend
services = ["Git", "EC2", "Docker", "kubernetes", "IAM", "S3", "EFS"]
services2 = ["Bash", "Lambda", "RDS"]
services.extend(services2)

print(services)

# Insert
services = ["Git", "EC2", "Docker", "kubernetes", "IAM", "S3", "EFS"]
services.insert(2, "Bash")

print(services)

# Remove
services = ["Git", "EC2", "Docker", "kubernetes", "IAM", "S3", "EFS"]
services.remove(services[-1])

print(services)

# POP
services = ["Git", "EC2", "Docker", "kubernetes", "IAM", "S3", "EFS"]
services.pop()

print(services)

# Count
services = ["Git", "EC2", "Docker", "kubernetes", "IAM", "S3", "EFS", "Git", "S3", "Git"]

print(services.count("Git"))
print(services.count("S3"))
print(services.count("Docker"))


# Sort
services = ["Git", "EC2", "Docker", "kubernetes", "IAM", "S3", "EFS", "Git", "S3", "Git"]
(services.sort())

print(services)


# Reverse
services = ["Git", "EC2", "Docker", "kubernetes", "IAM", "S3", "EFS"]
(services.reverse())

print(services)


# Clear
services = ["Git", "EC2", "Docker", "kubernetes", "IAM", "S3", "EFS"]
services.clear()

print(services)

# Dictionary methods

# Keys and values
car = {"make": "toyota", "model":"rav4", "year": "2026", "color": "pink"}

print(car.values())
print(car.keys())

# Update
car = {"make": "toyota", "model":"rav4", "year": "2026", "color": "pink"}

car["make"] = "lexus"
print(car)

car.update({"make":"ford"})
print(car)

# Conver strings/integers

age = "12"
age = int(age)
print(type(age))

print(list("abcd"))
print(float(140))

# TASK 1
# Storage usage report
total_storage_gb = 500
used_storage_gb = 356

# 1. Calculate the used storage percentage
# 2. Print: "Storage used: 71.2%" ()

percentage = (used_storage_gb/total_storage_gb)*100
print(percentage)
print(f"Storage used: {percentage}%")



# TASK 2:
server_info = ("server01", "192.168.1.12", "Ubuntu 22.04")
# Server name: server01
# IP Address: 192.168.1.12
# OS: Ubuntu 22.04

print(f"Server name: {server_info[0]}")
print(f"IP Address: {server_info[1]}")
print(f"OS: {server_info[2]}")
print("Server name: " + server_info[0])

print("10", "20")