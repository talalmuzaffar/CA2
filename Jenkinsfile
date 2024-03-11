pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository
                git 'https://github.com/talalmuzaffar/CA2'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Navigate to the cloned repository directory
                dir('CA2') {
                    // Install requirements
                    bat 'pip install -r requirements.txt'
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                // Navigate to the cloned repository directory
                dir('CA2') {
                    // Run pytest from test.py
                    bat 'pytest test.py'
                }
            }
        }
    }
}
