import streamlit as st
import tiktoken
import pandas as pd
from pathlib import Path
import io

st.set_page_config(
    page_title="Token Counter",
    page_icon="🔢",
    layout="wide"
)

def count_tokens(text: str, model: str = "gpt-3.5-turbo") -> int:
    """Count the number of tokens in a text string using the specified model's tokenizer."""
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

def process_file(uploaded_file) -> tuple[str, int, str]:
    """Process an uploaded file and return its details and token count."""
    # Read file content
    if uploaded_file.type == "application/pdf":
        try:
            import PyPDF2
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
            content = ""
            for page in pdf_reader.pages:
                content += page.extract_text()
        except Exception as e:
            return uploaded_file.name, 0, f"Error processing PDF: {str(e)}"
    else:
        try:
            content = uploaded_file.read().decode('utf-8')
        except UnicodeDecodeError:
            return uploaded_file.name, 0, "Error: File encoding not supported"
    
    # Count tokens
    try:
        token_count = count_tokens(content)
        return uploaded_file.name, token_count, "Success"
    except Exception as e:
        return uploaded_file.name, 0, f"Error counting tokens: {str(e)}"

def main():
    st.title("📊 Multi-File Token Counter")
    st.write("Upload multiple files to count tokens using GPT-3.5-turbo tokenizer")
    
    # File uploader
    uploaded_files = st.file_uploader(
        "Choose files to analyze",
        accept_multiple_files=True,
        type=['txt', 'pdf', 'csv', 'json', 'py', 'js', 'html', 'css', 'md']
    )
    
    if uploaded_files:
        # Process files and collect results
        results = []
        total_tokens = 0
        
        with st.spinner('Processing files...'):
            for file in uploaded_files:
                filename, token_count, status = process_file(file)
                results.append({
                    "Filename": filename,
                    "Token Count": token_count,
                    "Status": status
                })
                if status == "Success":
                    total_tokens += token_count
        
        # Display results
        st.subheader("Results")
        
        # Convert results to DataFrame for better display
        df = pd.DataFrame(results)
        st.dataframe(
            df,
            column_config={
                "Filename": st.column_config.TextColumn("Filename", width="medium"),
                "Token Count": st.column_config.NumberColumn("Token Count", format="%d"),
                "Status": st.column_config.TextColumn("Status", width="medium")
            }
        )
        
        # Display total tokens
        st.metric("Total Tokens", f"{total_tokens:,}")
        
        # Download results as CSV
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download Results as CSV",
            data=csv,
            file_name="token_count_results.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    main()