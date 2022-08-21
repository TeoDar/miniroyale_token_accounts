import streamlit as st
import pandas as pd
from parse import get_data


class MiniRoyaleWebApp():
    def __init__(self) -> None:
        pass
    def window(self):
        st.write('Данный сайт предназначен для получения полной сводки всех имеющихся у вас токенов в MINI ROYALE.')
        #Разделение виджетов на 2 колонки
        left_column, right_column = st.columns(2)
        #Колонка с полем ввода
        self.account = left_column.text_input(label='Введите токен вашего аккаунта на Solscan:')
        #Колонка с кнопками
        with right_column:
            self.btn_get_data = st.button('Выгрузить', on_click=self.get_tokens)
            self.btn_download_data = st.button('Скачать CSV', disabled=True)

    def get_tokens(self):
        if self.account:
            st.dataframe(pd.DataFrame(get_data(self.account)))
        else:
            pass
        #self.btn_download_data.
        

if __name__=='__main__':
    app = MiniRoyaleWebApp()
    app.window()