# Django PDF to DOC and DOC to PDF Converter

This Django project allows users to convert PDF files to DOC and DOC files to PDF.

## Features

- Convert PDF to DOC
- Convert DOC to PDF

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.x
- Django
- pdf2docx
- python-docx
- fpdf

Install the required packages using the following command:

```bash
pip install -r requirements.txt
```

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/kavinandan18/pdf_converter.git
    ```

2. Change to the project directory:

    ```bash
    cd django-multiple-apps
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

Usage

    Convert PDF to DOC:
        Visit http://127.0.0.1:8000/converter/pdf-to-doc/
        Upload a PDF file and click "Convert."

    Convert DOC to PDF:
        Visit http://127.0.0.1:8000/converter/doc-to-pdf/
        Upload a DOC file and click "Convert."

    View Conversion Result:
        After conversion, you'll be redirected to a result page with a download link.

Contributing

If you'd like to contribute to the project, please follow these steps:

    Fork the repository.
    Create a new branch for your feature/bug fix.
    Make your changes.
    Submit a pull request.

### License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/kavinandan18/pdf_converter/blob/master/LICENSE) file for details.

