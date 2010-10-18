// rotator1.js
// for the nifty image thing at the top.
jq(document).ready(
  function(){

// This next line is just to hide some text with JQuery.
    jq("#breadcrumbs-you-are-here").hide();

    jq('.fade1').innerfade({
      speed: 1000,
      timeout: 4000,
      type: 'random_start',
      containerheight: '140px'
      });
    jq('.fade2').innerfade({
      speed: 1000,
      timeout: 3100,
      type: 'random_start',
      containerheight: '140px'
      });
    jq('.fade3').innerfade({
      speed: 1000,
      timeout: 4300,
      type: 'random_start',
      containerheight: '140px'
    });
//    jq('ul#col-1').innerfade({
//       speed: 1500,
//       timeout: 4500,
//       type: 'sequence',
//       containerheight: '138px',
//    });
//    jq('ul#col-2').innerfade({
//       speed: 2000,
//       timeout: 7000,
//       type: 'sequence',
//       containerheight: '138px',
//    });
//    jq('ul#col-3').innerfade({
//       speed: 1000,
//      timeout: 6000,
//       type: 'sequence',
//       containerheight: '138px',
//    });

});