

import streamlit as st
import plotly.graph_objects as go
from PIL import Image

PAGE_CONFIG = {"page_title":"Hydra-OpenVino_Tool","page_icon":":bar_chart:","layout":"centered"}
st.beta_set_page_config(**PAGE_CONFIG)


  

def main():
    st.title("Hydra: OpenVino & AI based Remote plant monitoring & Feeding")
    st.subheader("Hydra is an Intel OpenVino based Apple Vegetation Monitoring and Watering system with Visual and Geospatial Analysis based on AIoT Technology")
if __name__ == '__main__':
    main()


fig = go.Figure(data=[go.Scatter(
        x=[2, 2, 2, 2, 2, 2, 2, 2, 2 ,2 ,2 ,2 ,2 ,2,
           4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
           6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
           8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
           10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
           12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
        y=[100, 250, 345, 450, 560, 680, 790, 910, 1050, 1250, 1380, 1490, 1670, 1789,
           100, 250, 345, 450, 560, 680, 790, 910, 1050, 1250, 1380, 1490, 1670, 1789,
           100, 250, 345, 450, 560, 680, 790, 910, 1050, 1250, 1380, 1490, 1670, 1789,
           100, 250, 345, 450, 560, 680, 790, 910, 1050, 1250, 1380, 1490, 1670, 1789,
           100, 250, 345, 450, 560, 680, 790, 910, 1050, 1250, 1380, 1490, 1670, 1789,
           100, 250, 345, 450, 560, 680, 790, 910, 1050, 1250, 1380, 1490, 1670, 1789,],
        mode='markers',
        marker=dict(
            color=[80, 80, 80, 80, 90, 80, 80 , 90, 85, 90, 95, 80, 70, 75,
                   80, 80, 80, 80, 85, 90, 95, 80, 70, 75, 90, 80, 80 , 90, 
                   70, 75, 80, 90, 70, 75, 80 , 95, 90, 95, 85, 80, 75, 80,
                   80, 90, 80, 80, 90, 80, 80, 80, 85, 90, 95, 80, 70, 75,
                   80, 80, 70, 75, 80, 80, 80, 90, 80, 80 , 90, 85, 90, 95, 
                   90, 95, 80, 70, 75, 80, 80, 80, 80, 90, 80, 80 , 90, 85],
            size=[25, 25, 25, 25, 30, 25, 25, 30, 28, 30, 35, 25, 20, 23,
                  25, 25, 25, 25, 30, 28, 30, 35, 25, 20, 23, 30, 25, 25, 
                  20, 23, 25, 30, 20, 23, 25, 35, 30, 35, 28, 25, 23, 25,
                  25, 30, 25, 25, 25, 25, 25, 30, 28, 30, 35, 25, 20, 23,
                  25, 25, 20, 23, 25, 25, 25, 30, 25, 25, 30, 28, 30, 35, 
                  30, 35, 25, 20, 23, 25, 25, 25, 25, 30, 25, 25, 30, 28],
            showscale=True
            )
    )])

# 70 - 20, 
 # 75 - 23, 
  #80 - 25, 
  #85 - 28, 
  #90 - 30,
  #95 - 35

fig2 = go.Figure(
    data=[go.Bar(y=[8.45, 7.98, 8.23, 8.98, 9.12, 10.32, 12.43, 13.57, 14.76, 14.57, 13.98, 12.23,
                    11.98, 11.54, 11.32, 10.98, 9.97, 9.65, 9.21, 8.87, 8.43, 8.12, 7.98, 7.87])],
    layout_title_text="Average Temperature of all the Arrays starting from 6am ending at 6am the next day"
)

fig3 = go.Figure(
    data=[go.Bar(y=[75.32, 76.76, 76.45, 76.86, 77.93, 78.24, 78.98, 79.68, 80.54, 80.98, 82.43, 83.65,
                    82.98, 82.43, 81.73, 81.52, 80.93, 80.21, 79.34, 78.34, 77.98, 76.43, 76.21, 75.90])],
    layout_title_text="Average Humididty of all the Arrays starting from 6am ending at 6am the next day"
)


menu = ["Home","Average-Temp","Average-Humidity","Average-Moisture","Geospatial-analysis"]

choice = st.sidebar.selectbox('Menu',menu)
img = Image.open("https://github.com/dhruvsheth-ai/heroku/blob/master/Screenshot_20200912-125546.png")

img2 = Image.open("https://github.com/dhruvsheth-ai/heroku/blob/master/image_fUhRbpUPET.jpeg")

img3 = Image.open("https://github.com/dhruvsheth-ai/heroku/blob/master/image_0NJXH36TJm.jpeg")

st.sidebar.subheader("Farm plot")



st.sidebar.image(img3, height=250, width=250)
st.sidebar.image(img, height=250, width=250)
st.sidebar.image(img2, height=250, width=250)
if choice == 'Average-Temp':
    
  st.plotly_chart(fig2)
  st.write("................................6am yesterday............................................6am today...................................")
if choice == 'Average-Moisture':
  st.subheader("This shows the visualisation of the Apple farm starting from Array1 and ending at Array6")
        
  st.plotly_chart(fig)
if choice == 'Average-Humidity':
  st.plotly_chart(fig3)
if choice == 'Geospatial-analysis':
  st.image(img3, height=1000, width=1000)
if choice == "Home":
  if st.checkbox("Show Notifications for Diseases"):
    st.success("No diseases detected for any plant in array1")
    st.error("Fire Blight detected in array2")
    st.error("Cedar Rust detected in array3")
    st.success("Apple Tree flowering in Array1")
    st.success("Ripe Apples detected in Array4")
    st.warning("Raw Apples detected in Array5")
  if st.checkbox("Show Notifications for Temperature"):
    st.subheader("Normal Temperature = 8C")
    st.subheader("Above Average Threshold = 15C")
    st.subheader("Critically High Temperature = 20C")
    st.success("Temperature levels Normal in Array1")
    st.warning("Temperature levels above Average threshold in Array2")
    st.error("Temperature levels critically high in Array3")
    st.success("Temperature levels Normal in Array4")
    st.success("Temperature levels Normal in Array5")
    st.warning("Temeparture levels above Average threshold in Array6")
  if st.checkbox("Show notifications for Atmosphere Humidity"):
    st.subheader("Normal Humidity = 75%")
    st.subheader("Above Average Threshold = 80%")
    st.subheader("Critically High Humidity = 85%")
    st.success("Humidity levels Normal in Array1")
    st.success("Humidity levels Normal in Array2")
    st.error("Humidity levels critically high in Array3")
    st.success("Humidity levels Normal in Array4")
    st.success("Humidity levels Normal in Array5")
    st.warning("Humidity levels Above Average Threshold in Array6")
  if st.checkbox("Show notifications for Soil Moisture"):
    st.subheader("Normal Soil Moisture = 70%")
    st.subheader("Above Average Threshold = 74%")
    st.subheader("Critically High Soil Moisture = 85%")
    st.success("Soil Moisture levels Normal in Array1")
    st.success("Soil Moisture levels Normal in Array2")
    st.error("Soil Moisture levels critically high in Array3")
    st.success("Soil Moisture levels Normal in Array4")
    st.success("Soil Moisture levels Normal in Array5")
    st.warning("Soil Moisture levels Above Average Threshold in Array6")
  
