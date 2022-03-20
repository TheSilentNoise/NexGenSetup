/*var internship_api_server = "http://0.0.0.0:8889/api/"*/

var internship_api_server = "http://18.144.19.26:8889/api/"

var internhip_details_url =  internship_api_server + "intearn/students/"

var internship_details_url = internship_api_server + "intearn/internship/"

$(document).ready(function () {

    $('#table_id').DataTable();

$("#subs_error").hide();
$("#subs_msg").hide();
$("#feedback-submitted").hide();

/*** email subscription ***/

$("#btnSubscription").click(function(e) {
$("#subs_error").hide();
$("#subs_msg").hide();
        var subs_email = $('#subs_email').val();
        if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(subs_email)){
            $.ajax({
                 url: '/user-email-subscription',
                 data : { subs_email : subs_email },
                 type: 'POST',
                 success: function(response) {
                        console.log(response);
                        if (response == "True"){
                            $('#subs_email').val("");
                            $("#subs_msg").show();
                        }
                    },
                 error: function(error) {
                        console.log(error);
                 }
        });
        }
        else{
            $("#subs_error").show();
        }
});


/**** user course feedback ****/

$("#btn-feedback").click(function(e) {
        var content_rating = $('input[name="content_rating"]:checked').val();
        var overall_rating = $('input[name="overall_rating"]:checked').val();
        var instructor_rating = $('input[name="instructor_rating"]:checked').val();
        var comments =  $('#comments').val();
        var course_id = $('#course_id').val();

        if(!instructor_rating){
        instructor_rating = 0;
        }
        if(!content_rating){
        alert("Please enter your feedback on content!")
        }
        else if(!overall_rating){
        alert("Please enter your feedback on overall course!")
        }
        else{
            $.ajax({
                 url: '/user-course-feedback',
                 data : {
                        content_rating : content_rating,
                        overall_rating : overall_rating,
                        instructor_rating : instructor_rating,
                        comments :  comments,
                        course_id : course_id
                  },
                 type: 'POST',
                 success: function(response) {
                 console.log(response)
                        if(response == 'True'){
                            $('#feedback-form').hide();
                            //alert('Thanks for your feedback');
                            $("#feedback-submitted").show();
                        }
                    },
                 error: function(error) {
                        console.log(error);
                 }
        });
        }
});


}); // end of document.ready()


function viewInternshipApplicants() {
   // document.getElementById("demo").innerHTML = "Hello World";
   var student_id = $("#student_id").val();
  // alert(student_id);
   var settings = {
         "async": true,
         "crossDomain": true,
         "url": internhip_details_url + student_id,
         "method": "GET"
   }

$.ajax(settings).done(function (response) {
    //console.log(response);
    address = response.address +","+ response.city + "," + response.state + "," + response.country
    name = response.first_name + " " + response.surname

    $("#name").html(name);
    $("#email").html(response.email);
    $("#contactno").html(response.contact_no);
    $("#address").html(address);
    $("#gender").html(response.gender);
    $("#dob").html(response.date_of_birth);
    $("#linkedin").html(response.linkedin_url);
    $("#institution").html(response.institution_name);
    $("#qualification").html(response.qualification);
    $("#department").html(response.department);
    $("#yearofpassing").html(response.year_of_passing);
    $("#companyname").html(response.company_name);
    $("#industrytype").html(response.industry_type);
    $("#designation").html(response.designation);
    $("#experience").html(response.experience);
    $("#skills").html(response.skills);


});

}


function viewInternshipOffers() {
   // document.getElementById("demo").innerHTML = "Hello World";
   var fk_internship_id = $("#fk_internship_id").val();
  // alert(student_id);
   var settings = {
         "async": true,
         "crossDomain": true,
         "url": internship_details_url + fk_internship_id,
         "method": "GET"
   }


$.ajax(settings).done(function (response) {

 $("#title").html(response.title);
 $("#paid-type").html(response.paid_type);
 $("#internship-type").html(response.internship_type);
 $("#compensation").html(response.compensation);
 $("#experience").html(response.experience);
 $("#position").html(response.position);
 $("#description").html(response.description);
 $("#skills").html(response.skills);
 $("#qualification").html(response.qualification);
 $("#stream").html(response.stream);
 $("#start-date").html(response.start_date);
 $("#end-date").html(response.end_date);
 $("#last-date").html(response.last_application_date);
 $("#contact-email").html(response.contact_email);
 $("#contact-phone").html(response.contact_no);
 $("#address").html(response.address);
 $("#city").html(response.city);
 $("#state").html(response.state);
 $("#country").html(response.country);


});

}






