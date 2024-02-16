clean: clean_nb clean_ds
clean_nb:
	@rm -rf notebook/outputs
clean_ds:
	@rm -rf dakota-service/inputs
	@rm -rf dakota-service/outputs
notebook: clean_nb
	@mkdir -p notebook/outputs/output_1
	# cd notebook && DY_SIDECAR_PATH_OUTPUTS=./outputs jupyter notebook --no-browser --ip=0.0.0.0 --NotebookApp.token='hello'
	cd notebook && DY_SIDECAR_PATH_OUTPUTS=./outputs jupyter nbconvert --execute --to notebook --inplace UQ.ipynb 
dakota-service: clean_ds
	@mkdir -p dakota-service/inputs/input_2
	@mkdir -p dakota-service/outputs/output_1
	@cp test_data/dakota.in dakota-service/inputs/input_2
	cd dakota-service && DY_SIDECAR_PATH_INPUTS=./inputs DY_SIDECAR_PATH_OUTPUTS=./outputs python main.py
start: dakota-service notebook
