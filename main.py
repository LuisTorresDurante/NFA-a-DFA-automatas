from flask import Flask, render_template, request, jsonify, send_file
from automata.fa.nfa import NFA
from automata.fa.dfa import DFA
import json
import os
import tempfile
from collections import defaultdict

app = Flask(__name__)

def fix_state_names(dfa):
    """Agregar prefijo 'q' a los nombres de estados si son numéricos"""
    # Crear nuevas transiciones con nombres de estados corregidos
    new_transitions = {}
    for state, transitions in dfa.transitions.items():
        new_state = f'q{state}' if str(state).isdigit() else state
        new_transitions[new_state] = {}
        for symbol, target in transitions.items():
            new_transitions[new_state][symbol] = f'q{target}' if str(target).isdigit() else target

    # Crear nuevo DFA con nombres de estados corregidos
    return DFA(
        states={f'q{state}' if str(state).isdigit() else state for state in dfa.states},
        input_symbols=dfa.input_symbols,
        transitions=new_transitions,
        initial_state=f'q{dfa.initial_state}' if str(dfa.initial_state).isdigit() else dfa.initial_state,
        final_states={f'q{state}' if str(state).isdigit() else state for state in dfa.final_states}
    )

def create_transition_table(dfa):
    """Crear una tabla de transiciones formateada desde el DFA"""
    table = defaultdict(dict)
    states = sorted(list(dfa.states))
    symbols = sorted(list(dfa.input_symbols))
    
    # Rellenar transiciones
    for state in states:
        for symbol in symbols:
            if state in dfa.transitions and symbol in dfa.transitions[state]:
                table[state][symbol] = dfa.transitions[state][symbol]
            else:
                table[state][symbol] = '-'
    
    return {
        'headers': symbols,
        'rows': [{
            'state': state,
            'is_initial': state == dfa.initial_state,
            'is_final': state in dfa.final_states,
            'transitions': [table[state][symbol] for symbol in symbols]
        } for state in states]
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        data = request.json
        
        # Crear NFA desde los datos de entrada
        nfa = NFA(
            states=set(data['states']),
            input_symbols=set(data['input_symbols']),
            transitions=data['transitions'],
            initial_state=data['initial_state'],
            final_states=set(data['final_states'])
        )
        
        # Convertir a DFA y corregir nombres de estados
        dfa = DFA.from_nfa(nfa)
        dfa = fix_state_names(dfa)
        
        # Generar diagrama
        temp_dir = tempfile.mkdtemp()
        diagram_path = os.path.join(temp_dir, 'dfa.png')
        dfa.show_diagram(path=diagram_path)
        
        # Crear tabla de transiciones
        table_data = create_transition_table(dfa)
        
        # Leer el archivo de imagen
        with open(diagram_path, 'rb') as f:
            image_data = f.read()
        
        # Limpiar archivos temporales
        os.remove(diagram_path)
        os.rmdir(temp_dir)
        
        return jsonify({
            'success': True,
            'table': table_data,
            'image': image_data.hex()  # Convertir datos binarios a cadena hexadecimal
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)