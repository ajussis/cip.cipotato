
/* Merged Plone Javascript file
 * This file is dynamically assembled from separate parts.
 * Some of these parts have 3rd party licenses or copyright information attached
 * Such information is valid for that section,
 * not for the entire composite file
 * originating files are separated by - filename.js -
 */

/* - carrosel.js - */
$j(document).ready(function() {
	$j('#servicosCarrosel li:last, #divGaleriaVideos li:last, #carroselNoticias li:last').addClass('last');
	
	$j('#servicosCarrosel').jcarousel({'animation':'slow', 'scroll':3 });
	
	$j('.carroselNoticias').jcarousel({'animation':'slow', 'scroll':1 });
	
	$j('#divGaleriaVideos').jcarousel({'vertical': true, 'animation':'slow', 'scroll':4 });
	$j('.divGaleriaCarrossel_h ul').jcarousel({'animation':'slow', 'scroll':1 });
	$j('.divGaleriaCarrossel_h li a:first, #divGaleriaVideos li a:first').trigger('click');	
	$j('.divGaleriaCarrossel_h li a, #divGaleriaVideos li a').click(function(e){
		var obj = $j(this).parents('.divDestMineCarrossel');
		if(obj.length < 1){
			is_mine = false;
			obj = $j(this).parents('.divBoxGalVideo');
		} else {
			is_mine = true;
		}
		
		$j('.divGaleriaCarrossel_h li a, #divGaleriaVideos li a').removeClass('active');
		$j(this).addClass('active');
		/*$j('param[name=movie]',obj).attr('value',$j(this).attr('href'));
		$j('embed',obj).attr('src',$j(this).attr('href'));*/
		width = $j('.divBoxVideo', obj).width();
		height = $j('.divBoxVideo', obj).height();
		$j('.divBoxVideo', obj).html('<object width="'+width+'" height="'+height+'">\
				<param name="movie" value="'+$j(this).attr('href')+'" />\
				<param name="allowFullScreen" value="true" />\
				<param name="allowscriptaccess" value="always" />\
				<embed src="'+$j(this).attr('href')+'" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="'+width+'" height="'+height+'" />\
			</object>');
		if(!is_mine){
			$j('h4', obj).html('<a href="'+$j(this).attr('name')+'">'+$j(this).attr('title')+'</a>');
			$j('p span', obj).html($j(this).attr('rev')+' <a href="'+$j(this).attr('name')+'"><img src="ico/icoMaisAmarelo.gif" width="9" height="9" alt="" class="baixoContraste" /></a>');
		} else {
			$j('p', obj).html('<a href="'+$j(this).attr('name')+'">'+$j(this).attr('title')+'</a>');
			$j('span:not(.spanMais)', obj).html($j(this).attr('rev')+' <a href="'+$j(this).attr('name')+'"><img src="ico/icoMaisAmarelo.gif" width="9" height="9" alt="" class="baixoContraste" /></a>');
		}
		
		e.preventDefault();
	});
	$j('.divGaleriaCarrossel_h li a:first, #divGaleriaVideos li a:first').addClass('active');
	
	$j('.jcarousel-skin-infograficos').jcarousel({'animation':'slow', 'scroll':1 });
	$j('.jcarousel-skin-infograficos .jcarousel-prev, .jcarousel-skin-infograficos .jcarousel-next').hide();
	$j('#btNextInfograficos').click(function(e){
		$j('.jcarousel-skin-infograficos .jcarousel-next').trigger('click');
		if($j('.jcarousel-skin-infograficos .jcarousel-next').hasClass('jcarousel-next-disabled'))
			$j(this).addClass('disable');
		else
			$j(this).removeClass('disable');
		$j('#btPrevInfograficos').removeClass('disable');
		e.preventDefault();
	})
	$j('#btPrevInfograficos').click(function(e){
		$j('.jcarousel-skin-infograficos .jcarousel-prev').trigger('click');
		if($j('.jcarousel-skin-infograficos .jcarousel-prev').hasClass('jcarousel-prev-disabled'))
			$j(this).addClass('disable');
		else
			$j(this).removeClass('disable');
		$j('#btNextInfograficos').removeClass('disable');
		e.preventDefault();
	});
	
	
	$j('.jcarousel-skin-infograficos2').jcarousel({'animation':'slow', 'scroll':1 });
	$j('.jcarousel-skin-infograficos2 .jcarousel-prev, .jcarousel-skin-infograficos2 .jcarousel-next').hide();
	$j('#btNextInfograficos2').click(function(e){
		$j('.jcarousel-skin-infograficos2 .jcarousel-next').trigger('click');
		if($j('.jcarousel-skin-infograficos2 .jcarousel-next').hasClass('jcarousel-next-disabled'))
			$j(this).addClass('disable');
		else
			$j(this).removeClass('disable');
		$j('#btPrevInfograficos2').removeClass('disable');
		e.preventDefault();
	})
	$j('#btPrevInfograficos2').click(function(e){
		$j('.jcarousel-skin-infograficos2 .jcarousel-prev').trigger('click');
		if($j('.jcarousel-skin-infograficos2 .jcarousel-prev').hasClass('jcarousel-prev-disabled'))
			$j(this).addClass('disable');
		else
			$j(this).removeClass('disable');
		$j('#btNextInfograficos2').removeClass('disable');
		e.preventDefault();
	})
	
	
	$j('#totalListagem').text($j('.jcarousel-skin-listagem li').size());
	$j('.jcarousel-skin-listagem').jcarousel({'animation':'slow', 'scroll':1 });
	$j('.jcarousel-skin-listagem .jcarousel-prev, .jcarousel-skin-listagem .jcarousel-next').hide();
	$j('#btNextListagem').click(function(e){
		$j('.jcarousel-skin-listagem .jcarousel-next').trigger('click');
		if($j('.jcarousel-skin-listagem .jcarousel-next').hasClass('jcarousel-next-disabled'))
			$j(this).addClass('disable');
		else
			$j(this).removeClass('disable');
		$j('#btPrevListagem').removeClass('disable');
		e.preventDefault();
	})
	$j('#btPrevListagem').click(function(e){
		$j('.jcarousel-skin-listagem .jcarousel-prev').trigger('click');
		if($j('.jcarousel-skin-listagem .jcarousel-prev').hasClass('jcarousel-prev-disabled'))
			$j(this).addClass('disable');
		else
			$j(this).removeClass('disable');
		$j('#btNextListagem').removeClass('disable');
		e.preventDefault();
	})


	// carrossel - servicos publicos
	jq('#mycarousel').jcarousel({
		vertical: true,
		scroll: 5
	});
	
});


