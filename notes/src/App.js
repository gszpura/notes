import './App.css';
import React, { useState, useEffect } from 'react';
import axios from 'axios';


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
      await axios.post('http://localhost:8000/notes', { content: newNote });
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
          <div key={note} className="note-box">
            {note}
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;