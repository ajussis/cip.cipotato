//tab effects
/*
var TabbedContent = {
	init: function() {	
		$(".tab_item").mouseover(function() {
		
			var background = $(this).parent().find(".moving_bg");
			
			$(background).stop().animate({
				left: $(this).position()['left']
			}, {
				duration: 300
			});
			
			TabbedContent.slideContent($(this));
			
		});
	},
	
	slideContent: function(obj) {
		
		var margin = $(obj).parent().parent().find(".slide_content").width();
		margin = margin * ($(obj).prevAll().size() - 1);
		margin = margin * -1;
		
		$(obj).parent().parent().find(".tabslider").stop().animate({
			marginLeft: margin + "px"
		}, {
			duration: 300
		});
	}
}

$(document).ready(function() {
//	TabbedContent.init();




});*/





var $$ = $.fn;

$$.extend({
  SplitID : function()
  {
    return this.attr('id').split('-').pop();
  },

  Slideshow : {
    Ready : function()
    {
       
       $('div.tmpSlideshowControl')
        .hover(
          function() {
            $(this).addClass('tmpSlideshowControlOn');
          }
          ,
          function() {
            $(this).removeClass('tmpSlideshowControlOn');
          }
        )
        .mouseover(
          function() {
            tmpSlided = $('div#tmpSlide-' + $(this).SplitID());
            if (!($(tmpSlided).hasClass('thisnow'))) {
                $('div.tmpSlide').fadeOut();
                $('div.tmpSlide').removeClass('thisnow');
            };

            $('div.tmpSlideshowControl').removeClass('tmpSlideshowControlActive');
            $(tmpSlided).addClass('thisnow');
            $('div#tmpSlide-' + $(this).SplitID()).fadeIn();
            $(this).addClass('tmpSlideshowControlActive');
          }
        );
    }

  }
});

$(document).ready(
  function() {
    $('div#tmpSlide-2').fadeIn();
    $$.Slideshow.Ready();
  }
);
