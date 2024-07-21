pipeline {
    parameters {
        // Parametre tanımlaması: node_count parametresi
        choice(name: 'node_count', choices: ['1', '2', '3', '4', '5'], description: 'Select number of nodes')
    }
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Git repo'yu checkout et
                git 'https://github.com/fuat-tirtar/insider.git'
            }
        }
        stage('Build and Test') {
            steps {
                // Docker Compose ile belirtilen sayıda node çalıştır
                script {
                    def count = params.node_count.toInteger()
                    if (count >= 1 && count <= 5) {
                        // Docker Compose ile node sayısını belirtilen sayıya göre ayarla
                        sh "docker-compose up -d --scale chrome-node=${count}"
                        // Testleri çalıştır (örneğin pytest gibi)
                        sh "docker-compose exec chrome-node pytest"
                    } else {
                        error "Invalid node_count parameter. Please choose a value between 1 and 5."
                    }
                }
            }
        }
    }

    post {
        always {
            // Testler bittikten sonra Docker Compose'i kapat
            sh 'docker-compose down'
        }
    }
}
