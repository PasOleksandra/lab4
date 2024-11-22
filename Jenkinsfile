pipeline { 
    options { timestamps() }
    environment {
        DOCKER_CREDS = credentials('tockendocker') 
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
                    image 'python:3.9-alpine' 
                    args '-u root' 
                } 
            } 
            steps { 
                sh 'apk add --update python3 py3-pip' 
                sh 'pip install xmlrunner' 
                sh 'pip install -r requirements.txt || echo "No requirements file found"' 
                sh 'python3 test.py' // запуск тестов
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
                sh 'echo $DOCKER_CREDS_PSW | docker login --username $DOCKER_CREDS_USR --password-stdin'
                sh 'docker build -t sashka/notes:latest .'
                sh 'docker push sashka/notes:latest'
                
            } 
        } // stage Publish
    } // stages
} // pipeline
