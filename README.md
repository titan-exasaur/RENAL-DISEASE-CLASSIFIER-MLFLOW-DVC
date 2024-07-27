# END-TO-END DEEP LEARNING PROJECT

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py


## Dataset : https://drive.google.com/file/d/1Mg6Gv7-sPl54NUL9Jx4h9_2dI943W4Ii/view?usp=sharing

## MODEL DEPLOYMENT
1. Build docker image for the source code

2. Push the docker image to ECR : 851725241660.dkr.ecr.eu-north-1.amazonaws.com/kidney_disease
stockholm

3. Launch EC2 instance

4. Pull the image from ECR in EC2

5. Launch docker image in EC2

