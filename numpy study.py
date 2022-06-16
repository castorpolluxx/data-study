#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np

array1=np.arange(10)
array2=np.arange(10,20)


# In[25]:


array1


# In[26]:


array2


# In[28]:


array1*2


# In[29]:


array1+array2


# In[32]:


import numpy as np

revenue_in_yen = [
    300000, 340000, 320000, 360000, 
    440000, 140000, 180000, 340000, 
    330000, 290000, 280000, 380000, 
    170000, 140000, 230000, 390000, 
    400000, 350000, 380000, 150000, 
    110000, 240000, 380000, 380000, 
    340000, 420000, 150000, 130000, 
    360000, 320000, 250000
]

# 코드를 작성하세요.
yen_array=np.array(revenue_in_yen)
won_array=yen_array*10.08

# 정답 출력
won_array


# #흥부부대찌개 신주쿠점의 흥행에 성공한 영훈이는 여세를 몰아 LA에도 가맹점을 하나 냈습니다.
# 이제 아버지께 매출을 보고하기 위한 프로세스가 조금 복잡해졌습니다. 각 지점의 매출을 원화로 변환시키고 더해야 하죠. 1엔에 10.08원, 1달러에 1138원이라고 가정하세요. 그리고 두 지점의 매출의 합이 원화로 담긴 numpy array를 만들어 출력해주세요.
# 반복문은 사용하면 안 됩니다!

# In[33]:


import numpy as np

revenue_in_yen = [
    300000, 340000, 320000, 360000, 
    440000, 140000, 180000, 340000, 
    330000, 290000, 280000, 380000, 
    170000, 140000, 230000, 390000, 
    400000, 350000, 380000, 150000, 
    110000, 240000, 380000, 380000, 
    340000, 420000, 150000, 130000, 
    360000, 320000, 250000
]

revenue_in_dollar = [
    1200, 1600, 1400, 1300, 
    2100, 1400, 1500, 2100, 
    1500, 1500, 2300, 2100, 
    2800, 2600, 1700, 1400, 
    2100, 2300, 1600, 1800, 
    2200, 2400, 2100, 2800, 
    1900, 2100, 1800, 2200, 
    2100, 1600, 1800
]

# 코드를 작성하세요.
yen_array=np.array(revenue_in_yen)
dollar_array=np.array(revenue_in_dollar)
won_array=yen_array*10.08 + dollar_array*1138
# 정답 출력
won_array


# **#numpy boolean 연산**

# In[34]:


import numpy as np


# In[46]:


array1=np.array([2,3,5,7,11,13,17,19,23,29,31])
array1>4


# In[47]:


array1 % 2 ==0


# In[48]:


booleans=np.array([ True, True, False, False, False, True, False, False])


# In[49]:


np.where(booleans)


#  **#array boolean 같이**

# In[51]:


np.where(array1>4)  #4보다 큰 값들 위치 찾기


# In[52]:


filter=np.where(array1>4)
filter


# In[53]:


array1[filter]   #인덱싱으로 4보다 큰 값 찾기


# **#내가 푼거**

# In[61]:


import numpy as np

revenue_in_yen = [
    300000, 340000, 320000, 360000, 
    440000, 140000, 180000, 340000, 
    330000, 290000, 280000, 380000, 
    170000, 140000, 230000, 390000, 
    400000, 350000, 380000, 150000, 
    110000, 240000, 380000, 380000, 
    340000, 420000, 150000, 130000, 
    360000, 320000, 250000
]

# 코드를 작성하세요.
ch=np.array(revenue_in_yen)  #배열을 변수에 저장
bad_days_revenue=np.where(ch<200000)   #20만엔보다 작은 위치 찾아내기
# 정답 출력
ch[bad_days_revenue]   #20만엔보다 작은 위치 값으로 출력하기


# **#해설**

# In[64]:


import numpy as np

revenue_in_yen = [
    300000, 340000, 320000, 360000, 
    440000, 140000, 180000, 340000, 
    330000, 290000, 280000, 380000, 
    170000, 140000, 230000, 390000, 
    400000, 350000, 380000, 150000, 
    110000, 240000, 380000, 380000, 
    340000, 420000, 150000, 130000, 
    360000, 320000, 250000
]

ch=np.array(revenue_in_yen)   #numpy의 도움을 받기 위해 numpy array로 만들기
filter=np.array(ch<200000) #조건에 해당하는 위치 filter에 저장
bad_days_revenue=ch[filter]  #인덱싱에 활용해 조건에 해당하는 위치에 있는 값 출력

bad_days_revenue


# In[70]:


#최댓값, 최솟값

import numpy as np

array1=np.array([14,6,13,21,23,31,9,5])

print(array1.max()) #최댓값
print(array1.min()) #최솟값
print(array1.mean()) #평균값
print(np.median(array1)) #중앙값
print(array1.std()) #표준편차
print(array1.var()) #분산


# In[ ]:




