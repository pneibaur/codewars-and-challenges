<!-- ------------------------------------------------------- -->
<!-- ------------------------------------------------------- -->
<!-- in this simple assignment you are given a number 
and have to make it negative. 
But maybe the number is already negative? -->

function makeNegative($num) {
    return abs($num) * -1;
}


<!-- ------------------------------------------------------- -->
<!-- ------------------------------------------------------- -->
<!-- You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0. -->

function positive_sum($arr) {
  $sum = 0;
  if (sizeof($arr) > 0){
    foreach ($arr as $i){
      if ($i > 0){
        $sum += $i;
      };
    };
  };
  return $sum;
}