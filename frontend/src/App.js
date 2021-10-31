import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import Navbar from "./components/Navbar"
import Search from "./pages/Search"
import CreateTab from "./pages/CreateTab"

function App() {
  return (
    <>
      <Router>
      <Navbar />
      <Switch>
        <Route path='/Search' exact component={Search} />
        <Route path='/CreateTab' component={CreateTab} />
      </Switch>
    </Router>

  </>

  );
}
  
export default App;