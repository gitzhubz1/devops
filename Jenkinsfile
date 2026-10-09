pipeline {
  agent any

  stages {
    stage('Snyk dependency scan') {
      steps {
        withCredentials([string(credentialsId: 'snyk-token', variable: 'SNYK_TOKEN')]) {
          sh 'npx --yes snyk test'
        }
      }
    }
  }
}
