// pipeline {
//     agent any
//     environment {
//         DOCKER_IMAGE = "food-app-selenium-tests"
//         TEST_URL = "http://16.171.54.54:3000"
//     }
//     stages {
//         stage('Checkout') {
//             steps {
//                 git url: 'https://github.com/aligee12/food-app-tests.git', branch: 'main'
//             }
//         }
//         stage('Build Docker Image') {
//             steps {
//                 script {
//                     sh 'docker build -t ${DOCKER_IMAGE} .'
//                 }
//             }
//         }
//         stage('Run Tests') {
//             steps {
//                 script {
//                     sh 'docker run --rm -e TEST_URL=${TEST_URL} ${DOCKER_IMAGE}'
//                 }
//             }
//         }
//     }
//     post {
//         always {
//             emailext (
//                 subject: "Jenkins Pipeline Test Results",
//                 body: "Test stage completed. Check Jenkins for details.",
//                 to: "${env.GIT_COMMITTER_EMAIL}",
//                 attachLog: true
//             )
//         }
//     }
// }

pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "food-app-selenium-tests"
        TEST_URL = "http://16.171.54.54:3000"
    }

    stages {
        stage('Checkout') {
            steps {
                // Clean the workspace before checkout
                cleanWs()
                git url: 'https://github.com/aligee12/food-app-tests.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'docker run --rm -e TEST_URL=${TEST_URL} ${DOCKER_IMAGE}'
                }
            }
        }
    }

    post {
        always {
            script {
                // Initialize a variable to hold the committer's email
                def committerEmail = ""

                // Check if there are any changes in the build
                if (currentBuild.changeSets) {
                    // Iterate over the change sets to get the committer's email
                    for (int i = 0; i < currentBuild.changeSets.size(); i++) {
                        def entries = currentBuild.changeSets[i].items
                        for (int j = 0; j < entries.length; j++) {
                            def entry = entries[j]
                            // Set the committer's email from the first change found
                            committerEmail = entry.authorEmail
                            // Break the inner loop once we have the email
                            if (committerEmail) break
                        }
                        // Break the outer loop if we have the email
                        if (committerEmail) break
                    }
                }

                // If no committer email is found from the changelog, send to a default address
                if (!committerEmail) {
                    println "Could not determine committer's email. Sending to a default address."
                    // SET YOUR DEFAULT EMAIL ADDRESS HERE
                    committerEmail = "itzsyed1212@gmail.com"
                }

                // Now, send the email
                emailext (
                    subject: "Jenkins Pipeline: ${currentBuild.fullDisplayName} - ${currentBuild.currentResult}",
                    body: """<p>Check console output at <a href="${env.BUILD_URL}">${env.JOB_NAME} [${env.BUILD_NUMBER}]</a></p>
                           <p><b>Project:</b> ${env.JOB_NAME}</p>
                           <p><b>Build Number:</b> ${env.BUILD_NUMBER}</p>
                           <p><b>Status:</b> ${currentBuild.currentResult}</p>
                           <p>A new build was triggered by a commit.</p>
                           <p><b>Changelog:</b></p>
                           <ul>
                               ${currentBuild.changeSets.collect { it.items.collect { '<li>' + it.msg + ' (' + it.author.fullName + ')</li>' }.join('') }.join('')}
                           </ul>""",
                    to: committerEmail,
                    attachLog: true,
                    mimeType: 'text/html'
                )
            }
        }
    }
}