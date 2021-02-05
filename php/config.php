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
  <script src="../x/html/edit.js" defer></script>
</head>

<body>
  <button style="padding: 5px; margin: 2px;" onclick="location.href='/~supvis/cgi/index.php'">Overview</button>

  <h1 style="text-align: center; margin-bottom: 70px">Linux Defender - Configuration</h1>

  <form action="sucsess.php" method="post">
    <table id="table">
      <thead style="color: #f5f5f5;">
        <tr>
          <th>IP</th>
          <th>Port</th>
          <th>Protokoll</th>
          <th>Intervall</th>
          <th>Argumente</th>
          <th>Bearbeiten</th>
        </tr>
      </thead>
      <tbody id="table">
        <?php
        $myfile = fopen("../x/config.txt", "r") or die("Unable to open file!");
        $fileR = "";

        while (!feof($myfile)) {
          $fileR = $fileR . fgets($myfile) . "<br>";
        }

        $fileR = $fileR . ",,," . "<br>";

        fclose($myfile);

        $rows = explode("<br>", $fileR);
        for ($x = 0; $x < count($rows) - 1; $x++) {
          $rows[$x] = str_replace(" ", "", $rows[$x]);
          $rowsSplit = explode(",", $rows[$x], 6);

          echo '<tr class="row-' . $x . '"> 
        <td class="ip">' . $rowsSplit[0] . '</td>
        <td class="port">' . $rowsSplit[1]. '</td>
        <td class="protocol">' . $rowsSplit[2] . '</td>
        <td class="interval">' . $rowsSplit[3] . '</td>
        <td class="arguments">' . $rowsSplit[4] . '</td>
        <td class="groups">' . $rowsSplit[5] . '</td>

        <td style="text-align: center">
            <a style="cursor: pointer; padding: 0" onclick="edit(' . $x . ')">
                &#9998;
            </a>
        </td>
    </tr>';
        }
        ?>
      </tbody>
    </table>
  </form>

</body>

</html>