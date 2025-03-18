import streamlit as st
import random

# --- Load Custom Styling ---
with open("style.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Import Elegant Google Fonts ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Roboto+Slab:wght@500&display=swap');
    </style>
""", unsafe_allow_html=True)

# --- App Header ---
st.markdown("""
    <h1 class='title'>
        🌱 Nurturing a Growth Mindset 🌱
    </h1>
""", unsafe_allow_html=True)

# --- Introduction to the Experience ---
st.markdown("<p class='info-box'>Welcome to a transformative journey that empowers you to embrace the limitless potential of your mind. This experience is crafted to help you cultivate a growth mindset—the powerful belief that your talents and intelligence can evolve through perseverance and dedication. Let's embark on this journey to unlock your full potential.</p>", unsafe_allow_html=True)

# --- Section: Unveiling the Growth Mindset ---
st.markdown("<h2 class='section-header'>🧠 Discover the Essence of a Growth Mindset</h2>", unsafe_allow_html=True)
st.markdown("<p>A growth mindset is an empowering perspective that encourages you to embrace challenges, persevere in the face of adversity, view effort as the gateway to mastery, learn from constructive feedback, and draw inspiration from the achievements of others.</p>", unsafe_allow_html=True)
st.markdown("<p>In contrast, a fixed mindset limits possibilities, believing that intelligence and talent are unchangeable. Those with a fixed mindset may shy away from challenges and retreat when obstacles arise. It’s time to embrace the growth mindset and elevate your journey.</p>", unsafe_allow_html=True)

# --- Section: Reflection Prompts for a Growth-Oriented Mindset ---
st.markdown("<h2 class='section-header'>💡 Thought-Provoking Prompts for Reflection</h2>", unsafe_allow_html=True)

prompts = [
    "When confronted with a challenge, how do you instinctively react?",
    "Instead of saying 'I can't do this,' try rephrasing it as 'I can't do this... yet.' How does that shift your perspective?",
    "Reflect on a time when you faced difficulty. What valuable lesson did that experience impart to you?",
    "How can you reframe a perceived setback as a golden opportunity to learn and grow?",
    "What small but meaningful step can you take today to edge closer to your aspirations?",
    "How can you embrace the learning process, even when it feels demanding and uncomfortable?",
    "In what area of your life can you challenge yourself to venture into something new this week?",
]

selected_prompt = st.selectbox("Choose a prompt to ponder:", prompts)

if st.button("Reflect and Grow"):
    st.markdown(f"<div class='prompt-container animate__animated animate__fadeIn'><p class='prompt-text'><b>Prompt:</b> {selected_prompt}</p><p>Take a moment to reflect deeply on this prompt and connect it to your own experiences and inner wisdom.</p></div>", unsafe_allow_html=True)

# --- Section: Inviting You to Embrace Challenges ---
st.markdown("<h2 class='section-header'>🚀 Embrace Challenges for Growth</h2>", unsafe_allow_html=True)

challenges = [
    "Learn a new word in a language that excites you.",
    "Attempt a puzzle that stretches your thinking.",
    "Dedicate 15 minutes to practicing a skill you've always wanted to master (e.g., coding, playing an instrument).",
    "Conquer a small task you’ve been procrastinating on and feel the satisfaction of completion.",
    "Reach out to an old friend or acquaintance you’ve lost touch with.",
    "Experiment with a new recipe or craft a dish you’ve never tried before.",
    "Take a peaceful walk and observe your surroundings with fresh eyes, as if seeing them for the first time.",
]

if 'current_challenge' not in st.session_state:
    st.session_state['current_challenge'] = None

if st.button("Get Your Personal Challenge"):
    st.session_state['current_challenge'] = random.choice(challenges)

if st.session_state['current_challenge']:
    st.markdown(f"<div class='prompt-container animate__animated animate__fadeIn'><p class='prompt-text'><b>Your Personalized Challenge:</b> {st.session_state['current_challenge']}</p><p>Take this opportunity to embrace the challenge and discover what you can learn along the way.</p></div>", unsafe_allow_html=True)
    if st.button("Challenge Completed"):
        st.success("Wonderful! You've faced a challenge with courage. Take a moment to reflect on what you learned from the experience.")
        st.session_state['current_challenge'] = None  # Reset the challenge

# --- Section: Tips for Nurturing a Growth Mindset ---
st.markdown("<h2 class='section-header'>🌟 Timeless Tips for Nurturing a Growth Mindset</h2>", unsafe_allow_html=True)
st.markdown("""
<ul>
    <li>Embrace challenges as opportunities for self-growth and transformation.</li>
    <li>Persist through setbacks, knowing they are integral to your personal development.</li>
    <li>Recognize that effort is the key to mastery—your hard work will always yield results.</li>
    <li>Welcome constructive criticism as a tool for refinement and enhancement.</li>
    <li>Celebrate the achievements of others as a source of motivation and inspiration.</li>
</ul>
""", unsafe_allow_html=True)

# --- Section: Enriching Resources for Further Learning ---
st.markdown("<h2 class='section-header'>📚 Curated Resources for Deepening Your Growth Mindset</h2>", unsafe_allow_html=True)
st.markdown("""
<p>Here are some curated resources to further explore and cultivate a growth mindset:</p>
<ul>
    <li><a href="https://www.mindsetworks.com/" target="_blank">Mindset Works - The Foundation of Growth Mindset</a></li>
    <li><a href="https://www.ted.com/talks/carol_s_dweck_the_power_of_believing_that_you_can_improve" target="_blank">Carol Dweck: The Power of Believing That You Can Improve (TED Talk)</a></li>
</ul>
""", unsafe_allow_html=True)

# --- Footer with Aesthetic Closing ---
st.markdown("<div style='text-align: center; margin-top: 30px; color: #777;'>Created by Muhammad Ahmed, powered by Streamlit & Python</div>", unsafe_allow_html=True)
