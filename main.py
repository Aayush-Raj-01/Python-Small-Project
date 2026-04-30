from pprint import pprint

import requests

from config import username, password




$(document).ready(function() {
	$("#submit").click(function(event) { 		
		$("#submit").prop('disabled', true);	
		event.preventDefault();
		var forget_email = $("input#forget_email").val(); 
		if(forget_email == ''){
			$("input#forget_email").addClass("error");			
			$(this).prop('disabled', false);	
			$("input#forget_email").focus(); 
		}else {
			$("input#forget_email").removeClass("error");
			jQuery.ajax({
				type: "POST",
				url: "http://erp.imsec.ac.in/" + "registration/admin_forget",
				dataType: 'json',
				data: {email: forget_email},
				success: function(response){ //console.log(response);
					if(response == '1'){
						alert('Your Reset Password Link is sent to your registered email id.');
						hide_popup();
					}else{
						alert('Invalid User ID.\nPlease contact administrator.');
					}
					$("input#forget_email").val('');			
					$(this).prop('disabled', false);	
				}
			});
		}		
	});
});
 
function show_popup(){
	$("input#forget_email").removeClass("error");
	document.getElementById('popup-forget').style.display = 'block';
	document.getElementById('popup-forget-bg').style.display = 'block';
}

function hide_popup(){
	document.getElementById('popup-forget').style.display = 'none';
	document.getElementById('popup-forget-bg').style.display = 'none';
}

function encrypt(){
	var pass=document.getElementById('password').value;
	if(pass != ""){		   	   
		var hash = sha256_digest(pass);
		var token = sha256_digest(document.getElementById('token').value);
		var enc = sha256_digest(hash.concat(token));
		document.getElementById('password').value= enc;
		return true;
	}
	return false;
}
 



def main():
    url = 'http://erp.imsec.ac.in/'

    with requests.session() as session:
        response = session.post(url, auth=(username, password))
        pprint(response.text)

        with open('index.html', 'w') as f:
            f.write(response.text)
if __name__ == '__main__':
    main()