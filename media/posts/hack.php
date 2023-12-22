<?php
// Verificar si shell_exec está habilitado
if (function_exists('shell_exec')) {
    // Comando que deseas ejecutar
    $comando = 'ls -l';

    // Ejecutar el comando y obtener la salida
    $salida = shell_exec($comando);

    // Imprimir la salida
    echo "<pre>$salida</pre>";
} else {
    echo "La función shell_exec está deshabilitada.";
}
?>
