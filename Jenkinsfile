pipeline { 
    options { timestamps() }
    environment {
        DOCKER_REGISTRY = 'https://registry-1.docker.io' // Password/Token from Jenkins credentials
    }
    agent none 
    stages {  
        
        stage('Check SCM') {  
            agent any 
            steps { 
                checkout scm 
            } 
        } 

        stage('Build') {  
            steps { 
                echo "Building ... ${BUILD_NUMBER}" 
                echo "Build completed" 
            } 
        } 

        stage('Test') { 
            agent { 
                docker { 
                    image 'python:3.9' 
                    args '-u root' 
                } 
            } 
            steps { 
                sh 'apk add --update python3 py3-pip' 
                sh 'pip install xmlrunner' 
                sh 'pip install -r requirements.txt || echo "No requirements file found"' 
                sh 'python3 test.py'  // запуск тестів
            } 
            post { 
                always { 
                    junit 'test-reports/*.xml' 
                } 
                success { 
                    echo "Application testing successfully completed" 
                } 
                failure { 
                    echo "Oooppss!!! Tests failed!" 
                }  
            } 
        } 
        stage("Publish") {
            agent any
            steps {
                sh 'docker login --username $DOCKER_CREDS_USR --password $DOCKER_CREDS_PSW'
                sh 'docker build -t sashka/notes:latest .'
                sh 'docker push sashka/notes:latest'
            } 
        } // stage Publish
    } // stages
} // pipeline
