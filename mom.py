import streamlit as st
import math as m

st.markdown('<h1>Trasformer calculator</h1>',unsafe_allow_html=True)
#st.radio('parameters of the transformer',['oc voltage','oc current','oc power','sc voltage','sc current','sc power'])
oc_voltage=st.number_input('Enter the oc voltage:')
oc_current=st.number_input('Enter the oc current:')
if oc_voltage and oc_current != 0:
    oc_power=st.number_input('Enter the oc power:')
    cosphi = oc_power/(oc_voltage*oc_current)
    #st.write('cosphi is', cosphi)
    sinphi=m.sqrt(1-cosphi**2)
    #st.write('sinphi is',sinphi)
    Iw = oc_current*sinphi
    #st.write('Iw', Iw)
    Iu = oc_current*cosphi
    #st.write('Iu', Iu)
    Im = m.sqrt(Iw**2-Iu**2)
    #st.write('Im',Im)
    R0 = oc_voltage/Iw
    if Iu != 0:
        X0 = oc_voltage/Iu
    #st.write('X0',X0)
     #st.write('R0',R0)
sc_voltage = st.number_input('Enter the value of sc voltage:')
sc_current = st.number_input('Enter the value of sc current:')
X = st.number_input('Enter the load factor:')
rating = st.number_input('Enter the rating:')
if sc_voltage and sc_current != 0:
    sc_power = st.number_input('Enter the value of sc power:')
    Z = sc_voltage/sc_current
    #st.write('Z',Z)
    Rsc = sc_power/(sc_current**2)
    #st.write('Rsc',Rsc)
    Xsc = m.sqrt(Z**2-Rsc**2)
    #st.write('Xsc',Xsc)
    copper_losses = sc_power*(X**2)
    total_losses = copper_losses + sc_power
    
#Efficiency
if X != 0:
    output = rating*(X**2)
    input = total_losses + output
    eff = (output/input)*100
    st.write('Efficiency of the transformer is :',eff)
    
       
    
