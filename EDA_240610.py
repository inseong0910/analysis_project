#!/usr/bin/env python
# coding: utf-8

# ### 1. 파일 불러오기

# In[3]:


import pandas as pd


# In[4]:


df = pd.read_csv('./1. data/agency_performance_model.csv')

df


# ### 2. 컬럼 살펴보기

# #### 2-1. AGENCY_ID

# In[5]:


# 2-1. agency_id
# 3~9998


# In[6]:


df['AGENCY_ID'].value_counts()


# #### 2-2. PRIMARY_AGENCY_ID

# In[7]:


# 2-2. PRIMARY_AGENCY_ID
# 정수로 되어 있고, 99999는 값이 아닌듯
# 주요 에이전시 ID


# In[8]:


df['PRIMARY_AGENCY_ID'].value_counts()


# In[9]:


df['PRIMARY_AGENCY_ID'].count


# In[10]:


# 약 21.3만개의 데이터 가운데 특이한 값 99999가 37,874개나 있다.


# #### 2-3. PROD_ABBR

# In[11]:


# 컬럼명 해석하지 못함
# ABBR의 절차(procedure)


# In[12]:


df['PROD_ABBR'].value_counts()


# #### 2-4. PROD_LINE

# In[13]:


df['PROD_LINE'].value_counts()


# In[14]:


# CL : 상업보험
# PL : 생명보험


# #### 2-5. STATE_ABBR

# In[15]:


# STATE_ABBR : state 약자?


# In[16]:


df['STATE_ABBR'].value_counts()


# In[17]:


# 지역별, PL/CL별 가입자 수 파악 가능


# #### 2-6. STAT_PROFILE_DATE_YEAR

# In[18]:


df['STAT_PROFILE_DATE_YEAR'].value_counts()


# #### 2-7. RETENTION_POLY_QTY

# In[19]:


df['RETENTION_POLY_QTY'].value_counts()


# In[20]:


# RETENTION_POLY_QTY : 유효정책 또는 계약건수


# #### 2-8. POLY_INFORCE_QTY

# In[21]:


# POLY_INFORCE_QTY : 유효 계약건수


# In[22]:


df['POLY_INFORCE_QTY'].value_counts()


# In[23]:


df['POLY_INFORCE_QTY'].info()


# #### 2-9. PREV_POLY_INFORCE_QTY

# In[24]:


# PREV_POLY_INFORCE_QTY : 과거 유효 계약건수


# In[25]:


df['PREV_POLY_INFORCE_QTY'].value_counts()


# #### 2-10. NB_WRTN_PREM_AMT

# In[26]:


# NB_WRTN_PREM_AMT : 새 계약건의 보험료


# In[27]:


df['NB_WRTN_PREM_AMT'].value_counts()


# #### 2-11. WRTN_PREM_AMT

# In[28]:


# WRTN_PREM_AMT : 현재까지 납입한 보험료


# In[29]:


df['WRTN_PREM_AMT'].value_counts()


# In[30]:


df['WRTN_PREM_AMT'].describe()


# In[31]:


df['WRTN_PREM_AMT']


# In[32]:


# 매우 다양한 숫자들이 값으로 되어 있음


# #### 2-12. PREV_WRTN_PREM_AMT

# In[33]:


# PREV_WRTN_PREM_AMT : 과거 납입한 보험료


# In[34]:


df['PREV_WRTN_PREM_AMT'].value_counts()


# In[35]:


df.corr()


# In[36]:


# 현재-과거 납입 보험료간 상관관계
df[['WRTN_PREM_AMT','PREV_WRTN_PREM_AMT']].corr()


# In[37]:


# 현재-과거 납입 보험료간 상관관계 계수가 0.922929로 나와서 높은 상관관계가 있음을 확인하였다.


# #### 2-13. PRD_ERND_PREM_AMT

# In[38]:


# PRD_ERND_PREM_AMT : 납입한 보험료


# In[39]:


df['PRD_ERND_PREM_AMT'].value_counts()


# In[40]:


df['PRD_ERND_PREM_AMT'].plot(kind='hist')


# #### 2-14. PRD_INCRD_LOSSES_AMT

# In[41]:


# PRD_INCRD_LOSSES_AMT : 보상금 지불 총액


# In[42]:


