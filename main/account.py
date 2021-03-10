import pandas as pd
import numpy as np
import secrets
import asyncio
import datetime
from jinja2 import Template


class Users():
    def __init__(self):
        pass
                
    def update(self, path):
        self.df = pd.read_excel(path)
        self.df['логин'] = self.df[self.df.columns[[0, 1, 2]]].apply(lambda x: ''.join([i.replace(' ', '') for i in x]), axis=1)
        self.df['пароль ученика'] = self.df['пароль ученика'].apply(lambda x: secrets.token_urlsafe(8))
        self.df['пароль родителя'] = self.df['пароль родителя'].apply(lambda x: secrets.token_urlsafe(8))
        self.df['marks'] = pd.DataFrame
        self.last_day = None
    
#     def add_day(self):
#         if  datetime.date != self.last_day:
#             d = {datetime.date: 'был на уроке'}
#             self.df['marks'].apply(lambda x: x.append(pd.DataFrame(d), inde))
#             self.last_day = datetime.date
    def all_info(self, user):
        return self.df.loc[self.df['логин'] == user]

    def get_marks(self, user):
        return self.df.loc[self.df['логин'] == user]['marks']
        
    def add_lesson(self, school, lesson):
        for i in self.df[self.df['школа'] == school]['marks']:
            print(len(i.columns))


# In[5]:


a = Users()
#  a.update('C:\\Users\\Tolmaks\PycharmProjects\\alterdaiaryProject\\alterdairy\\main\\static\\main\\csv\\~$аккаунты.xlsx')


# In[32]:









