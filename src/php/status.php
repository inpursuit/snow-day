<?php
  //ini_set('display_errors', 'On');
  //error_reporting(E_ALL);

  header('Content-type: text/plain');

  $url = htmlspecialchars($_GET["url"]);
  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
  $data = curl_exec($ch);
  curl_close();

  $DOM = new DOMDocument;
  $DOM->loadHTML($data);

  $status = $DOM->getElementById('ContentArea');
  if ($status != null) {
    $bqs = $status->getElementsByTagName('blockquote');
    $bq = $bqs->length > 0 ? $bqs->item(0) : null;
    if($bq != null) {
      $divs = $bq->getElementsByTagName('div');
      $div = $divs->length >= 2 ? $divs->item(1) : null;
      if($div != null) {
        $text = $div->textContent;
        if(strpos($text,'closed') !== false) {
          print("CLOSED");
        } else if(preg_match('/[2|two] hour/i', $text)) {
          print("DELAY");
        } else {
          print("OPEN");
        }
      }
    }
  } else {
    print("ERROR");
  } 
?>
