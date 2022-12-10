import React, { useContext } from "react";
import Table from "../../components/Table/Table";
import { UserContext } from "../../context/UserContext";

import "./Report.css";

export const Report = () => {
  const { symbols } = useContext(UserContext);

  console.log(symbols)
  const headers = {
    head1: "Nombre",
    head2: "Tipo",
    head3: "Ambito",
    head4: "Fila",
    head5: "Columna",
  };

  return (
    <div className="container">
      <div className="row">
        <h3>Tabla de simbolos</h3>
        <Table headers={headers} data={symbols} />
      </div>
    </div>
  );
};
