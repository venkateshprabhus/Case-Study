import streamlit as st
import requests

api_post_url = "https://2nze9y2sra.execute-api.ap-south-1.amazonaws.com/prod/post"
api_get_url = "https://2nze9y2sra.execute-api.ap-south-1.amazonaws.com/prod/get"

st.title("Compose and Publish Your Post")

Post_text = st.text_area("Write your post and add hashtags (e.g., 'Your post text #hashtag1 #hashtag2'):", height=150)

# Button to post hashtags
if st.button("Publish"):
    if Post_text:
        response = requests.post(api_post_url, json={"Post_text": Post_text})
        st.write(f"Response Status Code: {response.status_code}")
        st.write(f"Response Body: {response.text}")
        if response.status_code == 200:
            st.success("Post published successfully!")
        else:
            st.error("Failed to publish post.")
    else:
        st.error("Text cannot be empty.")

# Button to get trending hashtags
if st.button("Get Trending Hashtags"):
    response = requests.get(api_get_url)
    if response.status_code == 200:
        trending_hashtags = response.json().get('trending_hashtags', [])
        if trending_hashtags:
            st.write("Trending Hashtags:")
            for Hashtag, count in trending_hashtags:
                st.write(f"#{Hashtag} - {count} times")
        else:
            st.write("No trending hashtags.")
    else:
        st.error("Failed to retrieve trending hashtags.")
