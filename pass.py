import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("🔐Password Strength Checker")
st.markdown("""
## welcome to the ultimate password strength checker! 👋👋    
use this simple tool to check the strength of your password and get suggestions on how to make it strong.🔒
we will give you helpful tips to create a **Strong Password** 🔒
""")

password = st.text_input("Enter your Password", type="password")

feedback = []   # Empty veriable to store users feedback
# jb b hum koi big projects bnaen gay to empaty veriable bna k .append() ka use kren gay

score = 0

if password:
    if len(password) >= 8:   # Agar length more then or equal to 8 characters 
        score += 1           # Score +Plus kr rha hai
    else:
        feedback.append("❌Password should be at least 8 characters long.")   # Add in feedback
        

# Use of Rejex here
#  In This line using rejex to add capital and small case letters 
if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
    score += 1
else:
    feedback.append("❌Password should contain both upper and lower case characters.")
    
# Here can check numbers 0-9 (its a rule to check 0-9) when we write   \d 
if re.search(r'\d', password):
    score += 1    # ager score 0-9 k ander ho ga to 1 + (plus) kr le ga
else:
    feedback.append("❌password should contain at least one digit.")
    


if re.search(r'[!@#$%&*]', password):   # Add any one special characterl 
    score += 1
else:
    feedback.append("❌Password should contain at least one special character (!@#$%&*).")
    

if score == 4:
    feedback.append("✅ your password is strong🎉")
    
elif score == 3:
    feedback.append("🟡your password is medium strength. It could be stronger.")
    
else:
    feedback.append("🔴your password is week. Please make it stronger.")
    

if feedback:
    st.markdown("## Improvement Suggestions")
    for tip in feedback:
        st.write(tip)
        
        
else:
    st.info("Please enter your password to get started.")