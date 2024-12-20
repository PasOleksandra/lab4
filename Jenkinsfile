pipeline {
    options { timestamps() }
    environment {
        DOCKER_CREDS = credentials('tockenn') // Вкажіть ID облікових даних
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
                    image 'python:3.9-alpine' // Уточнений образ
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
                    withCredentials([usernamePassword(credentialsId: 'tockenn', passwordVariable: 'DOCKER_CREDS_PSW', usernameVariable: 'DOCKER_CREDS_USR')]) {
                        sh 'echo $DOCKER_CREDS_PSW | docker login -u $DOCKER_CREDS_USR --password-stdin'
                        sh 'docker build -t your-repo/your-image:latest .'
                        sh 'docker push your-repo/your-image:latest'
                    }
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
