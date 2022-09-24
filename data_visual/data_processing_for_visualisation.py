import pandas as pd


class DataSetPrep():
    def __init__(self, file, sheet_name):
        self.file = pd.ExcelFile(file)
        self.sheet_name = sheet_name
    
    def run(self):
        df = self.read()
        newdf = self.drop(df)
        self.export(newdf)
        print(newdf)

    def read(self):
        df = pd.read_excel(self.file, self.sheet_name)
        return df
    
    def drop(self, df):
        newdf = df.dropna()
        newdf1 = newdf.drop(newdf.index[1:len(newdf.index)])
        newdf1 = newdf1.reset_index(drop=True)
        return newdf1
    
    def export(self, df):
        df.to_csv("DownloadingRamHackathon\data_visual\csv_outputs\{}{}".format(self.sheet_name, ".csv"))

pop_file = "DownloadingRamHackathon\data_visual\census-2021-ms-a02.xlsx"
pop_sheet_name = "MS-A02"


test = DataSetPrep(pop_file, pop_sheet_name)
test.run()