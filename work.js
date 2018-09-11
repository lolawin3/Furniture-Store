function solution(s){
	s = parseFloat(s);
	var money = [100,50,20,10,5,1,0.25,0.10,0.05,0.01];
	var newArr = [0,0,0,0,0,0,0,0,0,0];
	if(s<=0){
		console.log("stuff: "+ newArr);
		return newArr
	}
	money.forEach(function(element,index){
		var count = 0;
		while (s >= money[index]){
			count+=1;
			s -= money[index];
		}
		newArr[index] = count;
	})
	console.log("Answer: "+ newArr);
}

solution(0.61);