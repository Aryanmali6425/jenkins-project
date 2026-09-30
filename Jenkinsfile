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

        echo 'Running deployed application...'
        sh 'python3 deployed/app.py'

        echo 'DEPLOYMENT SUCCESSFUL!'
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
