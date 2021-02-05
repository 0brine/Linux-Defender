#!/srv/www/cgi-bin/php
<?php
        $page = $_SERVER['PHP_SELF'];
        $sec = "4";
        header("Refresh: $sec; url=$page");
?>
<html lang="de">

<head>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Linux Defender - Overview</title>
    <link rel="stylesheet" href="../x/html/main.css">
    <link rel="shortcut icon" type="image/x-icon" href="../x/html/ico/favicon.ico">
    <link rel="apple-touch-icon" sizes="180x180" href="../x/html/ico/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="../x/html/ico/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="../x/html/ico/favicon-16x16.png">
    <link rel="manifest" href="../x/html/ico/site.webmanifest">

</head>

<body>
<button style="padding: 5px; margin: 2px;" onclick="location.href='/~supvis/cgi/config.php'">Configure</button>
<h1 style="text-align: center; margin-bottom: 70px;">Linux Defender</h1>

<div id="metadata" style="display:none;">
<?php
    /* $logfile = fopen("../x/log.txt", "r") or die("Unable to open file!");
    $loglines = "";

    while(!feof($myfile)) {
        $loglines = $loglines . fgets($logfile) . "<br>";
    }

    fclose($logfile);


    $logrows = explode("<br>",$fileR);
    for ($x = 0; $x < count($logrows)-1; $x++) {
        $logrows[$x] = str_replace(" ","",$logrows[$x]);
        $nameValue = explode(":",$logrows[$x]);
        echo "<div class='$nameValue[0]'>$nameValue[1]</div>";
    } */
?>
</div>

<div class="container">
    <div class="row">

        <?php

        $myfile = fopen("../x/status.txt", "r") or die("Unable to open file!");
        $fileR = "";

        while(!feof($myfile)) {
            $fileR = $fileR .fgets($myfile) . "<br>";
        }

        fclose($myfile);
        $rows = explode("<br>",$fileR);
        for ($x = 0; $x < count($rows)-1; $x++) {
            $rows[$x] = str_replace(" ","",$rows[$x]);
            $rowsSplit = explode(",",$rows[$x]);
            if (count($rowsSplit) <= 1) {
                break;
            }

            echo '<div class="process">
            <div class="box bg-'.$rowsSplit[0] .'"></div>
            <div class="content">
                <h2>'.$rowsSplit[3].'</h2>
                <p>'.$rowsSplit[1].":".$rowsSplit[2].'</p>
            </div>
        </div>';
        }
        ?>

        <!-- Für ungerade Anzahl an Spalten -->
        <div class="process">
        </div>
        <!-- -->
    </div>
</div>
</body>

</html>

