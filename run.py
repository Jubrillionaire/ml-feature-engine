import pandas as pd 



def load_data(filename='sales_data.csv'):
    print("loaded data...")
    try:
        df = pd.read_csv(filename)
        print(f"successfully loaded {len(df)} data!")
    except FileNotFoundError:
        print("Sales data not found")
        return pd.DataFrame(columns=['Day', 'Customers', 'Total_Sales', 'Top_Selling_Item'])




def main():
    print("running app....")
    data = load_data()


main()