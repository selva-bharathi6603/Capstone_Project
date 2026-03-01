pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "selva6603/python-devops-app"
    }

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/yourusername/yourrepo.git'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-pass', variable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u yourdockerhubusername --password-stdin'
                }
                sh 'docker push $DOCKER_IMAGE'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                ssh ubuntu@<app-server-ip> "
                docker pull $DOCKER_IMAGE &&
                docker stop python-app || true &&
                docker rm python-app || true &&
                docker run -d -p 5000:5000 --name python-app $DOCKER_IMAGE
                "
                '''
            }
        }
    }
}
