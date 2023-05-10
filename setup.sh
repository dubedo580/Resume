mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[theme]\n\
primaryColor = '#C3A38C'\n\
backgroundColor = '#2A3042'\n\
secondaryBackgroundColor = '#C3A38C'\n\
textColor = '#E1E1E1'\n\
" > ~/.streamlit/config.toml