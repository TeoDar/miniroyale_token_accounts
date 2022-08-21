import streamlit as st
import pandas as pd
from parse import get_data, _get_sample_characters, _get_sample_weapons
 

class MiniRoyaleWebApp():
    def __init__(self) -> None:
        if 'characters' not in st.session_state:
            st.session_state.characters = pd.DataFrame(_get_sample_characters())
        if 'weapons' not in st.session_state:
            st.session_state.weapons = pd.DataFrame(_get_sample_weapons())
        # if 'download' not in st.session_state:
        #     st.session_state.download = self.right_column.download_button(label='Скачать', data='')
            
    def window(self):
        st.write('Данный сайт предназначен для получения полной сводки всех имеющихся у вас токенов в MINI ROYALE.')
        #Колонка с полем ввода
        self.account = st.text_input(label='Введите токен вашего аккаунта на Solscan:')
        #Разделение виджетов на 2 колонки
        self.left_column, self.right_column = st.columns(2)
        #Колонка с кнопками
        self.left_column.button('Выгрузить', on_click=self.get_tokens)
        
        st.write('Персонажи:')
        st.write(st.session_state.characters)
        st.write('Оружие:')
        st.write(st.session_state.weapons)
        
    def get_tokens(self):
        if self.account:
            from pandas.io.excel import ExcelWriter
            from io import BytesIO
            characters, weapons = get_data(self.account)
            st.session_state.characters = pd.DataFrame(characters)
            st.session_state.weapons = pd.DataFrame(weapons)
            output = BytesIO()
            with ExcelWriter(output) as writer:
                st.session_state.characters.to_excel(writer, index=False, sheet_name="Персонажи")
                st.session_state.weapons.to_excel(writer, index=False, sheet_name="Оружие")
            xls = output.getvalue()
            self.right_column.download_button(label='Скачать',data=xls, file_name='tokens.xlsx', mime='text/xls')

if __name__=='__main__':
    app = MiniRoyaleWebApp()
    app.window()
    
#ERoSDccar6zKd3boNboq2Y65nx4u8yRGRc5pbYcsMfSt