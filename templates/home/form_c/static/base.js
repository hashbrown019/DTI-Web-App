
//add input text
// sample edit git
$(document).ready(function(){
$(".hidden-textbox").hide();
$("select#form_interprise").change(function(){
var currentVal = $(this).val();
if(currentVal == "others"){
$(".hidden-textbox").show();
}
else
$(".hidden-textbox").hide();
});  
});


$(document).ready(function(){
$(".hidden-textbox2").hide();
$("select#industry_cluster").change(function(){
var currentVal = $(this).val();
if(currentVal == "pfns"){
$(".hidden-textbox2").show();
}
else
$(".hidden-textbox2").hide();
});  
});

$(document).ready(function(){
$(".hidden-column_18_21").hide();
$("select#type_assistance").change(function(){
var currentVal = $(this).val();
if(currentVal == "product_dev"){
$(".hidden-column_18_21").show();
}
else
$(".hidden-column_18_21").hide();
});  
});


$(document).ready(function(){
$(".hidden-column_9_18").hide();
$("select#type_inv_match").change(function(){
var currentVal = $(this).val();
if(currentVal == "expansion" || currentVal == "productive_investment"){
$(".hidden-column_9_18").show();
}
else
$(".hidden-column_9_18").hide();
});  
});

$(document).ready(function(){
$(".hidden-column_19_26").hide();
$("select#type_inv_match").change(function(){
var currentVal = $(this).val();
if(currentVal == "rehabilitation"){
$(".hidden-column_19_26").show();
}
else
$(".hidden-column_19_26").hide();
});  
});

$(document).ready(function(){
$(".hidden-column_22_28").hide();
$("select#type_assistance").change(function(){
var currentVal = $(this).val();
if(currentVal == "consultancy_serv"){
$(".hidden-column_22_28").show();
}
else
$(".hidden-column_22_28").hide();
});  
});



$(document).ready(function(){
$(".hidden-textbox3").hide();
$("select#no_indigenous_group").change(function(){
var currentVal = $(this).val();
if(currentVal == "yess"){
$(".hidden-textbox3").show();
}
else
$(".hidden-textbox3").hide();
});  
});

$(document).ready(function(){
$(".hidden-textbox4").hide();
$("select#form_interprise").change(function(){
var currentVal = $(this).val();
if(currentVal == "yess1"){
$(".hidden-textbox4").show();
}
else
$(".hidden-textbox4").hide();
});  
});

$(document).ready(function(){
$(".hidden-textbox5").hide();
$("select#pricing").change(function(){
var currentVal = $(this).val();
if(currentVal == "yess2"){
$(".hidden-textbox5").show();
}
else
$(".hidden-textbox5").hide();
});  
});

$(document).ready(function(){
$(".hidden-textbox6").hide();
$("select#quality_raw").change(function(){
var currentVal = $(this).val();
if(currentVal == "yess3"){
$(".hidden-textbox6").show();
}
else
$(".hidden-textbox6").hide();
});  
});

$(document).ready(function(){
$(".hidden-textbox7").hide();
$("select#quality_final_prod").change(function(){
var currentVal = $(this).val();
if(currentVal == "yess4"){
$(".hidden-textbox7").show();
}
else
$(".hidden-textbox7").hide();
});  
});

$(document).ready(function(){
$(".hidden-textbox8").hide();
$("select#existing_comm").change(function(){
var currentVal = $(this).val();
if(currentVal == "yess5"){
$(".hidden-textbox8").show();
}
else
$(".hidden-textbox8").hide();
});  
});

$(document).ready(function(){
$(".hidden-textbox9").hide();
$("select#prov_supp_assis").change(function(){
var currentVal = $(this).val();
if(currentVal == "yess6"){
$(".hidden-textbox9").show();
}
else
$(".hidden-textbox9").hide();
});  
});

$(document).ready(function(){
$(".hidden-textbox10").hide();
$("select#business_prodc3").change(function(){
var currentVal = $(this).val();
if(currentVal == "yess7"){
$(".hidden-textbox10").show();
}
else
$(".hidden-textbox10").hide();
});  
});
$(document).ready(function(){
$(".hidden-textbox11").hide();
$("select#member_following").change(function(){
var currentVal = $(this).val();
if(currentVal == "orgs"){
$(".hidden-textbox11").show();
}
else
$(".hidden-textbox11").hide();
});  
});

$(document).ready(function(){
$(".hidden-textbox12").hide();
$("select#member_livelihood").change(function(){
var currentVal = $(this).val();
if(currentVal == "yess8"){
$(".hidden-textbox12").show();
}
else
$(".hidden-textbox12").hide();
});  
});