df['PRD_INCRD_LOSSES_AMT'].value_counts()


# In[43]:


df['PRD_INCRD_LOSSES_AMT'].plot(kind='hist')


# #### 2-15. MONTHS

# In[44]:


df['MONTHS'].value_counts()


# #### 2-16. RETENTION_RATIO

# In[45]:


# RETENTION_RATIO : 고객 유지 비율


# In[46]:


df['RETENTION_RATIO'].info()


# In[47]:


df['RETENTION_RATIO'].describe()


# In[48]:


df['RETENTION_RATIO'].value_counts()


# In[49]:


df['RETENTION_RATIO'].plot(kind='hist')


# #### 2-17. LOSS_RATIO

# In[50]:


df['LOSS_RATIO'].describe()


# In[51]:


df['LOSS_RATIO'].value_counts()


# #### 2-18. LOSS_RATIO_3YR

# In[52]:


df['LOSS_RATIO_3YR'].describe()


# In[53]:


df['LOSS_RATIO_3YR'].value_counts()


# #### 2-19. GROWTH_RATE_3YR

# In[54]:


# GROWTH_RATE_3YR : 3년간 성장률


# In[55]:


df['GROWTH_RATE_3YR'].describe()


# In[56]:


df['GROWTH_RATE_3YR'].value_counts()


# #### 2-20. AGENCY_APPOINTMENT_YEAR

# In[57]:


# AGENCY_APPOINTMENT_YEAR : 에이전시 약속 연도? 시작 연도?


# In[58]:


df['AGENCY_APPOINTMENT_YEAR'].value_counts()


# In[59]:


df['AGENCY_APPOINTMENT_YEAR'].plot(kind='hist')


# #### 2-21. ACTIVE_PRODUCERS

# In[60]:


# ACTIVE_PRODUCERS : 활동중인 FC
# FC : Financial Consultant


# In[61]:


df['ACTIVE_PRODUCERS'].value_counts()


# #### 2-22. MAX_AGE

# In[62]:


df['MAX_AGE'].value_counts()


# In[63]:


df['MAX_AGE'].describe()


# #### 2-23. MIN_AGE

# In[65]:


df['MIN_AGE'].value_counts()


# In[66]:


# 고객 1명에 대해 MAX_AGE, MIN_AGE가 있는 것으로 봐서는, 두 컬럼의 차이를 계산?


# #### 2-24. VENDOR_IND

# In[67]:


# VENDOR_IND : 매도인 IND


# In[68]:


df['VENDOR_IND'].value_counts()


# In[69]:


# 매도를 했는가? Yes 131926, No 81402 ???


# #### 2-25. VENDOR

# In[70]:


df['VENDOR'].value_counts()


# In[71]:


# 대리점 구분 A~F


# #### 2-26. PL_START_YEAR

# In[72]:


# PL_START_YEAR : 생명보험 시작 연도


# In[73]:


df['PL_START_YEAR'].value_counts()


# #### 2-27. PL_END_YEAR

# In[74]:


df['PL_END_YEAR'].value_counts()


# In[75]:


# 고객별 시작연도와 종료연도가 함께 주어진 것으로 봐서
# 고객별 가입기간(종료연도 - 시작연도)을 별도의 컬럼으로 계산할 수 있음


# #### 2-28. COMMISIONS_START_YEAR

# In[76]:


# COMMISIONS_START_YEAR : 수수료 시작 연도


# In[77]:


df['COMMISIONS_START_YEAR'].value_counts()


# #### 2-29. COMMISIONS_END_YEAR

# In[78]:


# COMMISIONS_END_YEAR : 수수료 종료 연도


# In[79]:


df['COMMISIONS_END_YEAR'].value_counts()


# In[80]:


# 고객별 (수수료 종료연도 - 시작연도) 계산?


# #### 2-30. CL_START_YEAR

# In[81]:


# CL_START_YEAR : 상업보험 시작 연도


# In[82]:


df['CL_START_YEAR'].value_counts()


# #### 2-31. CL_END_YEAR

# In[83]:


# CL_END_YEAR : 상업보험 종료 연도


# In[84]:


df['CL_END_YEAR'].value_counts()


# In[85]:


# 99999 전처리 필요


# #### 2-32. ACTIVITY_NOTES_START_YEAR

# In[86]:


