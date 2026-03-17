#USD to NRS
#Conversion app
import streamlit as st
Amount = input("What amount do you want to convert (in USD)?")
TotalConversion = float(Amount)*144
print("The total amount in NRS is " + str(TotalConversion))