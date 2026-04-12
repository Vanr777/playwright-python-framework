pipeline {
    agent {
        // Menggunakan image Docker resmi yang sudah punya Python dan Browser Playwright
        docker {
            image 'mcr.microsoft.com/playwright/python:v1.40.0-jammy'
        }
    }

    stages {
        stage('Checkout Kode') {
            steps {
                // Tahap mengambil kode terbaru dari GitHub
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Menginstall library yang ada di file requirements.txt kamu
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Automation Tests') {
            steps {
                // Menjalankan perintah pytest untuk eksekusi test
                // Kita tambahkan '--headed' atau '--browser' jika diperlukan,
                // tapi biasanya di Jenkins cukup 'pytest' saja (headless mode)
                sh 'pytest'
            }
        }
    }

    post {
        always {
            // Bagian ini akan selalu dijalankan, mau test-nya berhasil atau gagal
            echo 'Proses Automation selesai dijalankan.'
        }
        success {
            echo 'Selamat! Semua test berhasil dilewati.'
        }
        failure {
            echo 'Ada test yang gagal, silakan cek Console Output.'
        }
    }
}