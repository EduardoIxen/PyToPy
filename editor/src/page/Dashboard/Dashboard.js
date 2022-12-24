import React, { useContext, useState } from "react";
import "react-toastify/dist/ReactToastify.css";
import "codemirror/mode/python/python";
import "codemirror/mode/go/go";
import "codemirror/theme/dracula.css";
import "codemirror/theme/blackboard.css";
import "codemirror/addon/edit/matchbrackets";
import "codemirror/lib/codemirror.css";
import url from "../../config";

import { UnControlled as CodeMirror } from "react-codemirror2";
import { UserContext } from "../../context/UserContext";

import axios from "axios";
import "./setup-codemirror.css";
import Table from "../../components/Table/Table";
import { ToastContainer, toast } from "react-toastify";

export const Dashboard = () => {
  const { inputText, setInputText } = useContext(UserContext);
  const { outputText, setOutputText } = useContext(UserContext);
  const { setErr, err, setSymbols } = useContext(UserContext);

  const [code] = useState(inputText);
  const [outcode, setOutCode] = useState(outputText);

  const notifySuccessful = () => toast("Successful!");
  const notifyError = () => toast("Error!");

  const execute = async () => {
    await axios
      .post(`${url}/compilar`, { entrada: inputText })
      .then((res) => {
 
        if (res.data.err !== "[]") {
          notifyError();
          setErr(res.data.err);
        } else {
          notifySuccessful();
          setErr("");
        }

        setOutCode(res.data.result)
        setSymbols(res.data.symbol);
        
      })
      .catch((err) => {});
  };

  const mirilla = async () => {
    await axios
    .post(`${url}/mirilla`, { input: outputText })
    .then((res) => {
      if (res.data.err !== "[]") {
        notifyError();
        setErr(res.data.err);
      } else {
        notifySuccessful();
        setErr("")
      }
      setOutCode(res.data.result)
    })
    .catch((err) => {});
  }

  const bloque = async () => {
    await axios
    .post(`${url}/bloque`, { input: outputText })
    .then((res) => {
      if (res.data.err !== "[]") {
        notifyError();
        setErr(res.data.err);
      } else {
        notifySuccessful();
        setErr("")
      }
      setOutputText(res.data.result);
    })
    .catch((err) => {});
  }

  const headers = {
    head1: "No.",
    head2: "Descripción",
    head3: "Fila",
    head4: "Columna",
    head5: "Fecha y Hora",
  };

  return (
    <>
      <div className="container-xl">
        <div className="row">
          <div className="position-relative col-s mb-1">
            <button type="button" onClick={execute} className="btn btn-success me-4">
              Compilar
            </button>
            <button type="button" onClick={mirilla} className="btn btn-success">
              Mirilla
            </button>
          </div>
          <div className="col-md-6">
            <CodeMirror
              value={code}
              options={{
                lineNumbers: true,
                mode: "python",
                theme: "dracula",
              }}
              onChange={(editor, data, value) => {
                setInputText(editor.getValue());
              }}
            />
          </div>
          <div className="col-md-6">
            <CodeMirror
              value={outcode}
              options={{
                lineNumbers: true,
                mode: "go",
                theme: "blackboard",
                readOnly: false,
              }}
              onChange={(editor, data, value) => {
                setOutputText(editor.getValue());
              }}
            />
          </div>
        </div>
      </div>
      <div className="modal" id="exampleModal">
        <div className="modal-dialog modal-lg" role="document">
          <div className="modal-content">
            <div className="modal-header">
              <h5 className="modal-title">Errores</h5>
              <button
                type="button"
                className="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              >
                <span aria-hidden="true"></span>
              </button>
            </div>
            <div className="container">
              <div className="row">
                <div className="col-md-12">
                  <Table headers={headers} data={err} />
                </div>
              </div>
            </div>
            <div className="modal-footer"></div>
          </div>
        </div>
      </div>
      <ToastContainer
        position="top-center"
        autoClose={1800}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
      />
    </>
  );
};
