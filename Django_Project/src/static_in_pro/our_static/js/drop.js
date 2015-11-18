		function sel(i)
		{
			var preference='preference_';
			var select='_select';
			var start=preference.concat(i.toString());
			start=start.concat(select);
			return start;
		}

		function tbod(i)
		{
			var preference='preference_';
			var tbody='_tbody'
			var start=preference.concat(i.toString());
			start=start.concat(tbody);
			return start;
		}		
		function showFormInitialize(num)
		{
			for(i=num;i>=0;i--)
			{
				var remove=document.getElementById(sel(i)).value;
				for(j=i+1;j<=16;j++)
				{
					var element=document.getElementById(sel(j));
					for(k=0;k<element.length;k++)
					{
						if(element.options[k].value==remove)
							element.remove(k);
					}
				}
			}

			if(num<=15)
			{
				// alert("tbody");
				document.getElementById(tbod(num+1)).style.display = "block";
				if(num<=14)
				{
					for(i=num+2;i<=16;i++)
					{
						document.getElementById(tbod(i)).style.display = "none";
					}
				}
			}
		}
		function showForm(num)
		{
			//console.log(num);
			var BRANCH='{"BRANCHES":['+
			'{"val":"None","text":"None"},'+
			'{"val":"AE B.Tech","text":"Aerospace Engineering B.Tech"},'+
			'{"val":"CL B.Tech","text":"Chemical Engineering B.Tech"},'+
			'{"val":"CL Dual Deg","text":"Chemical Engineering Dual Degree"},'+
			'{"val":"CH","text":"Chemistry"},'+
			'{"val":"CE B.Tech","text":"Civil Engineering B.Tech"},'+
			'{"val":"CS B.Tech","text":"Computer Science and Engineering B.Tech"},'+
			'{"val":"EE B.Tech","text":"Electrical Engineering B.Tech"},'+
			'{"val":"EE Dual Deg E1","text":"Electrical Engineering Dual Degree E1"},'+
			'{"val":"EE Dual Deg E2","text":"Electrical Engineering Dual Degree E2"},'+
			'{"val":"EN Dual Deg","text":"Energy Science and Engineering Dual Degree"},'+
			'{"val":"EP B.Tech","text":"Engineering Physics B.Tech"},'+
			'{"val":"EP Dual Deg N1","text":"Engineering Physics Dual Degree N1"},'+
			'{"val":"ME B.Tech","text":"Mechanical Engineering B.Tech"},'+
			'{"val":"ME Dual Deg M2","text":"Mechanical Engineering Dual Degree M2"},'+
			'{"val":"MM B.Tech","text":"Metallurgical Engineering B.Tech"},'+
			'{"val":"MM Dual Deg Y1","text":"Metallurgical Engineering Dual Degree Y1"},'+
			'{"val":"MM Dual Deg Y2","text":"Metallurgical Engineering Dual Degree Y2" }]}';
			
			var obj = JSON.parse(BRANCH);
			var str1=document.getElementById(sel(num)).value;
			var str2="None";		
			var flag=str1.localeCompare(str2);
			if(flag!=0)
			{
				for(i=num+1;i<=16;i++)
				{
					var element=document.getElementById(sel(i));
					for(j=element.length-1;j>=0;j--)
					{
						element.remove(j);
					}
					for(j=0;j<=17;j++)
					{
						var opt = document.createElement('option');
						opt.value=obj.BRANCHES[j].val;
						opt.innerHTML=obj.BRANCHES[j].text;
						element.appendChild(opt);
					}
				}

				for(i=num;i>=0;i--)
				{
					var remove=document.getElementById(sel(i)).value;
					for(j=i+1;j<=16;j++)
					{
						var element=document.getElementById(sel(j));
						for(k=0;k<element.length;k++)
						{
							if(element.options[k].value==remove)
								element.remove(k);
						}
					}
				}

				
				if(num<=15)
				{
					// alert("tbody");
					document.getElementById(tbod(num+1)).style.display = "block";
					if(num<=14)
					{
						for(i=num+2;i<=16;i++)
						{
							document.getElementById(tbod(i)).style.display = "none";
						}
					}
				}
				

			}
			else
			{
				for(i=num;i<=16;i++)
				{
					var element=document.getElementById(sel(i));
					for(j=element.length-1;j>=0;j--)
					{
						element.remove(j);
					}
					for(j=0;j<=17;j++)
					{
						var opt = document.createElement('option');
						opt.value=obj.BRANCHES[j].val;
						opt.innerHTML=obj.BRANCHES[j].text;
						element.appendChild(opt);
					}
				}

				for(i=num-1;i>=0;i--)
				{
					var remove=document.getElementById(sel(i)).value;
					for(j=i+1;j<=16;j++)
					{
						var element=document.getElementById(sel(j));
						for(k=0;k<element.length;k++)
						{
							if(element.options[k].value==remove)
								element.remove(k);
						}
					}
				}

				if(num<=15)
				{
					for(j=num+1;j<=16;j++)
					{
						document.getElementById(tbod(j)).style.display="none";
					}
				}
				
			}

		// 	// var selopt = document.getElementById("present_select").value;
		// 	for(i=num+1;i<17;i++){
		// 		// alert(start);
		// 		var sel=document.getElementById(start);
		// 		for (j=0;j<sel.length;  j++) {
		// 		   if (sel.options[j].value==selopt) {
		// 		     sel.remove(j);
		// 		   }
		// 		}
		// 	}
		// var show=preference.concat((num+1).toString());
		// show=show.concat(tbody);
		// documsent.getElementById(show).style.display = "block";
		}

		{% if bool %}	
		window.onload=f;
		{% endif %}

		function f()
			{	
				var i=0;
				while(document.getElementById(sel(i)).value!="None"&&i!=16){
				showFormInitialize(i);
				i++;			
				}
			}