pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Downloading latest code from GitHub...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building project...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'python3 test.py'
            }
        }

        stage('Deploy') {
    steps {
        echo 'Deploying application...'

        sh '''
        mkdir -p deployed
        cp code1.py deployed/app.py
        '''

        echo 'Application deployed successfully!'
        sh 'ls -l deployed'
    }
}
    }

    post {

        success {
            echo 'Pipeline successful!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}
