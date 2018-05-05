var code={};

console.log('HUFFMAN CODING \n');

var dict = {};
dict['key'] = "blabla";
//console.log(dict);

//emulated get function from python
var getdict = function(object, key, default_value) {
    var result = object[key];
    return (typeof result !== "undefined") ? result : default_value;
}

//building frequency dictionary
var frequency = function(str){
	var freqs = {};
	for (var x =0;x < str.length;x++)
	{	
		var c=str.charAt(x);
		freqs[c]=getdict(freqs,c,0) + 1
	}	   

	return freqs;
};

//convert dict into stack containing elemnts of the form [a,b]
var convert_stack = function(dict){
	var stack = [];
	for (var k in dict)
	{
		stack.push([dict[k],k]);
	}
	return stack;
}

//sort the stack in ascending order
var sort = function(stack){
stack.sort(function compare(a,b){return a[0]-b[0];})
return stack;
}
//building tree
var build_tree = function(sorted){

	while (sorted.length > 1)
	{
		leastTwo = sorted.slice(0,2);
		fre=leastTwo[0][0]+leastTwo[1][0];
		len=sorted.length;
		rest = sorted.slice(2,len);
		rest.push([fre,leastTwo]);
		sorted=sort(rest);
		
	}
	return sorted[0];
}

//trimming tree
var trim_tree = function(tree){

	var p = tree[1];
	if (typeof p == typeof "s")
		{
			return p;
		}
	else
		{
			return [trim_tree(p[0]),trim_tree(p[1])];
	
		}
}
//assign codes to each character in a dict
var assign_codes = function(node,pat=''){
	//var codes = {};
	if(typeof node == typeof "")
		{
		code[node]=pat;
		}
	else{
		assign_codes(node[0],pat.concat('0'));
		assign_codes(node[1],pat.concat('1'));
		}

}

//encoding
var encode = function(text){
//	console.log(text);
	var output="";
	for (k=0;k<text.length;k++)
	{	key=text.charAt(k);

		bit=code[key];

		output=output.concat(bit);
	}

	return output;
}

//decoding

var decode = function(tree,codee){

	var output = "";
	var p = tree;
	for (k=0;k<codee.length;k++){
		bit=codee.charAt(k);
		if (bit=="0"){
			p=p[0];
		}
		else{
			p=p[1];
		}
		if (typeof p == typeof ""){
			output=output.concat(p);
			p=tree;
		}	
	}

return output;
}

tex="aaabccdeeeeeffg";
result=frequency(tex);
console.log(result);

stack=convert_stack(result);
sorted_stack=sort(stack);
ss=build_tree(sorted_stack);
//console.log(ss[1]);
trim=trim_tree(ss);
assign_codes(trim);
encod=encode(tex);
decod=decode(trim,encod);
console.log("encoded text:");
console.log(encod);
console.log("decoded text:");
console.log(decod);
console.log("oroginal text:");
console.log(tex);
