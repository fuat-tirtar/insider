pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'fuattirtar/insider:latest'
        NODE_COUNT = 1
    }

    stages {
        stage('Build') {
            steps {
                // Checkout the source code from GitHub
                git branch: 'main', url: 'https://github.com/fuat-tirtar/insider.git'
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
                    def containerId = docker.image(DOCKER_IMAGE).run('-d -e NODE_COUNT=${NODE_COUNT}')
                    
                    // Get logs for debugging
                    sh "docker logs ${containerId}"
                    
                    // Run tests inside the container
                    sh "docker exec ${containerId} python -m unittest test_insider.py"
                    
                    // Stop and remove the container
                    sh "docker stop ${containerId}"
                    sh "docker rm -f ${containerId}"
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
            // Optional: Clean up Docker containers if needed
            script {
                // Additional cleanup steps if necessary
            }
        }
    }
}
