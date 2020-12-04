<html lang="de">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Linux Defender</title>
    <link rel="stylesheet" href="main.css">
</head>

<body>
<button style="padding: 5px; margin: 2px;" onclick="alert('configure')">Configure</button>
<h1 style="text-align: center; margin-bottom: 70px;">Linux Defender</h1>

<div class="container">
    <div class="row">

        <?php
        $myfile = fopen("status.txt", "r") or die("Unable to open file!");
        $fileR = "";

        while(!feof($myfile)) {
            $fileR = $fileR .fgets($myfile) . "<br>";
        }

        fclose($myfile);
        $rows = explode("<br>",$fileR);
        for ($x = 0; $x < count($rows)-1; $x++) {

            $rowsSplit = explode(",",$rows[$x]);
            echo '<div class="process">
            <div class="box bg-'.$rowsSplit[0] .'"></div>
            <div class="content">
                <h2>'.$rowsSplit[3].'</h2>
                <p>'.$rowsSplit[1]." ".$rowsSplit[2].'</p>
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



