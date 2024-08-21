import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import pymysql





username = 'admin'
password = 'password'
host = 'link'
port = '3306' 
database = 'tamil'



# connection to the MySQL database
def get_connection():
    mysql = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'
    engine = create_engine(mysql)
    return engine






#bus data from MySQL
@st.cache_data
def fetch_bus_data():
    try:
        engine = get_connection()
        query = "SELECT * FROM Redbus"
        df = pd.read_sql(query, engine)
        engine.dispose()
        return df
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()  # Return error
    




# categorize bus types

def categorize_bus_type(bus_type):
    type_mapping = {
        'SUPER LUXURY (NON-AC, 2 + 2 PUSH BACK)': 'Non AC Sleeper',
        'RAJDHANI (A.C. Semi Sleeper)': 'AC Semi Sleeper',
        'GARUDA PLUS (VOLVO / BENZ A.C Multi Axle)': 'AC Sleeper',
        'RAJADHANI AC (CONVERTED METRO LUXURY)': 'AC Sleeper',
        'eGARUDA': 'AC Sleeper',
        'LAHARI A/C SLEEPER CUM SEATER': 'AC Sleeper',
        'Lahari Non A/C Sleeper Cum Seater': 'Non AC Sleeper',
        'A/C Seater / Sleeper (2+1)': 'AC Seater/Sleeper',
        'Electric A/C Seater (2+2)': 'AC Seater',
        'A/C Seater/Sleeper (2+1)': 'AC Seater/Sleeper',
        'AC Sleeper (2+1)': 'AC Sleeper',
        'A/C Sleeper (2+1)': 'AC Sleeper',
        'Scania AC Multi Axle Sleeper (2+1)': 'AC Sleeper',
        'Electric A/C Seater/Sleeper (2+1)': 'AC Seater/Sleeper',
        'Volvo A/C Semi Sleeper (2+2)': 'AC Semi Sleeper',
        'VE A/C Sleeper (2+2)': 'AC Sleeper',
        'AC Seater (2+3)': 'AC Seater',
        'A/C Seater / Sleeper (2+2)': 'AC Seater/Sleeper',
        'A/C Push Back (2+3)': 'AC Seater',
        'A/C Executive (2+3)': 'AC Seater',
        'NON A/C Seater Push Back (2+3)': 'Non AC Seater',
        'NON A/C Seater Pushback (2+3)': 'Non AC Seater',
        'Volvo 9600 A/C Seater (2+2)': 'AC Seater',
        'Volvo 9600 A/C Semi Sleeper (2+2)': 'AC Semi Sleeper',
        'Volvo B11R Multi Axle Seater (2+2)': 'AC Seater',
        'Non AC Seater 2+2': 'Non AC Seater',
        'Volvo Multi-Axle A/C seater/sleeper (2+1)': 'AC Seater/Sleeper',
        'NON A/C Seater / Sleeper (2+2)': 'Non AC Seater/Sleeper',
        'Volvo Multi-Axle A/C Seater/Sleeper (2+1)': 'AC Seater/Sleeper',
        'NON A/C Seater Push Back (2+3)': 'Non AC Seater',
        'Express (Non AC Seater 2+2)': 'Non AC Seater',
        'Volvo AC Seater (2+2)': 'AC Seater',
        'DOLPHIN CRUISE (VOLVO / SCANIA A.C Multi Axle)': 'AC Sleeper',
        'Rajdhani (AC Semi Sleeper 2+2)': 'AC Semi Sleeper',
        'Deluxe (Non AC Seater 2+2)': 'Non AC Seater',
        'Bharat Benz A/C Seater (2+2)': 'AC Seater',
        'NON A/C Seater (2+1)': 'Non AC Seater',
        'NON A/C Sleeper (2+2)': 'Non AC Sleeper',
        'Mercedes Benz Multi-Axle A/C Sleeper (2+1)': 'AC Sleeper',
        'NON A/C Sleeper (1+2)': 'Non AC Sleeper',
        'AC Seater Hvac 2+2': 'AC Seater',
        'Scania A/C Semi Sleeper (2+2)': 'AC Semi Sleeper',
        'A/C Semi Sleeper / Sleeper (2+2)': 'AC Semi Sleeper/Sleeper',
        'Mercedes Multi-Axle Semi Sleeper (2+2)': 'AC Semi Sleeper',
        'Volvo A/C (2+2)': 'AC Seater',
        'Express Non AC Seater 2+3': 'Non AC Seater',
        'Bharat Benz A/C Seater / Sleeper (2+2)': 'AC Seater/Sleeper',
        'HVAC Seater (2+3)': 'AC Seater',
        'Mercedes Benz A/C Sleeper (2+1)': 'AC Sleeper',
        'Volvo Multi-Axle A/C Seater (2+2)': 'AC Seater',
        'Tata A/C Seater (2+2)': 'AC Seater',
        'Volvo AC Seater 2+2': 'AC Seater',
        'A/C Seater / Sleeper (3+1)': 'AC Seater/Sleeper',
        'A/C Seater Hi-Tech Push Back (2+2)': 'AC Seater',
        'Volvo A/C Seater / Sleeper (2+1)': 'AC Seater/Sleeper',
        'A/C Seater Push Back (2+1)': 'AC Seater',
        'A/C Seater (2+1)': 'AC Seater',
        'Volvo AC Seater Pushback 2+2': 'AC Seater',
        'Bharat Benz A/C Seater (2+1)': 'AC Seater',
        'NON A/C Seater Semi Sleeper (2+1)': 'Non AC Semi Sleeper',
        'NON AC Seater/ Sleeper (2+1)': 'Non AC Seater/Sleeper',
        'Non AC Seater (2+1)': 'Non AC Seater',
        'NON A/C Seater Push Back (2+1)': 'Non AC Seater',
        'NON A/C Seater / Sleeper (3+1)': 'Non AC Seater/Sleeper',
        'Bharat Benz NON A/C Seater / Sleeper (2+1)': 'Non AC Seater/Sleeper',
        'Tempo Traveler NON A/C': 'Non AC Seater',
        'A/C Sleeper (2+2)': 'AC Sleeper',
        'Volvo A/C Sleeper (2+2)': 'AC Sleeper',
        'VE A/C Sleeper (2+2)': 'AC Sleeper',
        'AshokLeyland Stile A/C': 'AC Seater',
        'Bharath Benz A/C Sleeper (2+2)': 'AC Sleeper',
        # more mappings as needed
    }
    return type_mapping.get(bus_type, 'Others')






