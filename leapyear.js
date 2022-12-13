
function leapyear(year,message){
    
    if (year % 100 === 0 && year % 400 ===0 && year % 4 === 0){
        message = " It's a Leap Year!"
        String(year)
        answer = message
        return swal("Yes",year + answer,"success") }
    
    else if (year % 4 === 0 && year % 100 !== 0  ){
        message = " It's a Leap Year!"
        String(year)
        answer = message
        return swal("Yes!",year + answer,"success")}
    

    else {message = " Not A Leap Year!"
        String(year)
        answer = message
        return swal("No", year + answer, "error")}

    }
    
 
function press(year,message){
    var year = document.getElementById("text1").value
    leapyear(year,message)
}



function userdata(string){
console.log(string.value)
}

