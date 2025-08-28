import pandas
import random
import csv
from faker import Faker

fake = Faker()

num_row = int(input("Enter the Number or Rows You want to Generate"))


csv_file = input("Enter the the CSV file name" )

with open(csv_file , mode ='w', newline='') as file:
	writer = csv.writer(file)

	header = ['first name', 'Last_name', 'Gender', 'DOB' , 'Email' ,'Address','City','State','Zipcode','Loyality_Program']
	writer.writerow(header)

	for i in range(num_row):
		row = [fake.first_name(),fake.last_name(),random.choice(['M','F','Other','Not Specified']),fake.date(),
	fake.email(),fake.address(),fake.city(),fake.state(),fake.postcode(),random.randint(1,5)]
		writer.writerow(row)


print("Printed Successfully")

