import pandas as pd


# this function returns a pandas car cluster dataframe
def csv_to_car_cluster(csv_file):
    car_cluster = pd.read_csv(csv_file)

    return  car_cluster[['sourcing_country','manufacturer','fuel_type']]