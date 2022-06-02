import streamlit as st
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

header = st.container()
dataset = st.container()
with header:
    st.title('''NATIONAL CENTRE FOR TECHNOLOGY MANAGEMENT STI INDICATORS DASHBOARD''')
    st.text('''*The sample was randomly selected based on the list of establishments with at least 10 employees obtained from the National Bureau of Statistics (NBS) and the Nigerian Stock Exchange. 
* The Stock Exchange list includes only formal firms whereas the NBS list includes both formal and informal firms. These two sources were cross-referenced and any firm listed in both sources was automatically selected into the sample. The logic is that if a listed firm is still surviving. Note that firm exit rate is particularly high in Nigeria. 
* Subsequently, all other firms were stratified into six geographical zones (North-East, 
*`North-West, North-Central, South-West, South-East, South-South) and sector of activity. 
* The final sample was selected by proportional probability. 
* The survey questionnaire was delivered by hand to all the firms, and in many instances, some of the selected firms did no longer exist. In every possible case, the missing firm was substituted with another one in the same sector and geographical location. 
* The survey was first carried out in 2008 (initial sample of 1000 firms) and then repeated in 2011 (initial sample of 1500 firms). The final pooled sample includes 1359 firms, an overall response rate of 54%.

The pooled cross-sectional dataset available for download has some specific features:

* The dataset includes data from wave 1 (2005-2007) and wave 2 (2008-2010) of the Nigerian innovation surveys. 
* The year variable identifies the different survey waves. Wave 1 was completed in 2008 and wave 2, in 2011. 
* The service variable sorts the observations broadly into manufacturing and services. 
* The id variable identifies each unique firm. Repeatedness was ignored because repeated cases are only about 2.5%.
* As much as possible, variables have been matched across the two waves.   
* Due to coding changes and some inconsistencies in the survey instrument, a few variables could not be matched.  
* Any variable that could not be matched is retained in its original form.  
* Some of the variables have notes attached to them. The notes are consistent with what is in the accompanying codebook.xls
* Item numbering on the questionnaire for the two waves are not consistent. Thus, rather than use question numbers for variable names – as is commonly done – intuitive variable names and labels (defined in detail in the accompanying codebook.xls) are used.
* Definitions of main concepts can be found in the accompanying codebook.xls.
* It is strongly recommended that users thoroughly familiarize themselves with the accompanying codebook as well as the questionnaires for each of the waves before applying the dataset. This is crucial especially because of the skip patterns. While everything was done to ensure that the skip patterns were all correctly established, there can be no guarantee of perfection. 
* It is also strongly recommended that users be familiar with the nature of innovation surveys as this will help in understanding how to treat the data for analysis. The Oslo Manual, which is freely available online, is a very useful resource.

To have a feel of the sectoral distribution of the sample, type in Stata: tab service year


		Year data collected
Service		2008	2011	Total
			
manufacturing	519	371	890 
service		209	260	469 
			
Total		728	631	1,359 ''')

