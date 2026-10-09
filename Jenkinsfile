pipeline {
  agent any

  tools {
    nodejs 'NodeJS'
  }

  stages {
    stage('Snyk scan') {
      steps {
        withCredentials([string(credentialsId: 'snyk-token', variable: 'SNYK_TOKEN')]) {
          sh 'npx --yes snyk test'
        }
      }
    }
  }
}
