UPDATE CLIENTES_TEMP  SET CPF = translate(CPF, '.-/', '')  RETURNING * ;

UPDATE CLIENTES_TEMP  SET LOJA_MAIS_FREQUENTE = translate(LOJA_MAIS_FREQUENTE, '.-/', '') RETURNING * ;

UPDATE CLIENTES_TEMP  SET LOJA_DA_ULTIMA_COMPRA = translate(LOJA_DA_ULTIMA_COMPRA, '.-/', '') RETURNING * ;