pipeline {
    agent any

    parameters {
        string(name: 'BUILD_NAME', defaultValue: 'Build_Name', description: 'Set the build name')
        choice(name: 'NODE_COUNT', choices: '1\n2\n3\n4\n5', description: 'Number of nodes to run tests')
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout your VCS repository
                // git 'https://github.com/your-repo/docker-selenium-tests.git'
            }
        }
        
        stage('Build and Test') {
            steps {
                script {
                    def dockerImage = docker.build('selenium-tests')
                    dockerImage.inside {
                        sh 'python run_tests.py --node-count ${params.NODE_COUNT}'
                    }
                }
            }
        }

        stage('Send Test Results') {
            steps {
                script {
                    // Use curl or similar to send test results to webhook.site URL
                    // Example: sh 'curl -X POST -d "results=test_results" https://webhook.site/your-webhook-url'
                }
            }
        }
    }

    post {
        success {
            echo "Build ${BUILD_NAME} succeeded!"
        }
        failure {
            echo "Build ${BUILD_NAME} failed :("
        }
    }
}
