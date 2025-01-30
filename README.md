# Token Counter App

A Streamlit-based web application that allows users to upload multiple files and analyze them to count the number of tokens using OpenAI's GPT-3.5 tokenizer. This tool is particularly useful for developers and content creators who need to track token usage for GPT model interactions.

URL: https://ct-token-counter.streamlit.app/

## Features

- Multiple file upload support
- Supports various file formats:
  - Text files (.txt)
  - PDF documents (.pdf)
  - CSV files (.csv)
  - JSON files (.json)
  - Python files (.py)
  - JavaScript files (.js)
  - HTML files (.html)
  - CSS files (.css)
  - Markdown files (.md)
- Real-time token counting using OpenAI's official tokenizer
- Interactive data table with results
- Download results as CSV
- Total token count summary
- Error handling for unsupported file types and encodings
- Progress indicator during file processing

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/token-counter-app.git
cd token-counter-app
```

2. Create and activate a virtual environment (recommended):
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Dependencies

The application requires the following Python packages:
- streamlit
- tiktoken
- pandas
- PyPDF2

These can be installed using the included `requirements.txt` file or manually using pip:
```bash
pip install streamlit tiktoken pandas PyPDF2
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided URL (typically http://localhost:8501)

3. Use the file upload interface to select one or more files for analysis

4. View the results in the interactive table

5. Download the results as a CSV file using the download button

## File Processing Details

- Text-based files (txt, csv, json, py, js, html, css, md) are processed using UTF-8 encoding
- PDF files are processed using PyPDF2 for text extraction
- Token counting is performed using OpenAI's `tiktoken` library with the GPT-3.5-turbo encoding
- Files with unsupported encodings or corrupt data will be marked with an error status in the results

## Error Handling

The application handles various error cases:
- Unsupported file types
- Invalid file encodings
- PDF processing errors
- Token counting failures

Each error is captured and displayed in the status column of the results table, allowing for easy identification of problematic files.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Future Improvements

- Add support for more file formats
- Implement batch processing for large files
- Add token cost estimation based on OpenAI's pricing
- Add support for different GPT models and their respective tokenizers
- Implement file content preview
- Add token distribution visualization
- Add support for folder uploads

## Troubleshooting

### Common Issues

1. **File Encoding Errors**
   - Ensure your files are properly encoded (preferably UTF-8)
   - Try converting the file encoding before upload

2. **PDF Processing Issues**
   - Ensure PDFs are not encrypted
   - Check if the PDF contains extractable text
   - For scanned PDFs, OCR processing may be required (not supported in current version)

3. **Performance Issues**
   - Large files may take longer to process
   - Consider splitting very large files into smaller chunks
   - Monitor system memory usage when processing multiple large files

### Getting Help

If you encounter any issues not covered in this documentation:
1. Check the existing issues on the GitHub repository
2. Create a new issue with:
   - Detailed description of the problem
   - Steps to reproduce
   - System information
   - Sample files (if possible)

## Security Considerations

- The application processes files locally and does not send any data to external services
- Token counting is performed using the local tiktoken library
- No file content is stored permanently
- File uploads are processed in memory and temporary files are cleaned up automatically