#categorize time ranges
def categorize_time(time):
    if isinstance(time, str):
        time = pd.to_datetime(time).time()
    if time >= pd.Timestamp('00:00:00').time() and time < pd.Timestamp('04:00:00').time():
        return '0 to 4'
    elif time >= pd.Timestamp('04:00:00').time() and time < pd.Timestamp('08:00:00').time():
        return '4 to 8'
    elif time >= pd.Timestamp('08:00:00').time() and time < pd.Timestamp('12:00:00').time():
        return '8 to 12'
    elif time >= pd.Timestamp('12:00:00').time() and time < pd.Timestamp('16:00:00').time():
        return '12 to 16'
    elif time >= pd.Timestamp('16:00:00').time() and time < pd.Timestamp('20:00:00').time():
        return '16 to 20'
    elif time >= pd.Timestamp('20:00:00').time() and time <= pd.Timestamp('23:59:59').time():
        return '20 to 24'
    else:
        return 'Invalid Time'
    



def main():
    
    data = fetch_bus_data()
    if data.empty:
        st.stop() 




    
      # If column is string

    if data['departing_time'].dtype == 'object':
        try:
            data['departing_time'] = pd.to_datetime(data['departing_time'], format='%H:%M:%S').dt.time
            data['reaching_time'] = pd.to_datetime(data['reaching_time'], format='%H:%M:%S').dt.time
        except Exception as e:
            st.error(f"Error converting 'departing_time' or 'reaching_time': {e}")
            st.stop()



    # Apply categorization
    data['departure_range'] = data['departing_time'].apply(categorize_time)
    data['arrival_range'] = data['reaching_time'].apply(categorize_time)




    # Categorize bus type
    data['bus_category'] = data['bus_types'].apply(categorize_bus_type)

    st.title("Bus Data Dashboard")



    # Filter by route name
    route = st.sidebar.selectbox("Select a Route", options=["All"] + list(sorted(data['route_names'].unique())))
    if route != "All":
        data = data[data['route_names'] == route]



    # price filter
    min_price, max_price = st.sidebar.slider("Price Range", 0.0,12500.0, (float(data['prices'].min()), float(data['prices'].max())))
    data = data[(data['prices'] >=0) & (data['prices'] <= 12500)]



    # star rating
    min_rating, max_rating = st.sidebar.slider("Rating Range", float(data['star_rating'].min()), float(data['star_rating'].max()), (float(data['star_rating'].min()), float(data['star_rating'].max())))
    data = data[(data['star_rating'] >= min_rating) & (data['star_rating'] <= max_rating)]



    #bus category
    bus_category = st.sidebar.selectbox("Select Bus Category", options=["All"] + list(data['bus_category'].unique()))
    if bus_category != "All":
        data = data[data['bus_category'] == bus_category]



    #time range
    departure_range = st.sidebar.selectbox("Select Departure Time Range", options=["All", "0 to 4", "4 to 8", "8 to 12", "12 to 16", "16 to 20", "20 to 24"])

    if departure_range != "All":
        data = data[data['departure_range'] == departure_range]



    # Display filtered data
    st.write("Filtered Bus Data")
    st.dataframe(data)



    #visualization
    bins = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
    labels = [f"{x} - {x + 0.5}" for x in bins[:-1]]
    data['star_rating_binned'] = pd.cut(data['star_rating'], bins=bins, labels=labels, right=False)
    
    rating_counts = data['star_rating_binned'].value_counts().sort_index()
    
    st.write(f"Total buses: {len(data)}")
    st.bar_chart(rating_counts)
   
   



if __name__ == "__main__":
    main()
