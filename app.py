import pickle
def loadModel():
    pickle_a = open("model.pkl","rb")
    regressor = pickle.load(pickle_a)
    return regressor

def convertNeighbourhood(neighbourhood):
    if neighbourhood == 'Allston-Brighton':
        return 0
    elif neighbourhood == 'Back Bay':
        return 1
    elif neighbourhood == 'Beacon Hill':
        return 2
    elif neighbourhood == 'Brookline':
        return 3
    elif neighbourhood == 'Cambridge':
        return 4
    elif neighbourhood == 'Charlestown':
        return 5
    elif neighbourhood == 'Chestnut Hill':
        return 6
    elif neighbourhood == 'Chinatown':
        return 7
    elif neighbourhood == 'Dorchester':
        return 8
    elif neighbourhood == 'Downtown':
        return 9
    elif neighbourhood == 'Downtown Crossing':
        return 10
    elif neighbourhood == 'East Boston':
        return 11
    elif neighbourhood == 'Fenway/Kenmore':
        return 12
    elif neighbourhood == 'Financial District':
        return 13
    elif neighbourhood == 'Government Center':
        return 14
    elif neighbourhood == 'Harvard Square':
        return 15
    elif neighbourhood == 'Hyde Park':
        return 16
    elif neighbourhood == 'Jamaica Plain':
        return 17
    elif neighbourhood == 'Leather District':
        return 18
    elif neighbourhood == 'Mattapan':
        return 19
    elif neighbourhood == 'Mission Hill':
        return 20
    elif neighbourhood == 'North End':
        return 21
    elif neighbourhood == 'Roslindale':
        return 22
    elif neighbourhood == 'Roxbury':
        return 23
    elif neighbourhood == 'Somerville':
        return 24
    elif neighbourhood == 'South Boston':
        return 25
    elif neighbourhood == 'South End':
        return 26
    elif neighbourhood == 'Theater District':
        return 27
    elif neighbourhood == 'West End':
        return 28
    elif neighbourhood == 'West Roxbury':
        return 29

def convertPropertyType(property_type):
    if property_type == 'Apartment':
        return 0
    elif property_type == 'Bed & Breakfast':
        return 1
    elif property_type == 'Boat':
        return 2
    elif property_type == 'Condominium':
        return 3
    elif property_type == 'Dorm':
        return 4
    elif property_type == 'Entire Floor':
        return 5
    elif property_type == 'Guest house':
        return 6
    elif property_type == 'House':
        return 7
    elif property_type == 'Loft':
        return 8
    elif property_type == 'Other':
        return 9
    elif property_type == 'Town house':
        return 10
    elif property_type == 'Villa':
        return 11

def convertRoomType(room_type):
    if room_type == 'Entire home/apt':
        return 0
    elif room_type == 'Private room':
        return 1
    elif room_type == 'Shared room':
        return 2

def convertBedType(bed_type):
    if bed_type == 'Airbed':
        return 0
    elif bed_type == 'Couch':
        return 1
    elif bed_type == 'Futon':
        return 2
    elif bed_type == 'Pull-out Sofa':
        return 3
    elif bed_type == 'Real Bed':
        return 4

def convertCancellationPolicy(cancellation_policy):
    if cancellation_policy == 'flexible':
        return 0
    elif cancellation_policy == 'moderate':
        return 1
    elif cancellation_policy == 'strict':
        return 2
    elif cancellation_policy == 'super strict':
        return 3

def predictPrice(neighbourhood,property_type,room_type,accommodates,bedrooms,bathrooms,beds,bed_type,availability_365,cancellation_policy):
    regressor = loadModel()

    neighbourhood = convertNeighbourhood(neighbourhood)
    property_type = convertPropertyType(property_type)
    room_type = convertRoomType(room_type)
    bed_type = convertBedType(bed_type)
    cancellation_policy = convertCancellationPolicy(cancellation_policy)

    prediction = regressor.predict([[neighbourhood,property_type,room_type,accommodates,bathrooms,bedrooms,beds,bed_type,availability_365,cancellation_policy]])
    return prediction 

def main():
    price = 0
    
    st.set_page_config(page_title='Airbnb Price Predictor',layout='wide', page_icon=None,  initial_sidebar_state="auto", menu_items=None)
    col1, col2, col3= st.columns(gap="large",spec=[1.5,1,4])

    with col1:
        neighbourhoods = ['Roslindale', 'Jamaica Plain', 'Mission Hill', 'Fenway/Kenmore','Back Bay', 'Leather District', 'Chinatown', 'Hyde Park','North End', 'Roxbury', 'South End', 'Mattapan', 'East Boston','South Boston', 'Charlestown', 'West End', 'Beacon Hill','Theater District', 'Downtown Crossing', 'Downtown','Financial District', 'Government Center', 'Allston-Brighton','West Roxbury', 'Chestnut Hill', 'Dorchester', 'Brookline','Cambridge', 'Somerville', 'Harvard Square']
        neighbourhood = st.selectbox(label='Select Neighbourhood', options=neighbourhoods)

        property_types = ['House', 'Apartment', 'Condominium', 'Villa', 'Bed & Breakfast','Town house', 'Entire Floor', 'Loft', 'Guest house', 'Boat', 'Dorm','Other', 'Unknown']
        property_type = st.selectbox(label='Select Property Type', options=property_types)

        room_types = ['Entire home/apt', 'Private room', 'Shared room']
        room_type = st.selectbox(label='Select Room Type', options=room_types)

        accommodates = st.number_input(label='No.of accommodates', min_value=1, max_value=16, format='%d')

        bedrooms = st.number_input(label='No.of bedrooms', min_value=1, max_value=5,format='%d')

        bathrooms = st.number_input(label='No.of bathrooms', min_value=0.0, max_value=6.0, step=0.5, format='%.1f')

        beds = st.number_input(label='No.of beds', min_value=1, max_value=16)

        bed_types = ['Real Bed', 'Pull-out Sofa', 'Futon', 'Airbed', 'Couch']
        bed_type = st.selectbox(label='Select Bed Type', options=bed_types)

        availability_365 = st.number_input(label='No.of days available in a year', min_value=1, max_value=365, format='%d')

        cancellation_policies = ['moderate', 'flexible', 'strict', 'super strict']
        cancellation_policy = st.selectbox(label='Select Cancellation Policy', options=cancellation_policies)

    with col3:
        
        image = Image.open('./public/airbnb.png')
        st.image(image, width=250)

        st.markdown(
            "<h5 >Predict a price for your Airbnb based on what you are providing to customers</h5><br>"
            , unsafe_allow_html=True)

        if st.button(label="Predict Price"):
            price = predictPrice(neighbourhood,property_type,room_type,accommodates,bathrooms,bedrooms,beds,bed_type,availability_365,cancellation_policy) 
            price = str(price)[1:-1]
            price = "{:.2f}".format(float(price))
            st.header(f"Estimated Price is: ${price}")
    
    with col2:
        pass
            
if __name__=='__main__':
    main()

