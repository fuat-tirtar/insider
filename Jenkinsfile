pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'fuattirtar/insider:latest'
        NODE_COUNT = 1
    }

    stages {
        stage('Build') {
            steps {
                git 'https://github.com/fuat-tirtar/insider.git'
                script {
                    // Build Docker image
                    docker.build DOCKER_IMAGE
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run Docker container with tests
                    docker.image(DOCKER_IMAGE).withRun("-e NODE_COUNT=${NODE_COUNT}") {
                        sh 'docker exec -i $(docker ps -q --filter ancestor=${DOCKER_IMAGE}) python -m unittest test_insider.py'
                    }
                }
            }
        }
        stage('Send Test Results to Webhook') {
            steps {
                script {
                    // Example of sending test results to webhook.site
                    def response = httpRequest(
                        contentType: 'APPLICATION_JSON',
                        url: 'https://webhook.site/02eaf3aa-6596-4a62-aef2-0511d7e3bddd',
                        requestBody: '{"status": "Tests Passed"}'
                    )
                    echo "Response from webhook: ${response.status}"
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker containers
            script {
                docker.image(DOCKER_IMAGE).stop()
                docker.image(DOCKER_IMAGE).remove()
            }
        }
    }
}
