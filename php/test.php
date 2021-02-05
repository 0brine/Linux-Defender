#!/srv/www/cgi-bin/php
<html lang="de">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <meta http-equiv="X-UA-Compatible" content="ie=edge"/>
    <title>Linux Defender - Config</title>
    <link rel="stylesheet" href="config.css"/>
    <link rel="shortcut icon" type="image/x-icon" href="./ico/favicon.ico"/>
    <link rel="apple-touch-icon"
          sizes="180x180"
          href="./ico/apple-touch-icon.png"/>
    <link rel="icon"
          type="image/png"
          sizes="32x32"
          href="./ico/favicon-32x32.png"/>
    <link rel="icon"
          type="image/png"
          sizes="16x16"
          href="./ico/favicon-16x16.png"/>
    <link rel="manifest" href="./ico/site.webmanifest"/>
</head>

<body>
<button style="padding: 5px; margin: 2px;" onclick="location.href='/~supvis/cgi/index.php'">Overview</button>
<h1 style="text-align: center; margin-bottom: 70px">Linux Defender - Configuration</h1>

<table id="table">
    <thead style="color: #f5f5f5;">
    <tr>
        <th>IP</th>
        <th>Port</th>
        <th>Protocol</th>
        <th>Interval</th>
        <th>Arguments</th>
        <th>Edit</th>
    </tr>
    </thead>
    <tbody id="table">
    <?php
    $myfile = fopen("../status.txt", "r") or die("Unable to open file!");
    $fileR = "";

    while(!feof($myfile)) {
        $fileR = $fileR .fgets($myfile) . "<br>";
    }

    fclose($myfile);
    $rows = explode("<br>",$fileR);
    for ($x = 0; $x < count($rows)-1; $x++) {
        $rows[$x] = str_replace(" ","",$rows[$x]);
        $rowsSplit = explode(",",$rows[$x]);

        echo '<tr class="row-'. $x.'"> 
        <td>'. $rowsSplit[0] .'</td>
        <td>'. $rowsSplit[1] .'</td>
        <td>'. $rowsSplit[2] .'</td>
        <td>'. $rowsSplit[3] .'</td>
        <td>'. $rowsSplit[4] .'</td>
        <td>
            <a style="cursor: pointer; padding: 0" onclick="alert('.$x.')">
                &#9998;
            </a>
        </td>
    </tr>';
    }
    $page = $_SERVER['PHP_SELF'];
    $sec = "4";
    header("Refresh: $sec; url=$page");


    ?>
    </tbody>
</table>


</body>
</html>
