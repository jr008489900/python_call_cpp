import pandas as pd
import numpy as np

import subprocess
import pandas as pd
from io import StringIO

def call_cpp_sort(df):
    # 將DataFrame轉換成CSV格式的字串，避免逗號問題
    csv_data = df.to_csv(index=False, sep=' ')
    
    print(csv_data)
    # 呼叫外部C++程式
    cpp_process = subprocess.Popen(['./sort.exe'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    stdout, stderr = cpp_process.communicate(input=f"{len(df)}\n{csv_data}")
    print(stdout)
    
    # 解析排序後的結果
    sorted_csv_data = StringIO(stdout)
    sorted_df = pd.read_csv(sorted_csv_data, sep='|')
    
    return sorted_df

def GenerateData(num:int):
    # 產生隨機num筆資料
    np.random.seed(42)  # 設定隨機種子以確保結果可複製
    data = {
        'ID': range(0, num),
        'Name': [f'Person_{i}' for i in range(0, num)],
        'Age': np.random.randint(18, 65, size=num),
        'Salary': np.random.randint(30000, 100000, size=num)
    }
    # 建立DataFrame
    df = pd.DataFrame(data)
    return df

def main():
    data = GenerateData(10)
    sorted_data = call_cpp_sort(data)
    print(sorted_data)

if __name__ == '__main__':
    main()