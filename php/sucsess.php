#!/srv/www/cgi-bin/php
<html lang="de">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="X-UA-Compatible" content="ie=edge" />
  <title>Linux Defender - Config</title>
  <link rel="stylesheet" href="../x/html/config.css">
  <link rel="shortcut icon" type="image/x-icon" href="../x/html/ico/favicon.ico">
  <link rel="apple-touch-icon" sizes="180x180" href="../x/html/ico/apple-touch-icon.png">
  <link rel="icon" type="image/png" sizes="32x32" href="../x/html/ico/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="../x/html/ico/favicon-16x16.png">
  <link rel="manifest" href="../x/html/ico/site.webmanifest">
</head>

<body>
  <?php
  $row = $_POST["row"];
  $ip = $_POST["ip"];
  $port = $_POST["port"];
  $protocol = $_POST["protocol"];
  $interval = $_POST["interval"];
  $arguments = $_POST["arguments"];

  $myfile = fopen("../x/config.txt", "r") or die("Unable to open file!");
  $lines = array();

  while (!feof($myfile)) {
    array_push($lines, fgets($myfile));
  }

  fclose($myfile);

  if (count($lines) <= $row) {
    $lines[$row] = "\n" . $ip . "," . $port . "," . $protocol . "," . $interval . "," . $arguments;
  } else if (count($lines) - 1 == $row){
    $lines[$row] = $ip . "," . $port . "," . $protocol . "," . $interval . "," . $arguments;
  } else {
    $lines[$row] = $ip . "," . $port . "," . $protocol . "," . $interval . "," . $arguments . "\n";
  }


  $myfile = fopen("../x/config.txt", "w") or die("Unable to open file!");

  foreach ($lines as $line) {
    fwrite($myfile, $line);
  }

  fclose($myfile);

  echo("<script>location.href = 'config.php'</script>")
  ?>

</body>
</html>