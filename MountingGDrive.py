from google.colab import drive

# @markdown <br><center><img src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Google_Drive_logo.png/600px-Google_Drive_logo.png' height="50" alt="Gdrive-logo"/></center>
# @markdown <center><h3>Mount GDrive to /content/drive</h3></center><br>

drive.mount._DEBUG = False
drive.mount('/content/drive', force_remount=True)
