pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "selva6603/capestone-project"
    }

    stages {

        stage('Clone Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/selva-bharathi6603/Capstone_Project'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Login to DockerHub Using Token') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-token',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_TOKEN'
                )]) {
                    sh 'echo $DOCKER_TOKEN | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $DOCKER_IMAGE'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop capestone-container || true
                docker rm capestone-container || true
                docker run -d -p 5000:5000 --name capestone-container $DOCKER_IMAGE
                '''
            }
        }
    }
}
