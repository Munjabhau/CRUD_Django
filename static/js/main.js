let typed=new Typed(".auto-type",{
strings:["Create","Retrieve","Update","Delete"],
typeSpeed:150,
backSpeed:150,
loop:true
})

function validate()
{
    let name=document.forms["fn"]["name"].value;
    let age=document.forms['fn']["age"].value;
    let address=document.forms['fn']['address'].value;
    if (name == "")
    {
        document.getElementById("msg1").innerHTML="Name must be filled out";
    }
    if (isNaN(age) || age<1 || age>100)
    {
        document.getElementById("msg2").innerHTML="Please enter valid age";
        return false
    }
    if(address == "")
    {
        document.getElementById("msg3").innerHTML="Address must be filled out";
        return false
    }
}