import pandas as pd
from datetime import datetime

class CarAccident:
    def __init__(self, year, rank, month=None):
        self.year = year
        self.month = month
<<<<<<< HEAD
        self.rank = rank
        self.datas = pd.DataFrame()  # 初始化空的 DataFrame

        if rank == "A1":
            self.datas = pd.read_csv(f"./data/accidents/{year}/{year}年度A1交通事故資料.csv")
            self.datas = self.datas[:-2]  # 假設最後兩行是多餘的，去除
            if month:
                # 轉換日期格式並篩選出特定月份的數據
                self.datas['發生日期'] = self.datas['發生日期'].astype(int)
                if month > 9:
                    self.datas = self.datas[self.datas['發生日期'].astype(str).str[4:6] == str(month)]
                else:
                    self.datas = self.datas[self.datas['發生日期'].astype(str).str[4:6] == f"0{month}"]
                self.datas['發生日期'] = self.datas['發生日期'].astype(float)
                self.datas = self.datas.reset_index(drop=True)
        elif rank == "A2":
            if month is None:
                # 迭代1到12月份，將每個月的數據讀入並合併到 self.datas 中
                for m in range(1, 13):
                    monthly_data = pd.read_csv(f"./data/accidents/{year}/{year}年度A2交通事故資料_{m}.csv")
                    monthly_data = monthly_data[:-2]
                    self.datas = pd.concat([self.datas, monthly_data], ignore_index=True)
            else:
                self.datas = pd.read_csv(f"./data/accidents/{year}/{year}年度A2交通事故資料_{month}.csv")
                self.datas = self.datas[:-2]

=======
        if month:
            self.data = GetMonthData(self.year, self.month)
        else:
            self.data = []
            for i in range(1, 13):
                self.data.append(GetMonthData(self.year, i))

class GetMonthData():
    def __init__(self, year, month):
        pass
    
        if:
            self.datas = pd.read_csv(f".\\data\\accidents\\{year}\\{year}年度A2交通事故資料_{month}.csv")
        else:
            self.datas = pd.read_csv(f".\\data\\accidents\\{year}\\{year}年度A1交通事故資料.csv")
>>>>>>> origin/database
        
        self.dates = [datetime.strptime(str(int(d)), '%Y%m%d').strftime('%Y-%m-%d') for d in self.datas['發生日期']]
        self.times = [datetime.strptime(str(int(t)).zfill(6), '%H%M%S').strftime('%H:%M:%S') for t in self.datas['發生時間']]
        self.longitudes = self.datas['經度']
        self.latitudes = self.datas['緯度']
        self.casualties = self.datas['死亡受傷人數']
        self.fatalities = [int(c[2]) for c in self.casualties]
        self.injuries = [int(c[-1]) for c in self.casualties]
        self.location = self.datas['發生地點']
        self.administrative_area_level_1 = [loc[:3] for loc in self.location]
        self.administrative_area_level_2 = [loc[3:6] for loc in self.location]

        check = 0
        longitude_check = 0
        latitude_check = 0
        self.data = []
        for i in range(len(self.dates)):
            if self.times[i] == check:
                if (self.longitudes[i] == longitude_check) and (self.latitudes[i] == latitude_check):
                    continue
                else:
                    longitude_check = self.longitudes[i]
                    latitude_check = self.latitudes[i]
            else:
                check = self.times[i]
                self.data.append([
                    self.dates[i],
                    self.times[i],
                    self.latitudes[i],
                    self.longitudes[i],
                    self.fatalities[i],
                    self.injuries[i],
                    self.administrative_area_level_1[i],
                    self.administrative_area_level_2[i]
                ])

        self.newdata = pd.DataFrame(self.data, columns=[
            'date',
            'time',
            'latitude',
            'longitude',
            'fatality',
            'injury',
            'administrative_area_level_1',
            'administrative_area_level_2'
        ])

        self.dates = self.newdata.iloc[:, 0]
        self.times = self.newdata.iloc[:, 1]
        self.latitudes = self.newdata.iloc[:, 2]
        self.longitudes = self.newdata.iloc[:, 3]
        self.fatalities = self.newdata.iloc[:, 4]
        self.injuries = self.newdata.iloc[:, 5]
        self.administrative_area_level_1s = self.newdata.iloc[:, 6]
        self.administrative_area_level_2s = self.newdata.iloc[:, 7]

    def get_date(self, id=None):
        if id:
            return self.dates[id - 1]
        else:
            return self.dates

    def get_time(self, id):
        if id:
            return self.times[id - 1]
        else:
            return self.times

    def get_latitude(self, id=None):
        if id:
            return self.latitudes[id - 1]
        else:
            return self.latitudes
        

    def get_longitude(self, id):
        if id:
            return self.longitudes[id - 1]
        else:
            return self.longitudes

    def get_fatality(self, id):
        if id:
            return self.fatalities[id - 1]
        else:
            return self.fatalities

    def get_injury(self, id):
        if id:
            return self.injuries[id - 1]
        else:
            return self.injuries

    def get_administrative_area_level_1(self, id):
        if id:
            return self.administrative_area_level_1s[id - 1]
        else:
            return self.administrative_area_level_1s

    def get_administrative_area_level_2(self, id):
        if id:
            return self.administrative_area_level_2s[id - 1]
        else:
            return self.administrative_area_level_2s

if __name__ == "__main__":
    accident = CarAccident(year=111,month=3, rank="A1")
    
    # print(accident.get_date(10))
    # print(accident.get_time(10))
    # print(accident.get_latitude(10))
    # print(accident.get_longitude(10))
    # print(accident.get_fatality(10))
    # print(accident.get_injury(10))
    # print(accident.get_administrative_area_level_1(10))
    # print(accident.get_administrative_area_level_2(10))
