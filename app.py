from sklearn import naive_bayes
import streamlit as st 

import joblib
import time


# load Vectorizer For Gender Prediction
imported_vectorizer = open("models/gender_vectorizer.pkl","rb")
cv = joblib.load(imported_vectorizer)

# load Model For Gender Prediction
naive_bayes_model = open("models/gender_classification_model.pkl","rb")
clf = joblib.load(naive_bayes_model)


# Prediction
def gender_prediction(data):
	vect = cv.transform(data).toarray()
	result = clf.predict(vect)
	return result

def main():
	"""Gender Classifier App

	"""

	st.title("Gender Classifier with Streamlit")
	html_temp = """
	<div style="background-color:purple;padding:10px">
	<h2 style="color:white;text-align:center;">Gender Classifaction App </h2>
	</div>

	"""
	st.markdown(html_temp,unsafe_allow_html=True)
	

	name = st.text_input("Enter Person Name")
	if st.button("Predict Gender"):
		result = gender_prediction([name])
		if result[0] == 0:
			prediction = 'Female'
		else:
			result[0] == 1
			prediction = 'Male'
			

		st.success('Name: {} was classified as {}'.format(name.title(),prediction))
	


if __name__ == '__main__':
	main()