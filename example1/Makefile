export HDF5_USE_FILE_LOCKING := 'FALSE'

clean: clean_nb clean_ds clean_tools clean_ms clean_zip

clean_zip:
	@rm -rf zipfiles
clean_nb:
	@rm -rf notebook/inputs
	@rm -rf notebook/outputs
clean_ds:
	@rm -rf dakota-service/inputs
	@rm -rf dakota-service/outputs
clean_tools:
	@rm -rf tools
clean_ms:
	@rm -rf map-service
link_io: clean
	@mkdir -p notebook/outputs/output_1
	@mkdir -p notebook/inputs
	@mkdir -p dakota-service/outputs/output_1 
	@mkdir -p dakota-service/outputs/output_2 
	@mkdir -p dakota-service/inputs
	@mkdir -p map-service/outputs/output_1 
	@mkdir -p map-service/inputs
	@ln -rs dakota-service/outputs/output_1 notebook/inputs/input_1	
	@ln -rs notebook/outputs/output_1 dakota-service/inputs/input_2
	@ln -rs dakota-service/outputs/output_2 map-service/inputs/input_2
	@ln -rs map-service/outputs/output_1 dakota-service/inputs/input_3
jupyter: link_io
	@mkdir -p notebook/outputs/output_1
	@mkdir -p notebook/inputs/input_1
	cd notebook && \
	  DY_SIDECAR_PATH_INPUTS=./inputs DY_SIDECAR_PATH_OUTPUTS=./outputs jupyter notebook --no-browser --ip=0.0.0.0 --NotebookApp.token='hello'
notebook: link_io
	cd notebook && \
	  DY_SIDECAR_PATH_INPUTS=./inputs DY_SIDECAR_PATH_OUTPUTS=./outputs jupyter nbconvert --execute --to notebook --inplace UQ.ipynb 
dakota-service: link_io
	@mkdir tools
	cd tools && \
	  wget -q https://raw.githubusercontent.com/wvangeit/osparc-opt/studymap/tools/maps.py
	cd dakota-service && \
	  DY_SIDECAR_PATH_INPUTS=./inputs \
	    DY_SIDECAR_PATH_OUTPUTS=./outputs \
		python main.py
osparc_whl:
	pip install /home/vangeit/src/osparc-studymap/docker_scripts/*.whl
map-service: link_io osparc_whl
	@cp test_data/key_values.json map-service/inputs
	cd map-service && \
	  wget -q https://raw.githubusercontent.com/wvangeit/osparc-studymap/master/docker_scripts/map.py && \
	  OSPARC_API_KEY=`cat ../osparc_api_key.txt` \
	    OSPARC_API_SECRET=`cat ../osparc_api_secret.txt` \
		DY_SIDECAR_PATH_INPUTS=./inputs \
		DY_SIDECAR_PATH_OUTPUTS=./outputs \
		python map.py
zipfiles: clean
	@mkdir zipfiles
	zip -r zipfiles/dakota-service.zip dakota-service
	@cp ../requirements.txt model
	zip -r zipfiles/model.zip model
	@rm model/requirements.txt


start: dakota-service notebook map-service
