pipeline {
    options { timestamps() }
    environment {
        DOCKER_CREDS = credentials('tockenn') // Вкажіть ID облікових даних
        DOCKER_CREDS_USR = credentials('tockenn').username
        DOCKER_CREDS_PSW = credentials('tockenn').password
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
                    image 'python:3.9-alpine3.12' // Уточнений образ
                    args '-u root'
                }
            }
            steps {
                sh 'pip install xmlrunner'
                sh 'python3 test.py'
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
                    sh 'echo $DOCKER_CREDS_PSW | docker login -u $DOCKER_CREDS_USR --password-stdin'
                    sh 'docker build -t your-repo/your-image:latest .'
                    sh 'docker push your-repo/your-image:latest'
                }
            }
            post {
                always {
                    sh 'docker logout'
                }
            }
        }
    }
}
