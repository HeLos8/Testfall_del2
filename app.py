from flask import Flask, render_template #importerar flask och render_template från flaskbiblioteket Flask för att
#skapa webbservern och render_template för HTML-filer

app = Flask(__name__) #skapar en flask-applikation

@app.route('/') #dekorator som visar att det är startsidan som ska trigga den associerade funktionen
def home(): #funktionen som körs när anv går till startsidan
    return render_template('index.html') #visar index.html-filen när man besöker startsidan

if __name__ == '__main__': #gör så att servern kan köras direkt om skriptet körs som huvudprogram
    app.run(debug=True) #aktiverar debug läge
