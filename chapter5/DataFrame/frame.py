import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# 字典
data = {
    'state': ['Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada', 'Nevada'],
    'year': [2000, 2001, 2002, 2001, 2002, 2003],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
}

# 用字典构建DataFrame
frame = pd.DataFrame(data)
# print(frame)

# head() 选出头部的五行
# print(frame.head())

# 制定列的顺序
# print(pd.DataFrame(data, columns=['year', 'state', 'pop']))

# 传的列不包含在字典中，则结果中会有缺失值 NaN:
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                      index=['one', 'two', 'three', 'four', 'five', 'six'])
# print(frame2)
# print(frame2.columns)

# DataFrame 中的一列，可以按字典型标记或属性那样，检索为 Series
# print(frame2['state'])
# print(frame2.year)
# frame2[column] 对于任意列名均有效，但是 frame2.column 只在列名是有效的 Python 变量名 时有效

# 行也可以通过位置或特殊属性loc进行选取（后面会详细说明）
# print(frame2.loc['three'])

# 列的引用是可以修改的
frame2['debt'] = 16.5
# print(frame2)
frame2['debt'] = np.arange(6.)
# print(frame2)

# 将 Series 赋值给一列，Series 的索引会按照DataFrame的索引重新排列，并在空缺的地方填充空缺值
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
print(frame2)

frame2['debt'] = val
print(frame2)

frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)

# frame2.eastern 无法创建新的列。

# del 可以移除列

del frame2['eastern']
print(frame2.columns)

print()