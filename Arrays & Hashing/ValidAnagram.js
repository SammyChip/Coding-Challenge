var isAnagram = function(s, t) {
    if(s.length != t.length){ //early exit
        return false
    }
    else{
        s = s.split(""); //change to array
        t = t.split("");
        s= s.sort().join("");
        t= t.sort().join("");
        return s === t;
    }
    }