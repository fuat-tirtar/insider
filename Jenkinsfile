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
                    docker.image(DOCKER_IMAGE).inside("-e NODE_COUNT=${NODE_COUNT}") {
                        sh 'python -m unittest test_insider.py'
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
            // Docker containers will be cleaned up automatically by Docker's lifecycle management
            // If you need to explicitly clean up containers or volumes, you can do so here
            script {
                // Optional: You may choose to add additional cleanup commands if necessary
            }
        }
    }
}
