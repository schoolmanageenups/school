		function check()
 		{
 			//alert("haiii");
			var name=0;
			var expn=/^\D([a-z A-Z]|[0-9])*$/;
			var n=document.formchk.tx1.value;
			if(n=="")
			{
			
                document.getElementById("name").innerHTML="Enter a valid name";
                name=1;
			}
			else if(!expn.test(n))
			{
				document.getElementById("name").innerHTML="Invalid type";
				nme=1;
			}
			else
			{
				document.getElementById("name").innerHTML="";
				nme=0;
			}	
			
			
// 		var ad=0;
// 		var a=document.formchk.txt.value;
// 		if(a=="")
// 		{
// 			document.getElementById("adid").innerHTML="enter address here";
// 			ad=1;

// 		}
		
// 		else
// 		{
// 			document.getElementById("adid").innerHTML="";
// 			ad=0;
// 		}
		
		
// 		var gd=0;
// 		var g=document.formchk.gender.value;
// 		if(g=="")
// 		{
// 			document.getElementById("gnid").innerHTML="choose gender";
// 			gd=1;
// 		}
// 		else
// 		{
// 			document.getElementById("gnid").innerHTML="";
// 			gd=0;
// 		}
// 		var qd=null;
// 		var q = document.getElementsByClassName('cb');

// 		for(var i=0; q[i]; ++i)
// 		{
//       if(q[i].checked)
//       {
//            qd = q[i].value;
//            break;
//       }
// }
// 	if(qd==null)
// 	document.getElementById("qid").innerHTML="select qualification";
// 	else
// 	document.getElementById("qid").innerHTML="";	
// 		var cd=0;
// 		var c=document.formchk.city.value;
// 		if(c=="")
// 			{
// 			document.getElementById("cid").innerHTML="choose city";
// 			cd=1;
// 		}
// 		else
// 		{
// 			document.getElementById("cid").innerHTML="";
// 			cd=0;
// 		}
// 		if(nme==0&&ad==0&&gd==0&&qd==0)
        if(nme==0)
			return true;
		else
			return false;

	}