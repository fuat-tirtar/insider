pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'jenkins-github', url: 'https://github.com/fuat-tirtar/insider.git'
            }
        }
        
        stage('Start Selenium Grid') {
            steps {
                // Docker Compose ile Selenium Grid ve node'larını başlatma
                sh 'docker-compose up -d'
                
                // Selenium Grid'in hazır olup olmadığını kontrol etme, örneğin 5 saniye bekleyebiliriz
                sh 'sleep 5 && docker-compose ps'
            }
        }
        
        stage('Run Selenium Tests') {
            steps {
                // Selenium testlerini Docker konteynerında çalıştırma adımı
                sh 'docker-compose exec selenium-tests pytest -v --html=reports/report.html --self-contained-html tests/'
            }
        }
        
        stage('Send Test Results to Webhook') {
            steps {
                // Test sonuçlarını webhook'a gönderme adımı
                script {
                    def response = sh(script: 'curl -X POST -d @reports/report.html https://webhook.site/02eaf3aa-6596-4a62-aef2-0511d7e3bddd', returnStdout: true)
                    echo "Webhook response: ${response}"
                }
            }
        }
    }

    post {
        always {
            // Jenkins işlemlerinin sonunda Docker konteynerları kapatma adımı
            sh 'docker-compose down'
        }
    }
}
