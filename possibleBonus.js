function possibleBonus(a,b){
    ans = 'false';
    if (a < b)
        ans = (b-a <= 6);
    return ans;
}
