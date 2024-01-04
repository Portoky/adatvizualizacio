import csv
import pandas as pd


def modify():
    input_csv_path = 'd:/Universitate/MCC/Adatvizualizacio/african-elephants.csv'
    output_csv_path = 'd:/Universitate/MCC/Adatvizualizacio/modified-african-elephants.csv'
    with open(input_csv_path, 'r') as input_data, open(output_csv_path, 'w', newline='') as output_data:
        csv_reader = csv.DictReader(input_data)
        csv_writer = csv.DictWriter(output_data, fieldnames=[field for field in csv_reader.fieldnames if field not in ['Code', 'Entity'] ])
        header = next(csv_reader)
        csv_writer.writeheader()

        years_so_far = {}
        for record in csv_reader:
            if record["Year"] not in years_so_far:
                years_so_far[record["Year"]] = int(record["African Elephant population (AfESG, 2019)"])
            else:
                 years_so_far[record["Year"]] += int(record["African Elephant population (AfESG, 2019)"])
        for data in years_so_far:
            csv_writer.writerow({"Year": str(data), "African Elephant population (AfESG, 2019)":str(years_so_far[data])})

if __name__=='__main__':
    #df = pd.read_csv('african-elephants.csv')   
    #df[['year', 'sex', 'age', 'suicides_no']].set_index(['year', 'sex', 'age']).unstack().reset_index().to_csv("data.csv")
    modify()