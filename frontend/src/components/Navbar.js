import React from 'react';
import "./Navbar.css"
import {  Link } from "react-router-dom";
const Navbar= () =>{
  return (
		<header class="header">
		<div class="left">
			<a href="#">Home</a>
		</div>
  <div class="mid">
		<ul class="navbar">
			 <li>
      <Link to="/Search">Search</Link>
    </li>
    <li>
      <Link to="/CreateTab">Create</Link>
    </li>
		</ul>
   
  </div>
	<div class="right">
          <a href="#">Welcome</a>
        </div>

    </header>
  );
}
export default Navbar;