with dataset:
    st.header('NIGERIA INNOVATION DATA')
    df = pd.read_csv('nidata101.csv')
    df['turnover07'] = df['turnover07'].fillna(0)
    if st.checkbox('Show Data'):
        st.write(df.head())
        st.write(df['year'].info())
    st.subheader('EXPLORATORY DATA ANALYSIS')
    df2=df['sector'].value_counts()
    st.sidebar.subheader('NIGERIA INNOVATION ANAYLSIS')
    select = st.sidebar.selectbox('VISUALIZATION OF DATA',['NO OF COMPANY IN EACH SECTOR',
    'PERCENTAGE RATE OF EACH SECTOR','GROUPING OF SECTORS ACORDING TO THEIR AREA OF SERVICES',
    'TOTAL NUMBER OF STAFFS IN YEAR 2005 BY SECTORS ACORDING TO THEIR AREA OF SERVICES',
    'TOTAL NUMBER OF STAFFS IN YEAR 2006 BY SECTORS ACORDING TO THEIR AREA OF SERVICES',
    'TOTAL NUMBER OF STAFFS IN YEAR 2006 BY SECTORS ACORDING TO THEIR AREA OF SERVICES',
    'TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2005 FOR EACH SECTOR GROUPED BY THEIR SERVICES',
    'TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2006 FOR EACH SECTOR GROUPED BY THEIR SERVICES',
    'TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2007 FOR EACH SECTOR GROUPED BY THEIR SERVICES',
    'SECTORS AND THEIR INFORMATION SOURCE - INTERNAL',
    'SECTORS AND THEIR INFORMATION SOURCE - SUPPLIERS','SECTORS AND THEIR INFORMATION SOURCE -CUSTORMERS',
    'SECTORS AND THEIR INFORMATION SOURCE -COMPETITORS','SECTORS AND THEIR INFORMATION SOURCE -CONSULTANTS, COMMERCIAL LABS OR PRIVATE R&D INSTITUTES',
    'SECTORS AND THEIR INFORMATION SOURCE -UNIVERSITIES, OTHER HIGHER ED. INSTITUTIONS','SECTORS AND THEIR INFORMATION SOURCE -PUBLIC RESEARCH INSTITUTES',
    'SECTORS AND THEIR INFORMATION SOURCE -CONFERENCES, FAIRS, EXHIBITIONS','SECTORS AND THEIR INFORMATION SOURCE -JOURNALS, TRADE PUBLICATIONS',
    'SECTORS AND THEIR INFORMATION SOURCE -PROFESSIONAL, INDUSTRY ASSOCIATIONS','EFFECT OF INNOVATION (PRODUCT) - INCREASED RANGE OF GOODS/SERVICE OF EACH SECTORS',],key=1)
    if st.checkbox('Show Plot'):
        if select == 'NO OF COMPANY IN EACH SECTOR':
            col1,col2 = st.columns(2)
            df2= df['sector'].value_counts()
            with col1:
                st.subheader('VARIOUS SECTOR AND THE TOTAL NUMBER OF INDUSTRIES UNDER EACH SECTORS')
                fig = px.bar(x=df2.index,y = df2.values ,labels={'x':'Sector','y':'Outcome'},width=500, height=500)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                        paper_bgcolor="#4233FF ",)

                st.plotly_chart(fig)
            with col2:
                st.table(df2)
        elif select == 'PERCENTAGE RATE OF EACH SECTOR':
            st.subheader('PERCENTAGE RATE OF EACH SECTOR')
            fig =px.pie(names=df2.index,values=df2.values,color = df2.index,width=800, height=500)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="#4233FF",)
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig)
        elif select == 'GROUPING OF SECTORS ACORDING TO THEIR AREA OF SERVICES':
            st.subheader('GROUPING OF SECTORS ACORDING TO THEIR AREA OF SERVICES')
            fig = px.histogram(df, x="sector", color="service",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                paper_bgcolor="#4233FF ",)
            st.plotly_chart(fig)
        elif select == 'TOTAL NUMBER OF STAFFS IN YEAR 2005 BY SECTORS ACORDING TO THEIR AREA OF SERVICES':
            st.subheader('TOTAL NUMBER OF STAFFS IN YEAR 2005 BY SECTORS ACORDING TO THEIR AREA OF SERVICES')
            fig = px.sunburst(df, path=['service', 'sector'], values='totalstaff05',width=1000, height=500)
            fig.update_traces(textinfo='label+percent entry')
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                paper_bgcolor="#4233FF ",)
           
            st.plotly_chart(fig)
        elif select == 'TOTAL NUMBER OF STAFFS IN YEAR 2006 BY SECTORS ACORDING TO THEIR AREA OF SERVICES':
            st.subheader('TOTAL NUMBER OF STAFFS IN YEAR 2006 BY SECTORS ACORDING TO THEIR AREA OF SERVICES')
            fig = px.sunburst(df, path=['service', 'sector'], values='totalstaff06',width=800, height=800)
            fig.update_traces(textinfo='label+percent entry')
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                paper_bgcolor="#4233FF ",)
            st.plotly_chart(fig)
        elif select == 'TOTAL NUMBER OF STAFFS IN YEAR 2007 BY SECTORS ACORDING TO THEIR AREA OF SERVICES':
            st.subheader('TOTAL NUMBER OF STAFFS IN YEAR 2007 BY SECTORS ACORDING TO THEIR AREA OF SERVICES')
            fig = px.sunburst(df, path=['service', 'sector'], values='totalstaff07',width=800, height=500,color_continuous_scale='mint')
            fig.update_traces(textinfo='label+percent entry')
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                paper_bgcolor="#4233FF ",)
            st.plotly_chart(fig)
        elif select == 'TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2005 FOR EACH SECTOR GROUPED BY THEIR SERVICES':
            df = df[df['turnover05']!=0]
            st.subheader('TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2005 FOR EACH SECTOR GROUPED BY THEIR SERVICES')
            fig = px.sunburst(df, path=['service', 'sector'], values='turnover05',width=800, height=500,color='turnover05', 
            color_continuous_scale='balance',color_continuous_midpoint=np.mean(df['turnover05']))
            fig.update_traces(textinfo='label+percent entry') 
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                paper_bgcolor="#4233FF ",)
            st.plotly_chart(fig)
        elif select == 'TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2006 FOR EACH SECTOR GROUPED BY THEIR SERVICES':
            df = df[df['turnover06']!=0]
            st.subheader('TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2006 FOR EACH SECTOR GROUPED BY THEIR SERVICES')
            fig = px.sunburst(df, path=['service', 'sector'], values='turnover06',width=800, height=500,color='turnover06', 
            color_continuous_scale='redor',color_continuous_midpoint=np.mean(df['turnover06']))
            fig.update_traces(textinfo='label+percent entry') 
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                paper_bgcolor="#4233FF ",)
            st.plotly_chart(fig)
        elif select == 'TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2007 FOR EACH SECTOR GROUPED BY THEIR SERVICES':
            df = df[df['turnover07']!=0]
            st.subheader('TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2007 FOR EACH SECTOR GROUPED BY THEIR SERVICES')
            fig = px.sunburst(df, path=['service', 'sector'], values='turnover07',width=800, height=500,color='turnover07', 
            color_continuous_scale='rainbow',color_continuous_midpoint=np.mean(df['turnover07']))
            fig.update_traces(textinfo='label+percent entry') 
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                paper_bgcolor="#4233FF ",)

            st.plotly_chart(fig)
        elif select == 'SECTORS AND THEIR INFORMATION SOURCE - INTERNAL':
            st.subheader(' SECTORS AND THEIR INFORMATION SOURCE - INTERNAL')
            fig = px.histogram(df, x="sector", color="sinfo1",width=800, height=500)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                paper_bgcolor="#4233FF ",)
            st.plotly_chart(fig)
        elif select == 'SECTORS AND THEIR INFORMATION SOURCE - SUPPLIERS':
            st.subheader('SECTORS AND THEIR INFORMATION SOURCE - SUPPLIERS')
            fig = px.histogram(df, x="sector", color="sinfo2",width=800, height=500)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                paper_bgcolor="#4233FF ",)
            st.plotly_chart(fig)
        elif select == 'SECTORS AND THEIR INFORMATION SOURCE -CUSTORMERS':
            st.subheader('SECTORS AND THEIR INFORMATION SOURCE -CUSTORMERS')
            fig = px.histogram(df, x="sector", color="sinfo3",width=800, height=500) 
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                paper_bgcolor="#4233FF ",)
            st.plotly_chart(fig)
        elif select == 'SECTORS AND THEIR INFORMATION SOURCE -COMPETITORS':
            st.subheader('SECTORS AND THEIR INFORMATION SOURCE -COMPETITORS')
            fig = px.histogram(df, x="sector", color="sinfo4",width=800, height=500) 
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                paper_bgcolor="#4233FF ",)
            st.plotly_chart(fig)
        elif select == 'SECTORS AND THEIR INFORMATION SOURCE -CONSULTANTS, COMMERCIAL LABS OR PRIVATE R&D INSTITUTES':
            st.subheader('SECTORS AND THEIR INFORMATION SOURCE -CONSULTANTS, COMMERCIAL LABS OR PRIVATE R&D INSTITUTES')
            fig = px.histogram(df, x="sector", color="sinfo5",width=800, height=500)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                paper_bgcolor="#4233FF ",)
            st.plotly_chart(fig)
        elif select == 'SECTORS AND THEIR INFORMATION SOURCE -UNIVERSITIES, OTHER HIGHER ED. INSTITUTIONS':
            st.subheader('SECTORS AND THEIR INFORMATION SOURCE -UNIVERSITIES, OTHER HIGHER ED. INSTITUTIONS')
            fig = px.histogram(df, x="sector", color="sinfo6",width=800, height=500)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                paper_bgcolor="#4233FF ",)
            st.plotly_chart(fig)
        elif select == 'SECTORS AND THEIR INFORMATION SOURCE -PUBLIC RESEARCH INSTITUTES':
            st.subheader('SECTORS AND THEIR INFORMATION SOURCE -PUBLIC RESEARCH INSTITUTES')
            fig = px.histogram(df, x="sector", color="sinfo7",width=800, height=500)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                paper_bgcolor="#4233FF ",)
            st.plotly_chart(fig)
        elif select == 'SECTORS AND THEIR INFORMATION SOURCE -CONFERENCES, FAIRS, EXHIBITIONS':
            st.subheader('SECTORS AND THEIR INFORMATION SOURCE -CONFERENCES, FAIRS, EXHIBITIONS')
            fig = px.histogram(df, x="sector", color="sinfo8",width=800, height=500)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                paper_bgcolor="#4233FF ",)
            st.plotly_chart(fig)
        elif select == 'SECTORS AND THEIR INFORMATION SOURCE -JOURNALS, TRADE PUBLICATIONS':
            st.subheader('SECTORS AND THEIR INFORMATION SOURCE -JOURNALS, TRADE PUBLICATIONS')
            fig = px.histogram(df, x="sector", color="sinfo9",width=800, height=500)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                paper_bgcolor="#4233FF ",)
            st.plotly_chart(fig)
        elif select == 'SECTORS AND THEIR INFORMATION SOURCE -PROFESSIONAL, INDUSTRY ASSOCIATIONS':
            st.subheader('SECTORS AND THEIR INFORMATION SOURCE -PROFESSIONAL, INDUSTRY ASSOCIATIONS')
            fig = px.histogram(df, x="sector", color="sinfo10",width=800, height=500)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                paper_bgcolor="#4233FF ",)
            st.plotly_chart(fig)
            
        elif select == 'EFFECT OF INNOVATION (PRODUCT) - INCREASED RANGE OF GOODS/SERVICE OF EACH SECTORS':
            st.subheader('EFFECT OF INNOVATION (PRODUCT) - INCREASED RANGE OF GOODS/SERVICE OF EACH SECTORS')
            fig = px.histogram(df, x="sector", color="ieffect_prod1",width=800
            , height=500)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                paper_bgcolor="#4233FF ",)
            st.plotly_chart(fig)
    


   
