Blockly.defineBlocksWithJsonArray([
  {
    "type": "iniciar",
    "message0": "Iniciar",
    "nextStatement": null,
    "colour": 230
  },
  {
    "type": "avanzar",
    "message0": "Avanzar %1 ms",
    "args0": [{ "type": "field_number", "name": "TIEMPO", "value": 1000 }],
    "previousStatement": null,
    "nextStatement": null,
    "colour": 120
  },
  {
    "type": "girar",
    "message0": "Girar %1",
    "args0": [{
      "type": "field_dropdown",
      "name": "DIRECCION",
      "options": [["izquierda", "IZQUIERDA"], ["derecha", "DERECHA"]]
    }],
    "previousStatement": null,
    "nextStatement": null,
    "colour": 60
  },
  {
    "type": "esperar",
    "message0": "Esperar %1 ms",
    "args0": [{ "type": "field_number", "name": "TIEMPO", "value": 500 }],
    "previousStatement": null,
    "nextStatement": null,
    "colour": 20
  },
  {
    "type": "finalizar",
    "message0": "Finalizar",
    "previousStatement": null,
    "colour": 290
  }
]);
