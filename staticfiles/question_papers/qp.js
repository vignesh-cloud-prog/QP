// function filtertoggle(){
    // var filters=document.getElementById('filter')
    // var dis=document.getElementsByClassName('fa-filter')
    // if(filters.style.display != 'none'){
        // filters.style.display = 'none';
    // }
    // else{
        // filters.style.display = 'block';
    // }
// }

// function searchtoggle(){
    // var area=document.getElementById('type')
    // var search=document.getElementsByClassName('fa-search')
    // if(area.style.display = 'none'){
        // 
        // area.style.display = 'block';
    // }
    // else{
        // area.style.display = 'none';
        // 
    // }
// }

$('#search').click(function(){
    $('#type').fadeToggle(500);
})

$('#blue').click(function(){
    $('#filter').toggle(1000);
})
$('#short').click(function(){
    $('#filter').toggle(1000);
})
$('#share').click(function(){
    $('#papershare').toggle();
})

