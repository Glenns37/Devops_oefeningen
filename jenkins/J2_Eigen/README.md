# J2 – Eigen Jenkins Pipeline Experiment

## Doel
Dit experiment demonstreert de structuur van een **Declarative Pipeline** in Jenkins.
In plaats van een echte applicatie te compileren, simuleren we de drie hoofdstappen van software development (**Build, Test, Deploy**) met behulp van simpele Linux shell-commando's.

## Context
* **Type:** Jenkins Declarative Pipeline
* **Taal:** Groovy
* **Agent:** Any (draait op de Jenkins server zelf)

## Het Script
Het pipeline script voert drie fases uit:
1.  **Stage Build:** Maakt een logbestand aan (`build_log.txt`) om het compileren te simuleren.
2.  **Stage Test:** Controleert met `grep` of de "build" geslaagd is (of de tekst bestaat).
3.  **Stage Deploy:** Print een succesbericht als de vorige stappen goed gingen.

## Gebruik (In Jenkins)

### 1. Nieuwe Job Maken
1. Ga naar het Jenkins Dashboard (`http://localhost:8080`).
2. Klik op **New Item**.
3. Naam: `J2-Eigen-Pipeline`.
4. Selecteer **Pipeline** en klik op **OK**.

### 2. Pipeline Configureren
1. Scroll naar beneden naar de sectie **Pipeline**.
2. Zet **Definition** op `Pipeline script`.
3. Plak de volgende code in het vak:

```groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'J2 Experiment: Bezig met compileren...'
                sh 'echo "Dit is de build stap" > build_log.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'J2 Experiment: Automatische tests draaien...'
                sh 'grep "build" build_log.txt' 
            }
        }
        stage('Deploy') {
            steps {
                echo 'J2 Experiment: Uitrollen naar productie!'
                echo 'SUCCESS: Pipeline J2 is geslaagd.'
            }
        }
    }
}
