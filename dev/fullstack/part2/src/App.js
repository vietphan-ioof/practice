import logo from './logo.svg';
import './App.css';

import { useState, useEffect } from 'react'
import axios from 'axios'
import Note from './components/Note'
import notification from './components/notification'
import noteService from './services/notes'

const Footer = () => {
	const footerStyle = {
		color: 'green',
		fontStyle: 'italic',
		fontSize: 16
	}
	return (
		<div style={footerStyle}>
			<br />
			<em> Note app, Department of doo doo, MHI or Mental Health Institute 2069</em>
		</div>
	)
}



const App = () => {
	const [notes, setNotes] = useState([])
	const [newNote, setNewNote] = useState('a new note...')
	const [showAll, setShowAll] = useState(true)
	const [errorMessage, setErrorMessage] = useState('there is some error it seems')

	const hook = () => {
		console.log('effect')
		noteService.getAll().then(initialNotes => {
			setNotes(initialNotes)
		}
	)}

	useEffect(hook, [])

	const addNote = (event) => {
		event.preventDefault()
		const noteObject = {
			content: newNote,
			date: new Date().toISOString(),
			important: Math.random() < 0.5,
		}
		
		noteService.create(noteObject).then(returnedNote => {
			setNotes(notes.concat(returnedNote))
			setNewNote('')
		})


	}

	const toggleImportanceOf = (id) => {
		const url = `http://localhost:3001/notes/${id}`
		const note = notes.find(n=> n.id === id)
		const changedNote = { ...note, important: !note.important}

		noteService.update(id, changedNote).then(returnedNote => {
			setNotes(notes.map(n=> n.id !== id ? n : returnedNote))
		}).catch(error => {setErrorMessage(`Note '${note.content}' was already removed from the server`) 
			setTimeout(() => {
				setErrorMessage(null)
			}, 5000)
			setNotes(notes.filter(n => n.id !== id))
	  })
	}

	const handleNoteChange = (event) => {
		console.log(event.target.value)
		setNewNote(event.target.value)
	}

	const notesToShow = showAll
		? notes
		: notes.filter(note => note.important=== true)

	return (
		<div>
			<h1>Notes</h1>
			<notification message={errorMessage}/>
			<div>
				<button onClick={() => setShowAll(!showAll)}>
					show {showAll ? 'important' : 'all'}
				</button>
			</div>
			<ul>
				{notesToShow.map(note => 
					<Note key={note.id} note={note} toggleImportance={() => toggleImportanceOf(note.id)}/>
			)}
			</ul>
			<form onSubmit={addNote}>
				<input value={newNote} onChange={handleNoteChange}/>
				<button type="submit">save</button>
			</form>
			<Footer />
		</div>
	)
}

export default App
