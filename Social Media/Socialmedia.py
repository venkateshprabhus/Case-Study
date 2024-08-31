import streamlit as st
import requests
api_post_url = "https://2nze9y2sra.execute-api.ap-south-1.amazonaws.com/prod/post"
api_get_url = "https://2nze9y2sra.execute-api.ap-south-1.amazonaws.com/prod/get"
# Button to compose post
st.title("Compose and Publish Your Post")
Post_text = st.text_area("Write your post", height=150)
if st.button("Publish"):
    if Post_text:
        response = requests.post(api_post_url, json={"Post_text": Post_text})
        if response.ok:
            st.success("Post published successfully!")
        else:
            st.error("Failed to publish post.")
# Button to get trending hashtags
if st.button("Get Trending Hashtags"):
    response = requests.get(api_get_url)
    trending_hashtags = response.json().get('trending_hashtags', [])
    for Hashtag, count in trending_hashtags:
        st.write("Trending Hashtag")
        st.write(f"#{Hashtag} - {count} post")