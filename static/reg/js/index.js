$i('.email').on("change keyup paste",
  function(){
    if($i(this).val()){
      $i('.icon-paper-plane').addClass("next");
    } else {
      $i('.icon-paper-plane').removeClass("next");
    }
  }
);

$i('.next-button').hover(
  function(){
    $i(this).css('cursor', 'pointer');
  }
);

$i('.next-button.email').click(
  function(){
    console.log("Next Button Pressed");
    $i('.email-section').addClass("fold-up");
    $i('.name-section').removeClass("folded");
  }
);

$i('.name').on("change keyup paste",
  function(){
    if($i(this).val()){
      $i('.icon-user').addClass("next");
    } else {
      $i('.icon-user').removeClass("next");
    }
  }
);

$i('.next-button').hover(
  function(){
    $i(this).css('cursor', 'pointer');
  }
);

$i('.next-button.name').click(
  function(){
    console.log("Next Button Pressed");
    $i('.name-section').addClass("fold-up");
    $i('.college-section').removeClass("folded");
  }
);

$i('.college').on("change keyup paste",
  function(){
    if($i(this).val()){
      $i('.icon-building').addClass("next");
    } else {
      $i('.icon-building').removeClass("next");
    }
  }
);

$i('.next-button').hover(
  function(){
    $i(this).css('cursor', 'pointer');
  }
);

$i('.next-button.college').click(
  function(){
    console.log("Next Button Pressed");
    $i('.college-section').addClass("fold-up");
    $i('.number-section').removeClass("folded");
  }
);

$i('.number').on("change keyup paste",
  function(){
    if($i(this).val()){
      $i('.icon-mobile-phone').addClass("next");
    } else {
      $i('.icon-mobile-phone').removeClass("next");
    }
  }
);

$i('.next-button').hover(
  function(){
    $i(this).css('cursor', 'pointer');
  }
);

$i('.next-button.number').click(
  function(){
    console.log("Next Button Pressed");
    $i('.number-section').addClass("fold-up");
    $i('.events-section').removeClass("folded");
  }
);
$i('.events').on("change keyup paste",
  function(){
    if($i(this).val()){
      $i('.icon-trophy').addClass("next");
    } else {
      $i('.icon-trophy').removeClass("next");
    }
  }
);

$i('.next-button').hover(
  function(){
    $i(this).css('cursor', 'pointer');
  }
);

$i('.next-button.events').click(
  function(){
    console.log("Next Button Pressed");
    $i('.events-section').addClass("fold-up");
    $i('.success').css("marginTop", 0);
  }
);
$i("#waves-reg").submit(function(e) {
    e.preventDefault();
});

