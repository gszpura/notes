import './App.css';
import React, { useState, useEffect } from 'react';
import axios from 'axios';


interface NoteAddRequest {
  note: string;
}


function App() {
  const [notes, setNotes] = useState([]);
  const [newNote, setNewNote] = useState('');

  useEffect(() => {
    fetchNotes();
  }, []);


  const fetchNotes = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/v1/notes');
      console.error('Received:', response.data.notes);
      setNotes(response.data.notes);
    } catch (error) {
      console.error('Error fetching notes:', error);
    }
  };

  const handleNoteChange = (event) => {
    setNewNote(event.target.value);
  };

  const addNote = async () => {
    try {
      const noteToAdd: NoteAddRequest = { note: newNote };
      await axios.post('http://localhost:8000/api/v1/note', noteToAdd);
      setNewNote('');
      fetchNotes();
    } catch (error) {
      console.error('Error adding note:', error);
    }
  };

  return (
    <div className="App">
      <h1>Notes App</h1>
      <input
        type="text"
        value={newNote}
        onChange={handleNoteChange}
        placeholder="Enter a new note"
      />
      <button onClick={addNote}>Add Note</button>
      <div className="notes-container">
        {notes.map((note) => (
          <div>
              <div key={note.id} className="note-box">
                {note.note}
              </div>
          {note.created_at}
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;