pipeline {
    agent any
    
    environment {
        DOCKER_HOME = '/usr/bin/docker' // Docker'ın PATH'i
        COMPOSE_HOME = '/usr/bin/docker-compose' // Docker Compose'un PATH'i
    }
    
    stages {
        stage('Checkout') {
            steps {
                script {
                    // Git repo'yu belirtilen branch'ten ve credentialId ile clone etme
                    git branch: 'main', credentialsId: 'github-jenkins', url: 'https://github.com/fuat-tirtar/insider.git'
                }
            }
        }
        
        stage('Start Selenium Grid') {
            steps {
                // Docker Compose ile Selenium Grid ve node'larını başlatma
                sh "${COMPOSE_HOME} up -d"
                
                // Selenium Grid'in hazır olup olmadığını kontrol etme
                sh 'sleep 5 && ${COMPOSE_HOME} ps'
            }
        }
        
        stage('Run Selenium Tests') {
            steps {
                // Selenium testlerini Docker konteynerında çalıştırma adımı
                sh "${COMPOSE_HOME} exec selenium-tests pytest -v --html=reports/report.html --self-contained-html tests/"
            }
        }
        
        stage('Send Test Results to Webhook') {
            steps {
                // Test sonuçlarını webhook'a gönderme adımı
                script {
                    def response = sh(script: "curl -X POST -d @reports/report.html https://webhook.site/02eaf3aa-6596-4a62-aef2-0511d7e3bddd", returnStdout: true)
                    echo "Webhook response: ${response}"
                }
            }
        }
    }

    post {
        always {
            // Jenkins işlemlerinin sonunda önce eski imajları sil sonra da Docker konteynerları kapatma adımı
            sh "${DOCKER_HOME} system prune -af"
            sh "${COMPOSE_HOME} down"
        }
    }
}
