 function clicked() {
       if (confirm('Do you wanna to submit?')) {
           yourformelement.submit();
       } else {
           return false;
       }
    }