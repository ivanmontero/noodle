
// P5.js

var bars = 15;
var nums = [];
var totalLength;
var cline = 1;   // -1 means done
var i = 1, j = 0;
var temp;
var speed = 5;

function setup() {
    var canvas = createCanvas($("#vis").width(), $("#vis").height());
    canvas.parent("vis");
    for(var i = 1; i <= bars; i++) {
        nums.push(i);
    }

    shuffle(nums, true);
    // totalLength = width - width/5;
    totalLength = width - 4;
}

function update() {
    $(".sort-code").css("background-color", "#FFFFFF");
    console.log("refresh " + cline);
    switch(cline){
        case 1: // Simulate for loop
            console.log("1 Entered");
            if( i < nums.length) {
                // cline += 5;
                cline++;
            } else {
                i = -1;
                cline=-1;
            }
            $("#code1").css("background-color", "#FFFF00");
            break;
        case 2:
        // Sets the temp variable.
            temp = nums[i];
            nums[i] = 0;

            cline++;
            $("#code2").css("background-color", "#FFFF00");
            break;
        case 3:
            j = i - 1;

            cline++;
            $("#code3").css("background-color", "#FFFF00");
            break;
        case 4:
            if( j >= 0 && nums[j] > temp) {
                cline++;
            } else {
                cline = 7;
            }
            $("#code4").css("background-color", "#FFFF00");
            break;
        case 5:
            nums[j + 1] = nums[j];
            nums[j] = 0;

            cline++;
            $("#code5").css("background-color", "#FFFF00");
            break;
        case 6:
            j--;

            cline = 4;
            $("#code6").css("background-color", "#FFFF00");
            break;
        case 7:
            nums[j + 1] = temp;

            temp = 0;
            i++;
            cline = 1;
            $("#code7").css("background-color", "#FFFF00");
            break;
    }
    // Line 1
    // for(var i = 0; i < array.length; i++) {
    // Line 2
        // var temp = array[i];
    // Line 3
        // var j = i - 1;
    // Line 4
        // while (j >= 0 && array[j] > temp) {
    // Line 5
            // array[j + 1] = array[j];
    // Line 6
            // j--;
        // }
    // Line 7
        // array[j + 1] = temp;
    // }

    // Code highlighting

    
}

function draw() {
    update();
    fill(255,255,255);
    rect(-5, -5, width + 10, height + 10);
    
    // if (mouseIsPressed) {
    //     fill(0);
    // } else {
    //     fill(255);
    // }
    // ellipse(mouseX, mouseY, 80, 80);
    var initSpace = (width-totalLength )/2;
    var spaceFromBottom = width/5;
    var spaceFromTop = width/2.25;
    var barWidth = totalLength / bars;
    var maxHeight = height - spaceFromBottom - spaceFromTop;
    // temp = nums[3];
    // nums[3] = 0;
    color(0, 0, 0);
    fill(255,255,255);
    for(var x = 0; x < nums.length; x++) {
        var barHeight = maxHeight * (nums[x] / bars);
        if(x == i) fill(0, 255, 0);
        if(x == j) fill(0, 0, 255);
        // var col = 255 * (nums[i] / bars);
        // fill(col, col, col);
        rect(initSpace + x * barWidth, height - spaceFromBottom - barHeight, barWidth, barHeight);
        if(x == i || x == j) noFill();
    }
    if(temp) {
        console.log("this works");
        // var col = 255 * (temp / bars);
        // console.log(col);
        var barHeight = maxHeight * (temp / bars);
        console.log(barHeight);
        // fill(col, col, col);
        fill(255,0,0);
        rect(width/2 - barWidth/2, 0, barWidth, barHeight);
    }
    fill(0,255,0);
    text("i = " + i, 0, height - height/20);
    fill(255,0,0);
    text("temp = " + temp, width/3, height - height/20);
    fill(0,0,255);
    text("j = " + temp, (2*width)/3, height - height/20);
    frameRate(speed);
}

function insertionSort(array) {
  for(var i = 0; i < array.length; i++) {
    var temp = array[i];
    var j = i - 1;
    while (j >= 0 && array[j] > temp) {
      array[j + 1] = array[j];
      j--;
    }
    array[j + 1] = temp;
  }
  return array;
}

// // Function got off the internet
// function shuffle(a) {
//     for (let i = a.length; i; i--) {
//         let j = Math.floor(Math.random() * i);
//         [a[i - 1], a[j]] = [a[j], a[i - 1]];
//     }
// }

function reset() {
    shuffle(nums, true);
    totalLength = width - width/5;

    cline = 1;   // -1 means done
    i = 1;
    j = 0;
}