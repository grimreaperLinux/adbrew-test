import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [todos, setTodos] = useState([]);
  const [error, setError] = useState(null);
  const newTodoRef = useRef('');

  // This function is for fetching all the todo items.
  const fetchTodos = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/todos/');
      if (response.status === 200) {
        setTodos(response.data); 
        setError(null);
      } else {
        setError('Error fetching Todos');
      }
    } catch (error) {
      setError('Network error');
    }
  };

  useEffect(() => {
    fetchTodos();
  }, []); 

  // This function is for adding a new todo item.
  const addTodo = async () => {
    const newTodo = newTodoRef.current.value; 

    try {
      const response = await axios.post('http://127.0.0.1:8000/todos/', {
        todo: newTodo
      });

      if (response.status === 201) {
        setTodos([...todos, newTodo]);
        newTodoRef.current.value = ''; 
        window.alert('Todo added successfully!'); 
        setError(null);
      } else {
        setError('Error adding todo');
      }
    } catch (error) {
      setError('Network error');
    }
  };

  return (
    <div style={{"display": "flex","justify-content":"center","align-items":"center","flex-direction":"column"}}>
      <div>
        <h1>List of TODOs</h1>
        {error ? (
          <p>Error: {error}</p> 
        ) : todos.length === 0 ? (
          <p>No items to display.</p>
        ) : (
          <ul>
            {todos.map((todo, index) => (
              <li key={index}>{todo}</li>
            ))}
          </ul>
        )}
      </div>
      <div>
        <h1>Create a ToDo</h1>
        <form>
          <div>
            <label htmlFor="todo">ToDo: </label>
            <input
              type="text"
              ref={newTodoRef} 
            />
          </div>
          <div style={{ "marginTop": "5px","display": "flex","justify-content": "center"}}>
            <button type="button" onClick={addTodo}>
              Add ToDo!
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default App;