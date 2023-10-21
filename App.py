from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'midiFile' in request.files:
        midi_file = request.files['midiFile']
        if midi_file:
            midi_file_path = 'uploads/temp.mid'
            midi_file.save(midi_file_path)
    
    return 'MIDI file uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)
