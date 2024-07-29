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
                    docker.build(DOCKER_IMAGE)
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run Docker container with tests
                    def containerId = docker.image(DOCKER_IMAGE).inside("-e NODE_COUNT=${NODE_COUNT}") {
                        sh 'python -m unittest discover -s tests'
                    }
                    // Check if the container is running
                    def isRunning = sh(script: "docker ps -q --filter ancestor=${DOCKER_IMAGE}", returnStatus: true) == 0
                    if (!isRunning) {
                        error "Docker container is not running."
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
                // Get list of containers that are stopped but might still be lingering
                def containers = sh(script: "docker ps -a -q --filter 'status=exited' --filter 'ancestor=${DOCKER_IMAGE}'", returnStdout: true).trim()
                if (containers) {
                    sh "docker rm -f ${containers}"
                }
            }
        }
    }
}
