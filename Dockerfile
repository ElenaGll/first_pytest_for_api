FROM python
WORKDIR first_pytest_for_api/
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV=dev
CMD python -m pytest -s --alluredir=test_results/ /first_pytest_for_api/tests/