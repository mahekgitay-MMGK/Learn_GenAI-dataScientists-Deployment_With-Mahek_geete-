"""Simple GenAI billing dashboard. Run with: streamlit run Day_1"""

import importlib

try:
	st = importlib.import_module("streamlit")
except ModuleNotFoundError as exc:
	if exc.name != "streamlit":
		raise
	raise SystemExit("Streamlit is required. Install it with: python -m pip install streamlit") from exc
import pandas as pd

st.set_page_config(page_title="GenAI Billing Dashboard", page_icon="💳", layout="wide")
st.title("💳 GenAI Billing Dashboard")
st.write("Example AI usage and costs")

usage = pd.DataFrame({
	"Model": ["GPT-4o", "Claude 3.5", "Gemini 1.5"],
	"Tokens": [15500, 10200, 12000],
	"Cost ($)": [0.12, 0.09, 0.07],
})

model = st.selectbox("Choose a model", usage["Model"])
selected = usage[usage["Model"] == model]

st.metric("Total cost", f"${selected['Cost ($)'].sum():.2f}")
st.bar_chart(usage.set_index("Model")["Cost ($)"])
st.dataframe(usage, hide_index=True)
st.caption("Sample data only.")
