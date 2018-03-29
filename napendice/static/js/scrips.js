$(function(){
    var div = $('#mov-header__menu');
    var menuIcon = $('#menu-icon');
    console.log('**************');
    
    menuIcon.on('click',function(){
      //primero menu
      console.log('---------');
      console.log(div);
      div["0"].style.display = 'block';
    });

    div.on('click',function(){
        //primero menu
        div["0"].style.display = 'none';
    });
  }
);