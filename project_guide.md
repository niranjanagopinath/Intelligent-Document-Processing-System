# Intelligent Document Processing System Completion Steps

This guide outlines the steps to complete the core functionality of your Document Processing System using the libraries already present in `requirements.txt` (`transformers`, `torch`, `spacy`).

## Phase 1: Implement Core AI Services
Create a new file `app/services/ai_processor.py` to handle the intelligent processing logic.

1.  **Initialize Summarization Pipeline**:
    *   Import `pipeline` from `transformers`.
    *   Initialize a summarizer pipeline (e.g., `pipeline("summarization")`).
    *   Create a function `generate_summary(text)` that takes input text and returns a summary.
    *   **Tip**: Handle max length to avoid errors with long documents.

2.  **Initialize Classification Pipeline**:
    *   Initialize a zero-shot classification pipeline (e.g., `pipeline("zero-shot-classification")`).
    *   Create a function `classify_document(text, labels)` where `labels` is a list of categories (e.g., `["invoice", "contract", "report", "resume"]`).
    *   Return the label with the highest score.

## Phase 2: Integrate Services into Main API
Modify `app/main.py` to use the new AI services.

3.  **Import AI Functions**:
    *   Import `generate_summary` and `classify_document` from `app.services.ai_processor`.

4.  **Update Upload Endpoint Logic**:
    *   Inside the `upload_file` function, after extracting text:
        *   Call `generate_summary(text)`.
        *   Call `classify_document(text, ["invoice", "contract", "report"])`.
    *   Store the results in variables (e.g., `summary_text`, `doc_category`).

5.  **Save to Database**:
    *   Update the `models.Document` instantiation to include the new fields:
        ```python
        new_doc = models.Document(
            filename=file.filename,
            content=text,
            summary=summary_text,
            category=doc_category
        )
        ```

## Phase 3: Enhance Text Extraction (Optional but Recommended)
For better accuracy, especially with scanned PDFs or images.

6.  **Add OCR Support**:
    *   If using `pypdf` is insufficient for scanned docs, install `pytesseract` or `easyocr`.
    *   Update `app/services/extractor.py` to fallback to OCR if `pypdf` returns empty text.

## Phase 4: Validating and Testing

7.  **Test with Sample Documents**:
    *   Use Postman or curl to upload different document types (PDFs with text).
    *   Verify in the database that `summary` and `category` fields are populated correctly.

8.  **Performance Optimization**:
    *   Loading models takes time. Load pipelines globally at startup (outside the request function) to avoid reloading them for every request.
