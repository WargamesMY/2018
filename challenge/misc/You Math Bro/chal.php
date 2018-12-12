<?php
date_default_timezone_set('Asia/Kuala_Lumpur');

$flag = "wgmy{d0_you_ev3n_m4th_br0}";

$eq = ['+', '-', 'x'];

print "Welcome to match class.\n";
print "You're required to answer 30 questions within 40 seconds.\n";
print "Type 'start' to start answering.\n\n";

print "> ";
$input = trim(fgets(STDIN));

if ($input == 'start') {
    $start_time = time();

    for ($i = 1; $i <= 30; $i++) {
        $temp_1 = rand(10, 58);
        $temp_2 = rand(9, $temp_1);
        $equat = $eq[ array_rand($eq) ];
        $killer = "";
        if(rand(1,5) == 1) {
            $killer = ';print("y u eval bro");exit();';
        }
        print "Progress [" . $i . "/30] " . $temp_1 . " " . $equat . " " . $temp_2 . "" . $killer . "\n";
        print "Answer > ";
        $answer = trim(fgets(STDIN));
        $now = time();

        if ($now - $start_time > 40) {
            print "You took too long to answer the question!\n";
            exit();
        } else {
            if (evalAnswer($temp_1, $temp_2, $equat) == $answer) {
                print "Correct!\n";
                if ($i >= 30) {
                    print "You're doing good! Here's the prize: \n";
                    print $flag;
                }
            } else {
                print "Wrong answer!\n";
                exit();
            }
        }
    }
}

function evalAnswer($n1, $n2, $eq)
{
    $answer = false;
    switch ($eq) {
        case '+':
            $answer = $n1 + $n2;
            break;

        case '-':
            $answer = $n1 - $n2;
            break;

        case 'x':
            $answer = $n1 * $n2;
            break;
    }
    return $answer;
}
