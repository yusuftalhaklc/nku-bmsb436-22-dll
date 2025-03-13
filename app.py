from doubly_linked_list import DoublyLinkedList
from flask import Flask, render_template, request, redirect, url_for, jsonify
import uuid
import datetime
import random
import string

app = Flask(__name__)

history = []
current_list = DoublyLinkedList()

@app.route('/')
def index():
    return render_template('index.html', 
                          list_data=current_list.to_list(), 
                          history=history,
                          student_info={
                              'name': 'Yusuf Talha Kılıç',
                              'id': '1210606019',
                              'course': 'BMSB436. Python Programlamaya Giriş',
                              'homework': '22. Çift yönlü bir bağlı listeyi (doubly linked list) kopyalayan ve tersine çeviren bir fonksiyon yazın.',
                              'website': 'https://nku-bmsb436-22-dll.yusuftalhaklc.com'
                          })

@app.route('/add_element', methods=['POST'])
def add_element():
    value = request.form.get('value', '')
    if value:
        current_list.append(int(value) if value.isdigit() else value)
        history.append({
            'id': str(uuid.uuid4()),
            'timestamp': datetime.datetime.now().strftime("%H:%M:%S"),
            'operation': 'Ekleme',
            'details': f'"{value}" eklendi'
        })
    
    return jsonify({
        'list_data': current_list.to_list(),
        'history': history
    })

@app.route('/clear_list', methods=['POST'])
def clear_list():
    global current_list
    old_data = current_list.to_list()
    current_list = DoublyLinkedList()
    history.append({
        'id': str(uuid.uuid4()),
        'timestamp': datetime.datetime.now().strftime("%H:%M:%S"),
        'operation': 'Temizleme',
        'details': f'Liste temizlendi: {old_data}'
    })
    
    return jsonify({
        'list_data': current_list.to_list(),
        'history': history
    })

@app.route('/copy_list', methods=['POST'])
def copy_list():
    global current_list
    old_data = current_list.to_list()
    current_list = current_list.copy()
    history.append({
        'id': str(uuid.uuid4()),
        'timestamp': datetime.datetime.now().strftime("%H:%M:%S"),
        'operation': 'Kopyalama',
        'details': f'Liste kopyalandı: {old_data}'
    })
    
    return jsonify({
        'list_data': current_list.to_list(),
        'history': history
    })

@app.route('/reverse_list', methods=['POST'])
def reverse_list():
    global current_list
    old_data = current_list.to_list()
    current_list.reverse()
    new_data = current_list.to_list()  
    history.append({
        'id': str(uuid.uuid4()),
        'timestamp': datetime.datetime.now().strftime("%H:%M:%S"),
        'operation': 'Tersine Çevirme',
        'details': f'Liste tersine çevrildi: {old_data} → {new_data}'
    })
    
    return jsonify({
        'list_data': current_list.to_list(),
        'history': history
    })

@app.route('/copy_and_reverse', methods=['POST'])
def copy_and_reverse():
    global current_list
    old_data = current_list.to_list()
    current_list = current_list.copy_and_reverse()
    new_data = current_list.to_list()  
    history.append({
        'id': str(uuid.uuid4()),
        'timestamp': datetime.datetime.now().strftime("%H:%M:%S"),
        'operation': 'Kopyalama ve Tersine Çevirme',
        'details': f'Liste kopyalandı ve tersine çevrildi: {old_data} → {new_data}'
    })
    
    return jsonify({
        'list_data': current_list.to_list(),
        'history': history
    })

@app.route('/load_example', methods=['POST'])
def load_example():
    global current_list
    length = random.randint(3, 7)
    
    numbers = list(range(1, 101)) 
    letters = list(string.ascii_uppercase) 
    emojis = ["😀", "😁", "😂", "🤣", "😃", "😄", "😅", "😆", "😉", "😊", 
              "🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐨", "🐯",
              "🍎", "🍐", "🍊", "🍋", "🍌", "🍉", "🍇", "🍓", "🍒", "🍑"]
    symbols = ["★", "☆", "✮", "✯", "✰", "⭐", "✪", "✫", "✬", "✭", "✡", "❋", "❊", "❉", "❈", "❇", "❆", "❅", "❄", "❃"]
    
    all_options = numbers + letters + emojis + symbols
    example_data = [random.choice(all_options) for _ in range(length)]
    current_list = DoublyLinkedList().from_list(example_data)
    history.append({
        'id': str(uuid.uuid4()),
        'timestamp': datetime.datetime.now().strftime("%H:%M:%S"),
        'operation': 'Örnek Yükleme',
        'details': f'Rastgele örnek liste yüklendi: {example_data}'
    })
    
    return jsonify({
        'list_data': current_list.to_list(),
        'history': history
    })

@app.route('/clear_history', methods=['POST'])
def clear_history():
    global history
    history = []
    return jsonify({
        'list_data': current_list.to_list(),
        'history': history
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)