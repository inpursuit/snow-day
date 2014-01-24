<?php
  header('Content-type: text/plain');

  $url = htmlspecialchars($_GET["url"]);
  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
  $data = curl_exec($ch);
  curl_close();

  $DOM = new DOMDocument;
  $DOM->loadHTML($data);

  $status = $DOM->getElementById('status');
  if ($status != null) {
    $text = $status->textContent;
    if(strpos($text,'closed') !== false) {
      print("CLOSED");
    } else if(strpos($text,'2 hour') !== false) {
      print("DELAY");
    } else {
      print("OPEN");
    }
  } else {
    print("No status found");
  }
?>
