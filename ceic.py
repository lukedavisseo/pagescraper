import requests
from bs4 import BeautifulSoup
import streamlit as st

st.header('CEIC Indicator Doc Creator')

url = st.text_input('Enter URL')

submit = st.button('Submit')

if submit:

	page = requests.get(url)

	soup = BeautifulSoup(page.content, "html.parser", from_encoding="iso-8859-1")

	h1 = soup.h1.text
	p = soup.find('p', class_="mxw-88 mt-38").text.replace("â","'").replace("â","-").partition('\n')[0]
	p_line = soup.find('p', class_="mxw-88 mt-38").text.replace("â","'").replace("â","-").partition('. ')[0]
	p_bullets = soup.find('p', class_="mxw-88 mt-38").text.replace("â","'").replace("â","-").partition('\n')[0].replace(". ", "\n* ")
	p_bullets_latest = soup.find('p', class_="mxw-88 mt-38").text.replace("â","'").replace("â","-").partition('\n')[0].replace(". ", "\n* ").replace('.In the latest reports','.\n\n* In the latest reports')
	p_bullets2 = '* ' + p_bullets
	p_bullets3 = '* ' + p_bullets_latest
	h4 = soup.find_all('h4')[1].text.replace('\n','')

	st.write(f'# {h1} Indicator Page Recommendations')
	st.write(f'## {h1}')
	st.write(url)
	st.write(f'### HEADING')
	st.write(f'**H1:** {h1}')
	st.write(f'### BODY CONTENT')
	if 'In the latest reports' in p:
		p_latest = p.replace('.In the latest reports','.\n\nIn the latest reports')
		st.write(f'**Current:** {p_latest}')
		st.write(f'H2: {h4}')
		st.write('[DATA TABLE]')
		st.write(f'### RECOMMENDED')
		st.write(f'H2: Key information about {h1}')
		st.write(f'{p_bullets2}')
		st.write(f'H2: Further information about {h1}')
		st.write(f'{p_bullets3}')
		st.write(f'H2: {h4}')
		st.write(f'{p_line}. See the table below for more data.')
		st.write('[DATA TABLE]')
	else:
		st.write(f'**Current:** {p}')
		st.write(f'H2: {h4}')
		st.write('[DATA TABLE]')
		st.write(f'### RECOMMENDED')
		st.write(f'H2: Key information about {h1}')
		st.write(f'{p_bullets2}')
		st.write(f'H2: {h4}')
		st.write(f'{p_line}. See the table below for more data.')
		st.write('[DATA TABLE]')