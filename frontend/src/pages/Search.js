import React, { useState, useRef, useEffect } from 'react';


const Search = () =>{
  const [first, second] = useState([])
  const searched = useRef()

  function Add(e) {
    
    const name  = searched.current.value
    if (name === '')return
  }
  function Reset(e){
    searched.current.value = '';

  }
  return (
    <div>
      <h3>Search</h3>
      <div>
      <input ref={searched} type="text" />
      <button onClick={Add}> Search </button>
      <button onClick = {Reset}> Reset </button>
      </div>
    </div>
  );
}
export default Search;