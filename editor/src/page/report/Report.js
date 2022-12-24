import React, { useContext } from "react";
import Table from "../../components/Table/Table";
import { UserContext } from "../../context/UserContext";

import "./Report.css";

export const Report = () => {
  const { symbols } = useContext(UserContext);
  const { err } = useContext(UserContext);

  console.log(symbols)
  const headers = {
    head1: "Nombre",
    head2: "Tipo",
    head3: "Ambito",
    head4: "Fila",
    head5: "Columna",
  };

  const headers2 = {
    head1: "No.",
    head2: "Descripción",
    head3: "Fila",
    head4: "Columna",
    head5: "Fecha y Hora",
  };

  return (
    <div className="container">
      <div className="row">
        <h3 class="text-white bg-dark">Tabla de simbolos</h3>
        <Table headers={headers} data={symbols} />
      </div>

      <div className="row">
        <h3 class="text-white bg-dark">Tabla de errores</h3>
        <Table headers={headers2} data={err} />
      </div>
    </div>

  );
};
