import React from "react";
import { NavLink } from "react-router-dom";

export const Navbar = () => {
  return (
    <>
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark mb-3">
        <div className="container-fluid">
          <NavLink className="navbar-brand" to="/" activeClassName="active">
            PyToPy
          </NavLink>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon" />
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <NavLink className="nav-link" to="/" activeClassName="active">
                  Home
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/analyze" activeClassName="active">
                  Compilador
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/report" activeClassName="active">
                  Reportes
                </NavLink>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </>
  );
};
