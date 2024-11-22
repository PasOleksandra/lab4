pipeline {
    options { timestamps() }
    environment {
        DOCKER_REGISTRY = 'https://registry-1.docker.io' // Docker Hub registry
        DOCKER_CREDS = credentials('tockenn') // ID облікових даних
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
                    image 'python:3.9-alpine' // Python образ з Alpine
                    args '-u root' 
                } 
            } 
            steps { 
                sh 'pip install xmlrunner' 
                sh 'pip install -r requirements.txt || echo "No requirements file found"' 
                sh 'python3 test.py' // запуск тестів
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
                script {
                    // Логін до Docker Hub
                    sh 'echo $DOCKER_CREDS_PSW | docker login $DOCKER_REGISTRY -u $DOCKER_CREDS_USR --password-stdin'
                    // Створення та публікація Docker образу
                    sh 'docker build -t sashka/notes:latest .'
                    sh 'docker push sashka/notes:latest'
                }
            }
            post {
                always {
                    sh 'docker logout'
                }
            }
        } // stage Publish
    } // stages
} // pipeline
