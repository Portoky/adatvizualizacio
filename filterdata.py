import csv
import pandas as pd


def modify():
    input_csv_path = 'd:/Universitate/MCC/Adatvizualizacio/master.csv'
    output_csv_path = 'd:/Universitate/MCC/Adatvizualizacio/masterRomania.csv'
    with open(input_csv_path, 'r') as input_data, open(output_csv_path, 'w') as output_data:
        csv_reader = csv.DictReader(input_data)
        csv_writer = csv.DictWriter(output_data, fieldnames=[field for field in csv_reader.fieldnames if field not in ['HDI for year', ' gdp_for_year ($) ', 'country-year'] ])
        header = next(csv_reader)
        print(header)
        csv_writer.writeheader()

        for record in csv_reader:
            if record['ï»¿country'] == 'Romania':
                del record['HDI for year']
                del record[' gdp_for_year ($) ']
                del record['country-year']
                csv_writer.writerow(record)

if __name__=='__main__':
    df = pd.read_csv('masterRomania.csv')   
    df[['year', 'sex', 'age', 'suicides_no']].set_index(['year', 'sex', 'age']).unstack().reset_index().to_csv("data.csv")