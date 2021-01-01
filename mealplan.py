import streamlit as st
import pandas as pd
from datetime import date, datetime
from PIL import Image
from pathlib import Path
import base64
today = date.today()

# st.write('Upload file')
# uploaded_file = st.file_uploader("Choose a file")
uploaded_file = 'data.csv'
st.title('Meal planner')
cols_used = [0,1,2]

# ## Instructions
# expander = st.sidebar.beta_expander('Instructions')
# expander.write("Test")

# # setup sidebar
week = st.date_input('Plan for week starting')

# Patient Selector
if uploaded_file is not None:
    # load data
    data = pd.read_csv(uploaded_file, usecols=cols_used, names=['Dish','Ingredients','URL'], skiprows=1)
    # data = pd.read_csv(uploaded_file, usecols=cols_used, names=['Ingredients','URL'], skiprows=1, index_col=0)
    
else:
    st.write('Upload data file to continue - export from redcap as CSV and tick "remove all tagged identifier fields"')


with st.beta_expander('Plan meals'):
    st.markdown('## Meals')
    # Monday
    # st.markdown('## Monday')
    col1, col2, col3 = st.beta_columns(3)
    mob = col1.selectbox(
        'Monday breakfast:',
        data['Dish'].unique()
    )
    mol = col2.selectbox(
        'Monday lunch:',
        data['Dish'].unique()
    )
    mod = col3.selectbox(
        'Monday dinner:',
        data['Dish'].unique()
    )
    mobdata = data[data['Dish'] == mob]
    mobdata['Ingredients'] = mobdata.Ingredients.apply(lambda x: x.split(','))
    mobing = list(mobdata['Ingredients'])[0]
    moburl = mobdata['URL']
    moldata = data[data['Dish'] == mol]
    moldata['Ingredients'] = moldata.Ingredients.apply(lambda x: x.split(','))
    moling = list(moldata['Ingredients'])[0]
    molurl = moldata['URL']
    moddata = data[data['Dish'] == mod]
    moddata['Ingredients'] = moddata.Ingredients.apply(lambda x: x.split(','))
    moding = list(moddata['Ingredients'])[0]
    modurl = moddata['URL']
    # Tuesday
    # st.markdown('## Tuesday')
    col1, col2, col3 = st.beta_columns(3)
    tub = col1.selectbox(
        'Tuesday breakfast:',
        data['Dish'].unique()
    )
    tul = col2.selectbox(
        'Tuesday lunch:',
        data['Dish'].unique()
    )
    tud = col3.selectbox(
        'Tuesday dinner:',
        data['Dish'].unique()
    )
    tubdata = data[data['Dish'] == tub]
    tubdata['Ingredients'] = tubdata.Ingredients.apply(lambda x: x.split(','))
    tubing = list(tubdata['Ingredients'])[0]
    tuburl = tubdata['URL']
    tuldata = data[data['Dish'] == tul]
    tuldata['Ingredients'] = tuldata.Ingredients.apply(lambda x: x.split(','))
    tuling = list(tuldata['Ingredients'])[0]
    tulurl = tuldata['URL']
    tuddata = data[data['Dish'] == tud]
    tuddata['Ingredients'] = tuddata.Ingredients.apply(lambda x: x.split(','))
    tuding = list(tuddata['Ingredients'])[0]
    tudurl = tuddata['URL']
    # Wednesday
    # st.markdown('## Wednesday')
    col1, col2, col3 = st.beta_columns(3)
    web = col1.selectbox(
        'Wednesday breakfast:',
        data['Dish'].unique()
    )
    wel = col2.selectbox(
        'Wednesday lunch:',
        data['Dish'].unique()
    )
    wed = col3.selectbox(
        'Wednesday dinner:',
        data['Dish'].unique()
    )
    webdata = data[data['Dish'] == web]
    webdata['Ingredients'] = webdata.Ingredients.apply(lambda x: x.split(','))
    webing = list(webdata['Ingredients'])[0]
    weburl = webdata['URL']
    weldata = data[data['Dish'] == wel]
    weldata['Ingredients'] = weldata.Ingredients.apply(lambda x: x.split(','))
    weling = list(weldata['Ingredients'])[0]
    welurl = weldata['URL']
    weddata = data[data['Dish'] == wed]
    weddata['Ingredients'] = weddata.Ingredients.apply(lambda x: x.split(','))
    weding = list(weddata['Ingredients'])[0]
    wedurl = weddata['URL']
    # Thursday
    # st.markdown('## Thursday')
    col1, col2, col3 = st.beta_columns(3)
    thb = col1.selectbox(
        'Thursday breakfast:',
        data['Dish'].unique()
    )
    thl = col2.selectbox(
        'Thursday lunch:',
        data['Dish'].unique()
    )
    thd = col3.selectbox(
        'Thursday dinner:',
        data['Dish'].unique()
    )
    thbdata = data[data['Dish'] == thb]
    thbdata['Ingredients'] = thbdata.Ingredients.apply(lambda x: x.split(','))
    thbing = list(thbdata['Ingredients'])[0]
    thburl = thbdata['URL']
    thldata = data[data['Dish'] == thl]
    thldata['Ingredients'] = thldata.Ingredients.apply(lambda x: x.split(','))
    thling = list(thldata['Ingredients'])[0]
    thlurl = thldata['URL']
    thddata = data[data['Dish'] == thd]
    thddata['Ingredients'] = thddata.Ingredients.apply(lambda x: x.split(','))
    thding = list(thddata['Ingredients'])[0]
    thdurl = thddata['URL']
    # Friday
    # st.markdown('## Friday')
    col1, col2, col3 = st.beta_columns(3)
    frb = col1.selectbox(
        'Friday breakfast:',
        data['Dish'].unique()
    )
    frl = col2.selectbox(
        'Friday lunch:',
        data['Dish'].unique()
    )
    frd = col3.selectbox(
        'Friday dinner:',
        data['Dish'].unique()
    )
    frbdata = data[data['Dish'] == frb]
    frbdata['Ingredients'] = frbdata.Ingredients.apply(lambda x: x.split(','))
    frbing = list(frbdata['Ingredients'])[0]
    frburl = frbdata['URL']
    frldata = data[data['Dish'] == frl]
    frldata['Ingredients'] = frldata.Ingredients.apply(lambda x: x.split(','))
    frling = list(frldata['Ingredients'])[0]
    frlurl = frldata['URL']
    frddata = data[data['Dish'] == frd]
    frddata['Ingredients'] = frddata.Ingredients.apply(lambda x: x.split(','))
    frding = list(frddata['Ingredients'])[0]
    frdurl = frddata['URL']
    # Saturday
    # st.markdown('## Saturday')
    col1, col2, col3 = st.beta_columns(3)
    sab = col1.selectbox(
        'Saturday breakfast:',
        data['Dish'].unique()
    )
    sal = col2.selectbox(
        'Saturday lunch:',
        data['Dish'].unique()
    )
    sad = col3.selectbox(
        'Saturday dinner:',
        data['Dish'].unique()
    )
    sabdata = data[data['Dish'] == sab]
    sabdata['Ingredients'] = sabdata.Ingredients.apply(lambda x: x.split(','))
    sabing = list(sabdata['Ingredients'])[0]
    saburl = sabdata['URL']
    saldata = data[data['Dish'] == sal]
    saldata['Ingredients'] = saldata.Ingredients.apply(lambda x: x.split(','))
    saling = list(saldata['Ingredients'])[0]
    salurl = saldata['URL']
    saddata = data[data['Dish'] == sad]
    saddata['Ingredients'] = saddata.Ingredients.apply(lambda x: x.split(','))
    sading = list(saddata['Ingredients'])[0]
    sadurl = saddata['URL']
    # Sunday
    # st.markdown('## Sunday')
    col1, col2, col3 = st.beta_columns(3)
    sub = col1.selectbox(
        'Sunday breakfast:',
        data['Dish'].unique()
    )
    sul = col2.selectbox(
        'Sunday lunch:',
        data['Dish'].unique()
    )
    sud = col3.selectbox(
        'Sunday dinner:',
        data['Dish'].unique()
    )
    subdata = data[data['Dish'] == sub]
    subdata['Ingredients'] = subdata.Ingredients.apply(lambda x: x.split(','))
    subing = list(subdata['Ingredients'])[0]
    suburl = subdata['URL']
    suldata = data[data['Dish'] == sul]
    suldata['Ingredients'] = suldata.Ingredients.apply(lambda x: x.split(','))
    suling = list(suldata['Ingredients'])[0]
    sulurl = suldata['URL']
    suddata = data[data['Dish'] == sud]
    suddata['Ingredients'] = suddata.Ingredients.apply(lambda x: x.split(','))
    suding = list(suddata['Ingredients'])[0]
    sudurl = suddata['URL']
with st.beta_expander('Show shopping list'):
    # st.markdown('## Shopping list')
    allings = set(mobing + moling + moding + tubing + tuling + tuding + webing + weling + weding + thbing + thling + thding + frbing + frling + frding + sabing + saling + sading + subing + suling + suding)
    for i in allings:
        st.checkbox(i)
with st.beta_expander('Show recipie links'):
    allurls = [moburl, molurl, modurl, tuburl, tulurl, tudurl, weburl, welurl, wedurl, thburl, thlurl, thdurl, frburl, frlurl, frdurl, saburl, salurl, sadurl, suburl, sulurl, sudurl]
    for i in allurls:
        if pd.notna(i.values):
            st.write(i.values)
