import streamlit as st

st.title(":violet[PROJECT LPK 2025]")
st.header(":blue[Penentuan Bilangan Ganjil dan Genap]")

number = st.number_input("Masukkan angka", min_value=0, max_value=100000)
if number%2==1:
  st.write("Bilangan",number,"termasuk bilangan ganjil")
else:
  st.write("Bilangan",number,"termasuk bilangan genap")
