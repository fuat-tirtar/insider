pipeline {
    agent any

    parameters {
        string(name: 'BUILD_NAME', defaultValue: 'Build_Name', description: 'Set the build name')
        choice(name: 'NODE_COUNT', choices: '1\n2\n3\n4\n5', description: 'Number of nodes to run tests')
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/fuat-tirtar/insider.git'
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
                    sh 'curl -X POST -d "results=test_results" https://webhook.site/9921afca-86a1-41ca-ac17-a8fe2586d364'
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
