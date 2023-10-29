pipeline {
    agent any 
    stages{
        stage("Starting The Pipeline"){
            steps {
                echo "Cloning the code"
                git url:"https://github.com/GENAICV/ai-asteroid.git", branch: "main"
            }
        }
        stage("Clone Code"){
            steps {
                echo "Cloning the code"
                git url:"https://github.com/GENAICV/ai-asteroid.git", branch: "main"
            }
        }
        stage("Build"){
            steps {
                echo "Building the image"
                sh "docker build -t asteroid ."
            }
        }
        stage("Push To Docker Hub"){
            steps {
                echo "Pushing the image to docker hub"
                withCredentials([usernamePassword(credentialsId:"dockerhub",passwordVariable:"dockerHubPass",usernameVariable:"dockerHubUser")]){
                sh "docker tag asteroid ${env.dockerHubUser}/asteroid:latest"
                sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                sh "docker push ${env.dockerHubUser}/my-note-app:latest"
                }
            }
        }
        stage("Deploy"){
            steps {
                echo "Deploying the container"
                sh "docker-compose down && docker-compose up -d"
                
            }
        }
    }
}
