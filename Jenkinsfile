pipeline{
    agent any
       environment {
        
         FLASK_APP='hello_flask.py'
         FLASK_ENV='production'
 
       }
    
    stages{
        stage('checkout'){
            steps{
                 withCredentials([string(credentialsId: 'ankygit', variable: 'git')]) {
                 echo "My password is '${git}'!"
                 checkout([$class: 'GitSCM',
                 branches: [[name: 'origin/master']],
                 extensions: [[$class: 'WipeWorkspace']],
                 userRemoteConfigs: [[url: "${git}"]]
                ])
            }
            }
        }
     stage ('dependencies'){
            steps{
              
         sh 'pip install -r requirements.txt'
               
            }
        }
           
        stage ('Testing'){
            steps{
                 sh 'coverage run tests.py'
            }
        }
        
          stage ('Analysis'){
              environment {
                 scannerHome=tool 'sonar scanner'
            }
              steps{
             sh 'coverage html tests.py'

           sh '${scannerHome}/bin/sonar-scanner -Dproject.settings=./sonar-project.properties'
         
              }
          }
          
             stage ('zip')
        {
            steps
            {
                 
                sh 'zip -r nimisha.zip .'
            }
        }
       stage ( 'nexus')
        {
            steps{
                withCredentials([usernamePassword(credentialsId: 'sudipa_nexus', passwordVariable: 'pass', usernameVariable: 'usr')]){
                sh label: '', script: 'curl -u ${usr}:${pass} --upload-file nimisha.zip http://3.14.251.87:8081/nexus/content/repositories/devopstraining/Nimisha-python/nimisha.zip'
            }
            }
        }
          stage ('Deploy'){
      steps{
         sh "JENKINS_NODE_COOKIE=dontKillMe forever start -c python flaskblog.py -a -uid mypyapp1"
       // sh 'python flaskblog.py'
        }
    }
        
    }
}

    
    
    