/* - chamada_tv.js - */
$j(document).ready(function(){
	$j('.chamada_tv .mostra_img img, .chamada_tv .mostra_texto div').hide();
	
	$j('.chamada_tv ul li a').click(function(e,auto){
		if($j('li.active a',$j(this).parents('ul')).get(0) === this){
			e.preventDefault();
			return;
		}
		if(!auto){
			var tv = $j(this).parents('.chamada_tv').get(0);
			clearInterval(tv.chamadaTv);
			clearTimeout(tv.chamadaTvAuto);
			tv.chamadaTvAuto = setTimeout(function(){
				tv.chamadaTv = setInterval(tv.chamadaTvInterval,6000);
			},7000);
		}
		$j(this).parents('ul').children('.space').css('display','block');
		$j(this).parents('ul').children('.active').removeClass('active');
		$j(this).parent().prev().css('display','none');
		$j(this).parent().next().css('display','none');
		$j(this).parent().addClass('active');
		
		$j('.mostra_img img:visible',$j(this).parents('.chamada_tv')).fadeOut(1000,function(){
			$j(this).hide();
		});
		
		$j('.mostra_texto div:visible',$j(this).parents('.chamada_tv')).hide();
		
		var imgName = $j(this).attr('href').split('#');
		
		if(imgName && imgName[1])
			if($j('.mostra_img img:visible').length > 0)
				$j('.mostra_img img[name='+imgName[1]+']',$j(this).parents('.chamada_tv')).fadeIn(1000);
			else
				$j('.mostra_img img[name='+imgName[1]+']',$j(this).parents('.chamada_tv')).show();
				
		$j('.mostra_texto .'+imgName[1],$j(this).parents('.chamada_tv')).show();
				
		e.preventDefault();
	});
	
	$j('.chamada_tv').each(function(){
		var tv = this;
		clearInterval(this.chamadaTv);
		clearTimeout(this.chamadaTvAuto);
		this.chamadaTvInterval = function(){
			var pr = $j('ul li.active',tv).nextAll('li[class!=space]').get(0);
			var el = $j('a', pr);
			if(pr)
				el.trigger('click',[true]);
			else
				$j('ul li:first a',tv).trigger('click',[true]);
		};
		this.chamadaTv = setInterval(this.chamadaTvInterval,6000);
	})
		
	$j('.chamada_tv ul li a:first').trigger('click',[true]);
});
