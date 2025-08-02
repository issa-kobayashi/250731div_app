import streamlit as st
from PIL import Image
# imageﾊpip install pillowｶﾞ必要 pil
import time
import datetime
n=0

st.title('250731streamlit')
st.caption('町内の為のホームページです｡')


#streamlit run e:\250731div_app\250731streamlit.py
#上記をｺﾏﾝﾄﾞﾌﾟﾛﾝﾌﾟﾄに打ち込みﾛｰｶﾙﾎｽﾄを起動させる


#縦に分轄
col1,col2=st.columns(2)

with col1:
        st.subheader('みずき野紹介')
        
        st.text('みずき野は田んぼに囲まれたとても静かな街です｡')
        st.write('かがた公園')
        
        
        #画像の登録
        #image=Image.open('iris_tree.png')
        image1=Image.open('./data250731re/IMG241103-11-01.jpg')
        
        #streamlitﾆimageｦ渡す
        st.image(image1,width=400)
        
        image2=Image.open('./data250731re/IMG241103-11-02.jpg')
        st.image(image2,width=400)
        
        image3=Image.open('./data250731re/IMG241103-11-03.jpg')
        st.image(image3,width=400)
            
        image4=Image.open('./data250731re/IMG250514-13-01.jpg')
        st.image(image4,width=400)
        
with col2:    
        
        #submit_btn=st.form_submit_button (f'切替')
        submit_btn=st.button('切替')
  
        
        if submit_btn:
            n=n+1
            st.text(f'切替完 n=',n)
            if 4<n :
               n=0
               
         
        if n==0 :
          image1=Image.open('./data250731re/IMG241103-11-01.jpg')
          image2=Image.open('./data250731re/IMG241103-11-02.jpg') 
          image3=Image.open('./data250731re/IMG241103-11-03.jpg') 
          image4=Image.open('./data250731re/IMG241103-11-04.jpg') 
          name='IMG241103-11-01','IMG241103-11-02','IMG241103-11-03','IMG241103-11-04'
          
        if n==1 :
          image1=Image.open('./data250731re/IMG241103-11-05.jpg')
          image2=Image.open('./data250731re/IMG241103-11-06.jpg') 
          image3=Image.open('./data250731re/IMG241103-12-07.jpg') 
          image4=Image.open('./data250731re/IMG241103-12-08.jpg') 
          name='IMG241103-11-05','IMG241103-11-06','IMG241103-11-07','IMG241103-11-08'
          
        if n==2 :
          image1=Image.open('./data250731re/IMG250212-09-01.jpg')
          image2=Image.open('./data250731re/IMG250212-09-02.jpg') 
          image3=Image.open('./data250731re/IMG250212-09-03.jpg') 
          image4=Image.open('./data250731re/IMG250302-14-01.jpg')     
          name='IMG250212-09-01','IMG250212-09-02','IMG250212-09-03','IMG250302-14-01'
         
        if n==3 :
          image1=Image.open('./data250731re/IMG250302-09-01.jpg')
          image2=Image.open('./data250731re/IMG250514-09-02.jpg') 
          image3=Image.open('./data250731re/IMG250514-09-03.jpg') 
          image4=Image.open('./data250731re/IMG250514-13-01.jpg')  
          name='IMG250302-09-01','IMG250514-09-02','IMG250514-09-03','IMG250514-13-01'
          
        if n==4 :
          image1=Image.open('./data250731re/IMG250514-13-02.jpg')
          image2=Image.open('./data250731re/IMG250514-13-03.jpg') 
          image3=Image.open('./data250731re/IMG250514-14-04.jpg') 
          image4=Image.open('./data250731re/IMG250514-14-05.jpg')   
          name='IMG250514-13-02','IMG250514-13-03','IMG250514-14-04','IMG250514-14-05'
        
        st.image(image1,width=400)
        st.image(image2,width=400)
        st.image(image3,width=400)
        st.image(image4,width=400)
        
        
        name='IMG241103-11-01','IMG241103-11-02','IMG241103-11-03','IMG241103-11-04'

        st.text(f'{name}')

