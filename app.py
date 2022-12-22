import streamlit as st
from google.oauth2 import service_account
from google.cloud import firestore
import json
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="streamlit-hydra")

st.set_page_config("Shabil's Portfolio",layout="wide")


# db = firestore.Client.from_service_account_json("firekey.json")
# doc_ref = db.collection('users').document('alovelace')
# doc_ref.set({
#     'first': 'Ada',
#     'last': 'Lovelace',
#     'born': 1815
# })
# for doc in users_ref.stream():
#     print('{} => {}'.format(doc.id, doc.to_dict()))
#     st.write('{} => {}'.format(doc.id, doc.to_dict()))
# st.write(my_details_ref.get().to_dict())

# for doc in my_details_ref.stream():
#     details = doc.to_dict()
#     name = details["name"]
#     summ = details["summary"]


class Education:
    def __init__(self, cert, cgpa,dur,loc):
        self.cert = cert
        self.cgpa = cgpa
        self.dur = dur
        self.loc = loc
    def getCert(self):
        return self.cert
    def getCgpa(self):
        return self.cgpa
    def getDur(self):
        return self.dur
    def getLoc(self):
        return self.loc
        
class AboutMe:
    def __init__(self, email, name, place, summ):
        self.email = email
        self.name = name
        self.place = place
        self.summ = summ
        
class WorkExp:
    def __init__(self, title, dur, place, projects):
        self.title = title
        self.dur = dur
        self.place = place
        self.projects = projects
        
st.info("My portfolio is still in development, TQ for visitting :)")

# Education integration
ref = db.collection("edu")
eduList = []
# ref.order_by("pos","asc")
for doc in ref.get():
    eduList.append(Education(doc.to_dict()["cert"],doc.to_dict()["cgpa"],doc.to_dict()["dur"],doc.to_dict()["loc"]))   


# Details integration
my_details_ref = db.collection('my-details') #.document("private-info")
details =  my_details_ref.get()[0].to_dict()
about = AboutMe(details["email"],details["name"],details["place"],details["summary"])

# Website info integration





# FE design
st.title(about.name)
tab1, tab2, tab3, tab4 = st.tabs(["About Me".center(15,"\u2001"), "Working Experience".center(25,"\u2001"), "Education".center(20,"\u2001"), "Side Projects".center(20,"\u2001")])

with tab1:
    st.subheader("Summary")
    st.write(about.summ)
    st.subheader("Skills")
    st.subheader("Contact")
    st.write("Email: " + about.email)
    st.write("Linked In: https://www.linkedin.com/in/shabil-imran-68953062/")

with tab2:
    st.subheader("Working Experience")
    
with tab3:
    # st.subheader("My Education")
    # st.markdown("""---""")
    for edus in eduList:
        c = st.container()
        c1,c2 = c.columns([1,3])
        c1.write(edus.getDur())
        c2.write(edus.getCert())
        c2.write(edus.getLoc())
        c2.write("CGPA/Result : "+edus.getCgpa())
        c.markdown("""---""")

with tab4:
    st.subheader("Side Projects")

