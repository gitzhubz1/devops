pipeline {
  agent {
    docker {
      image 'node:22-alpine'
    }
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
