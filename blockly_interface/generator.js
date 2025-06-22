Blockly.JavaScript['iniciar'] = function(block) {
  return '// Iniciar\n';
};

Blockly.JavaScript['avanzar'] = function(block) {
  const tiempo = block.getFieldValue('TIEMPO');
  return `avanzar(${tiempo});\n`;
};

Blockly.JavaScript['girar'] = function(block) {
  const direccion = block.getFieldValue('DIRECCION').toLowerCase();
  return `girar("${direccion}");\n`;
};

Blockly.JavaScript['esperar'] = function(block) {
  const tiempo = block.getFieldValue('TIEMPO');
  return `esperar(${tiempo});\n`;
};

Blockly.JavaScript['finalizar'] = function(block) {
  return '// Finalizar\n';
};
