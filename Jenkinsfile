pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_HOME = '/usr/local/bin/docker-compose'
    }    
    stages {
        stage('Checkout') {
            steps {
                script {
                    git branch: 'main', credentialsId: 'github-jenkins', url: 'https://github.com/fuat-tirtar/insider.git'
                }
            }
        }
        
        stage('Start Selenium Grid') {
            steps {
                sh "${DOCKER_COMPOSE_HOME} up -d"
                sh 'sleep 5 && ${DOCKER_COMPOSE_HOME} ps'
            }
        }
        
        stage('Run Selenium Tests') {
            steps {
                sh "${DOCKER_COMPOSE_HOME} exec selenium-tests pytest -v --html=reports/report.html --self-contained-html tests/"
            }
        }
        
        stage('Send Test Results to Webhook') {
            steps {
                script {
                    def response = sh(script: "curl -X POST -d @reports/report.html https://webhook.site/02eaf3aa-6596-4a62-aef2-0511d7e3bddd", returnStdout: true)
                    echo "Webhook response: ${response}"
                }
            }
        }
    }

    post {
        always {
            sh "${DOCKER_COMPOSE_HOME} down"
            sh "${DOCKER_COMPOSE_HOME} rm -fsv"
        }
    }
}
