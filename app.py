import streamlit as st

def main():
    st.header("Welcome to My Streamlit App")
    st.title("Hello, Streamlit!")
    st.write("This is a simple Streamlit app.") 
    name = st.text_input("Enter your name:")
    if name:
        st.write(f"Hello, {name}! Welcome to Streamlit.")

    col1, col2 = st.columns(2, gap="xxsmall")
    with col1:
        st.subheader("Column 1")
        st.write("This is the first column.")
        st.button("Click Me",type="primary", key="btn-1", width="stretch")   
    with col2:
        st.subheader("Column 2")
        st.write("This is the second column.")
        st.button("Click Me",type="primary", key="btn-2", width="stretch")
    
    st.button("Click Me",type="tertiary", key="btn-3",   width="content")

if __name__ == "__main__":
    main()
