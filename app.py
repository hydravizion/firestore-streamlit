import streamlit as st

from google.cloud import firestore

db = firestore.Client.from_service_account_json("firekey.json")
# doc_ref = db.collection('users').document('alovelace')
# doc_ref.set({
#     'first': 'Ada',
#     'last': 'Lovelace',
#     'born': 1815
# })

# Then query to list all users
my_details_ref = db.collection('my-details') #.document("private-info")
name = ""
summ = ""
# for doc in users_ref.stream():
#     print('{} => {}'.format(doc.id, doc.to_dict()))
#     st.write('{} => {}'.format(doc.id, doc.to_dict()))
# st.write(my_details_ref.get().to_dict())

for doc in my_details_ref.stream():
    details = doc.to_dict()
    name = details["name"]
    summ = details["summary"]

st.title(name)
st.subheader("Summary")
st.write(summ)
st.subheader("Working Experience")