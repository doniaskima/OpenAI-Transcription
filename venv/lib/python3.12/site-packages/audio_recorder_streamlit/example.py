import streamlit as st

from audio_recorder_streamlit import audio_recorder

st.subheader("Base audio recorder")
base_audio_bytes = audio_recorder(key="base")
if base_audio_bytes:
    st.audio(base_audio_bytes, format="audio/wav")

st.subheader("Custom recorder")
custom_audio_bytes = audio_recorder(
    text="",
    recording_color="#e8b62c",
    neutral_color="#6aa36f",
    icon_name="user",
    icon_size="6x",
    sample_rate=41_000,
    key="custom",
)
st.text("Click to record")
if custom_audio_bytes:
    st.audio(custom_audio_bytes, format="audio/wav")

st.subheader("Fixed length recorder")
fixed_audio_bytes = audio_recorder(
    energy_threshold=(-1.0, 1.0),
    pause_threshold=3.0,
    key="fixed",
)
st.text("Click to record 3 seconds")
if fixed_audio_bytes:
    st.audio(fixed_audio_bytes, format="audio/wav")
