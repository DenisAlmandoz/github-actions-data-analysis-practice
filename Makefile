install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

test:
	pytest -q

run-notebook:
	papermill notebooks/analysis.ipynb output/analysis-executed.ipynb
