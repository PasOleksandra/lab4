pipeline { 
    options { timestamps() } 

    agent none 
    stages {  
        stage('Check scm') {  
            agent any 
            steps { 
                checkout scm 
            } 
        } // stage Check scm

        stage('Build') {  
            steps { 
                echo "Building ...${BUILD_NUMBER}" 
                echo "Build completed" 
            } 
        } // stage Build

        stage('Test') { 
            agent { 
                docker { 
                    image 'python:3.12-alpine' 
                    args '-u root' 
                } 
            } 
            steps { 
                sh 'apk add --update python3 py3-pip' 
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
            } // post 
        } // stage Test
    } // stages
}