$(document).ready(function(){
$(".hidden-textbox13").hide();
$("select#dip_alignment_prod").change(function(){
var currentVal = $(this).val();
if(currentVal == "dipyesprod"){
$(".hidden-textbox13").show();
}
else
$(".hidden-textbox13").hide();
});  
});


$(document).ready(function(){
$(".hidden-textbox14").hide();
$("select#dip_alignment").change(function(){
var currentVal = $(this).val();
if(currentVal == "dipyes"){
$(".hidden-textbox14").show();
}
else
$(".hidden-textbox14").hide();
});  
});

$(document).ready(function(){
$(".hidden-textbox15").hide();
$("select#title_cert").change(function(){
var currentVal = $(this).val();
if(currentVal == "other_specifics"){
$(".hidden-textbox15").show();
}
else
$(".hidden-textbox15").hide();
});  
});


$(document).ready(function(){
$(".hidden-textbox16").hide();
$("select#title_cert2").change(function(){
var currentVal = $(this).val();
if(currentVal == "others_specifics"){
$(".hidden-textbox16").show();
}
else
$(".hidden-textbox16").hide();
});  
});


function myFunction() {
var checkbox1 = document.getElementById("business_reg_check");
var checkbox2 = document.getElementById("product_reg_check");
var checkbox3 = document.getElementById("cert_reg");
var checkbox4 = document.getElementById("lic_op");
var checkbox5 = document.getElementById("iso_cert");
var checkbox6 = document.getElementById("gapgmp_cert");
var checkbox7 = document.getElementById("organic");
var checkbox8 = document.getElementById("halal");
var checkbox9 = document.getElementById("other_cert");
var checkbox10 = document.getElementById("others_specific_products_checkbox");
var textt = document.getElementById("textt");
var textt2 = document.getElementById("textt2");
var textt3 = document.getElementById("textt3");
var textt4 = document.getElementById("textt4");
var textt5= document.getElementById("textt5");
var textt6 = document.getElementById("textt6");
var textt7 = document.getElementById("textt7");
var textt8 = document.getElementById("textt8");
var textt9 = document.getElementById("textt9");
var textt10 = document.getElementById("textt10");
if (checkbox1.checked == true){
textt.style.display = "block";
} else{
textt.style.display = "none";
}
if (checkbox2.checked == true){
textt2.style.display = "block";
} else {
textt2.style.display = "none";
}

if (checkbox3.checked == true){
textt3.style.display = "block";
} else {
textt3.style.display = "none";
}

if (checkbox4.checked == true){
textt4.style.display = "block";
} else {
textt4.style.display = "none";
}

if (checkbox5.checked == true){
textt5.style.display = "block";
} else{
textt5.style.display = "none";
}

if (checkbox5.checked == true){
iso_cert_specific.style.display = "block";
} else{
iso_cert_specific.style.display = "none";
}

if (checkbox6.checked == true){
textt6.style.display = "block";
} else {
textt6.style.display = "none";
}

if (checkbox6.checked == true){
textt6.style.display = "block";
} else {
textt6.style.display = "none";
}

if (checkbox7.checked == true){
textt7.style.display = "block";
} else {
textt7.style.display = "none";
}

if (checkbox8.checked == true){
textt8.style.display = "block";
} else {
textt8.style.display = "none";
}

if (checkbox9.checked == true){
textt9.style.display = "block";
} else {
textt9.style.display = "none";
}
if (checkbox9.checked == true){
other_cert_specify.style.display = "block";
} else {
other_cert_specify.style.display = "none";
}

if (checkbox10.checked == true){
others_specific_products.style.display = "block";
} else{
others_specific_products.style.display = "none";
}





}


//date picker
$(function() {
    $('#datepicker').datepicker();
    $('#datepicker2').datepicker();
    $('#datepicker3').datepicker();
    $('#datepicker4').datepicker();
    $('#datepicker5').datepicker();
    $('#datepicker6').datepicker();
    $('#datepicker7').datepicker();
    $('#datepicker8').datepicker();
    $('#datepicker9').datepicker();
    $('#datepicker10').datepicker();
    $('#datepicker11').datepicker();
    $('#datepicker12').datepicker();
    $('#datepicker13').datepicker();
    $('#datepicker14').datepicker();
    $('#datepicker15').datepicker();
    $('#datepicker16').datepicker();
    $('#datepicker17').datepicker();
    $('#datepicker18').datepicker();
    $('#datepicker19').datepicker();
    $('#datepicker20').datepicker();
    $('#datepicker21').datepicker();
    $('#datepicker22').datepicker();
    $('#datepicker23').datepicker();
    $('#datepicker24').datepicker();
    $('#datepicker25').datepicker();
    $('#datepicker26').datepicker();
    $('#datepicker27').datepicker();
    $('#datepicker28').datepicker();
    $('#datepicker29').datepicker();
});


