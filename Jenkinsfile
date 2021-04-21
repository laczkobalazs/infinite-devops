pipeline {
    agent any
    
    environment {
    REGISTRY = '558892180011.dkr.ecr.eu-central-1.amazonaws.com'
    AWS_CREDENTIAL = 'AWS'
    ECR_REPOSITORY = 'infinite-devops-repo'
    ECR_REGION = 'eu-central-1'
    AWS_REGION = 'eu-central-1'
    VERSION = 'latest'
    DOCKERFILE_PATH = './app/'
    BUCKET_NAME = 'infinite-bucket-for-hosting'
  }

    stages {
        stage('Cloning Git') {
            steps {
                git branch: 'development',
                credentialsId: 'jenkins-github',
                url: 'https://github.com/laczkobalazs/infinite-devops'
            }
        }
    
    
    stage('Build') {
      steps {
        sh """
          ls
          docker info
          docker build -t ${ECR_REPOSITORY}:${BUILD_NUMBER} ${DOCKERFILE_PATH}
          docker tag ${ECR_REPOSITORY}:${BUILD_NUMBER} ${REGISTRY}/${ECR_REPOSITORY}:${VERSION}
          docker images
        """

        script {
          docker.withRegistry("https://${REGISTRY}", "ecr:${ECR_REGION}:${AWS_CREDENTIAL}") {
              docker.image("${REGISTRY}/${ECR_REPOSITORY}").push("${VERSION}")
          }
        }
      }
    }
    
    stage('Deploy') {
      steps {
        withAWS(region:"${AWS_REGION}",credentials:"${AWS_CREDENTIAL}") {
            s3Upload(file:'app/static/index.html', bucket:"${BUCKET_NAME}", path:'index.html')
        }
      }
    }
  }
    post {
    success {
      sh "echo \033[32m Successfully built ${ECR_REPOSITORY}:${BUILD_NUMBER} image and pushed to ECR repository. \033[0m"
    }
    failure {
      sh 'echo \033[31m Failed \033[0m'
    }
    }
  
    
}
