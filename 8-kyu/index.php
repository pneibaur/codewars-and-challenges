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


<!-- ------------------------------------------------------- -->
<!-- ------------------------------------------------------- -->

<!-- 
    Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the 
missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef'] 
-->

function solution($str) {
    $counter = 0;
    $pairs = array();
    if (strlen($str) % 2 !== 0){
        $str = $str . "_";
        echo "new str: $str";
    }
    for ($i = 0; $i < strlen($str); $i++){
        if ($counter % 2 === 0){
            array_push($pairs, "{$str[$i]}{$str[($i+1)]}");
        };
        $counter += 1;
    };
    return $pairs;
}


<!-- ------------------------------------------------------- -->
<!-- ------------------------------------------------------- -->