# ACTIVITY_NOTES_START_YEAR : 활동 기록 시작 연도?


# In[87]:


df['ACTIVITY_NOTES_START_YEAR'].value_counts()


# #### 2-33. ACTIVITY_NOTES_END_YEAR

# In[88]:


# ACTIVITY_NOTES_END_YEAR : 활동 기록 종료 연도?


# In[89]:


df['ACTIVITY_NOTES_END_YEAR'].value_counts()


# In[90]:


# 고객별 종료연도 - 시작연도 계산?


# #### 2-34. CL_BOUND_CT_MDS

# In[91]:


# CL_BOUND_CT_MDS : 상업보험 계약수


# In[92]:


df['CL_BOUND_CT_MDS'].value_counts()


# #### 2-35. CL_QUO_CT_MDS

# In[93]:


# CL_QUO_CT_MDS : 상업보험 견적수


# In[94]:


df['CL_QUO_CT_MDS'].value_counts()


# #### 2-36. CL_BOUND_CT_SBZ

# In[95]:


# CL_BOUND_CT_SBZ : SBZ의 상업보험 계약수


# In[96]:


df['CL_BOUND_CT_SBZ'].value_counts()


# #### 2-37. CL_QUO_CT_SBZ

# In[97]:


# CL_QUO_CT_SBZ : SBZ의 상업보험 견적수


# In[98]:


df['CL_QUO_CT_SBZ'].value_counts()


# #### 2-38. CL_BOUND_CT_eQT

# In[99]:


# CL_BOUND_CT_eQT : 상업보험 전자계약수


# In[100]:


df['CL_BOUND_CT_eQT'].value_counts()


# #### 2-39. CL_QUO_CT_eQT

# In[101]:


# CL_QUO_CT_eQT : 상업보험 전자견적수 


# In[102]:


df['CL_QUO_CT_eQT'].value_counts()


# #### 2-40. PL_BOUND_CT_ELINKS

# In[103]:


# PL_BOUND_CT_ELINKS : E 생명보험 계약수


# In[104]:


df['PL_BOUND_CT_ELINKS'].value_counts()


# #### 2-41. PL_QUO_CT_ELINKS

# In[105]:


# PL_QUO_CT_ELINKS : E 생명보험 견적수


# In[106]:


df['PL_QUO_CT_ELINKS'].value_counts()


# #### 2-42. PL_BOUND_CT_PLRANK

# In[107]:


# PL_BOUND_CT_PLRANK : P 생명보험 계약수


# In[108]:


df['PL_BOUND_CT_PLRANK'].value_counts()


# #### 2-43. PL_QUO_CT_PLRANK

# In[109]:


# PL_QUO_CT_PLRANK : P 생명보험 견적수


# In[110]:


df['PL_QUO_CT_PLRANK'].value_counts()


# #### 2-44. PL_BOUND_CT_eQTte

# In[111]:


# PL_BOUND_CT_eQTte : 생명보험 전자계약수


# In[112]:


df['PL_BOUND_CT_eQTte'].value_counts()


# #### 2-45. PL_QUO_CT_eQTte

# In[113]:


# PL_QUO_CT_eQTte : 생명보험 전자견적수


# In[114]:


df['PL_QUO_CT_eQTte'].value_counts()


# #### 2-46. PL_BOUND_CT_APPLIED

# In[115]:


# PL_BOUND_CT_APPLIED : 승인된 생명보험 건수


# In[116]:


df['PL_BOUND_CT_APPLIED'].value_counts()


# #### 2-47. PL_QUO_CT_APPLIED

# In[117]:


# PL_QUO_CT_APPLIED : 승인된 생명보험 견적수


# In[118]:


df['PL_QUO_CT_APPLIED'].value_counts()


# #### 2-48. PL_BOUND_CT_TRANSACTNOW

# In[119]:


# PL_BOUND_CT_TRANSACTNO : 현재 진행중인 생명보험 계약수


# In[120]:


df['PL_BOUND_CT_TRANSACTNOW'].value_counts()


# #### 2-49. PL_QUO_CT_TRANSACTNOW

# In[121]:


# PL_QUO_CT_TRANSACTNOW : 현재 진행중인 생명보험 견적수


# In[122]:


df['PL_QUO_CT_TRANSACTNOW'].value_counts()


# In[ ]:




