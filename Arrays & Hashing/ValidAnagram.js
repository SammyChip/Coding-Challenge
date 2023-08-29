var isAnagram = function(s, t) {
    if(s.length != t.length){ //early exit
        return false
    }
    else{
        s = s.split(""); //change to array
        t = t.split("");
        s.sort();
        t.sort();
        for (i=0;i<s.length;i++){
            if(s[i]!= t[i]){
                return false
            }else if (i === s.length-1){
                return true;
            }
        };

    }
    }