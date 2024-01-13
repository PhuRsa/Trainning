<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
        background-color: rgba(0, 0, 0,0.9);
    }
    .data_crawl {
        border: 1px solid #ccc;
        background-color: grey;
        padding: 10px;
        margin-top: 10px;
    }
    h2,h3{
        color: red;
    }
    </style>
    <title>Crawl Web</title>
</head>
<body>
    <h2>Link Web</h2>
        <form method="POST" >
            <input name="url" id="url" type="text" placeholder="url">
            <button type="submit">Crawl</button>
        </form>
</body>
</html>
<?php 
if(isset($_POST['url'])){
    $url=$_POST['url'];
    $result=shell_exec("timeout 5 curl $url");
    if($result == NULL){
        die("<h2> invalid URL </h2>");
    }
    echo '<div class="data_crawl">' . htmlspecialchars($result) . '</div>';
}else{
    echo "<h2> provide URL <h2>";
}
?>