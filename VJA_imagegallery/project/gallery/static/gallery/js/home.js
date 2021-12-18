 $('.carousel').hover(mouseEnter, mouseLeave);
function mouseEnter() {
  
     $(this).carousel({
            interval: 400,
            pause: false
             });
     $(this).carousel('cycle');
};
function mouseLeave() {
   
     $(this).carousel('pause');
};

