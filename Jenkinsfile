pipeline {
    agent any
    
    environment {
        DOCKER_HUB_REPO = "vin1989/ml_pipeline:latest"
        CONTAINER_NAME = "mlpipeline"
        
    }
    
    
    
    stages {
        /* We do not need a stage for checkout here since it is done by default when using "Pipeline script from SCM" option. */
        
        stage('Train') {
            steps {
                echo 'Training model..'
                sh 'python train.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing model on test data'
                 sh 'python test_model.py'
                
            }
        }
        stage('Build Image') {
            steps {
                echo 'Building image..'
                
                sh 'docker build -t $DOCKER_HUB_REPO . '
                
                
                
            }
        }
        
        stage('Push Image') {
            steps {
                echo 'Push image..'
                
                withCredentials([usernamePassword(credentialsId: 'dockerhubvin1989', passwordVariable: 'pwd', usernameVariable: 'usr')]) {
                          sh "echo ${pwd} | docker login -u ${usr} --password-stdin"   
                          }
                          
                          sh "docker push $DOCKER_HUB_REPO"
                
                
                
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'docker stop $CONTAINER_NAME || true'
                sh 'docker rm $CONTAINER_NAME || true'
                sh 'docker run -d -it --name $CONTAINER_NAME  -p 5000:5000 $DOCKER_HUB_REPO'
               
            }
        }
    }
}