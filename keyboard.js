
var two = document.getElementById("2").style.background;


let log = console.log;
var all = document.querySelectorAll("div");

let pressed = false;

window.addEventListener("keydown",test);
window.addEventListener("keyup",nigg);
function nigg(key){
    console.log(key.keyCode)
    reset()
}
let box = ""
var di = document.getElementById("words").innerHTML ; 
var count = 1;
var minutes;
let texts = ['you','are','it','the','power','doing','certain','therefore','because','over','around','face','do','school'];
var index = 0;



function counter(){
    if(pressed == true){
        document.getElementById("clock").innerHTML=count; //adds timer to html
    minutes = (count/ 60);
    count++;
    console.log(count, minutes)
    if(count==60){
        clearInterval(myTimer)
    }
    }
}
myTimer = setInterval(counter,1000);


let inputArray = [];
let space = 0; //increments for each spacebar press
let typed = 0; //typed words
let error = 0; //errors
var accuracy;
var testx;
function compare(){
    
    if(inputArray[space][space]==randTexts[space]){ 
        typed++;
        document.getElementById("typed").innerHTML = typed;
    } else{
        error++;
        document.getElementById("error").innerHTML = error;
    }
    testx = typed + error;
     g = typed/testx
     accuracy = g * 100; 
    let t = Math.floor(accuracy)
     document.getElementById("accuracy").innerHTML=t +"%";
}
newtexts = [];
var randTexts = [];
function restart(){ // can do if game mode etc
    randTexts = []
    document.getElementById("type-array").value = null;
for(let i = 0; i <= texts.length; i++){
    
    let randomInteger = Math.floor(Math.random() * texts.length);

    randTexts.push(texts[randomInteger]);
}
    wpm = 0;
    count = 0;
    document.getElementById("clock").innerHTML=count;
    
    

    document.getElementById("textarea").value = null;
    document.getElementById("WPM").innerHTML=wpm;
    


}
function typeTest(){
    restart();
    myString = "";
   n =  myString+randTexts;
   k =  n.replaceAll(","," ");
    document.getElementById("type-array").value = k;

}
function test(key){ //when key is pressed

    
    
    
    box+=key.key
    console.log(((box.length)/5));
    document.getElementById("words").innerHTML =  box.length/5;
    pressed = true;
    log(key.keyCode)
    if(key.key!=='Control'){
        if(key.key!=='Alt'){
            if(key.key!=='AltGraph'){
                if(key.key!=='Tab'){
                    if(key.key!=='Shift'){
                        if(key.key!=='Backspace'){
                            if(key.key!=='Escape'){
                                document.getElementById("textarea").value+=key.key;//adds keyboard input to textarea value
                                

                if(count>0){
                    let wpm = Math.floor((document.getElementById("textarea").value.length/5)/minutes); //displays WPM
                    console.log(wpm);
                    document.getElementById("WPM").innerHTML=wpm;
                            }if(document.getElementById("clock").innerHTML==0){
                                document.getElementById("WPM").innerHTML=89;

                            } 
                            {
                                

                            }
                        }
                    }
                }
                
                }
                

            }
        }
        
    } colorPick = document.getElementById("colorPick").value;
    if(key.keyCode=="49"){
       one = document.getElementById("1").style.background = colorPick;
      

    }if(key.keyCode=="50"){
        two = document.getElementById("2").style.background = colorPick;
        

    }
    if(key.keyCode=="51"){
        two = document.getElementById("3").style.background = colorPick;
        

    }
    if(key.keyCode=="52"){
        two = document.getElementById("4").style.background = colorPick;
        

    }
    if(key.keyCode=="53"){
        two = document.getElementById("5").style.background = colorPick;
        

    }
    if(key.keyCode=="54"){
        two = document.getElementById("6").style.background = colorPick;
        

    }
    if(key.keyCode=="55"){
        two = document.getElementById("7").style.background = colorPick;
        

    }
    if(key.keyCode=="56"){
        two = document.getElementById("8").style.background = colorPick;
        

    }
    if(key.keyCode=="57"){
        two = document.getElementById("9").style.background = colorPick;
        

    }
    if(key.keyCode=="48"){
        two = document.getElementById("0").style.background = colorPick;
        

    }
    if(key.keyCode=="187"){
        two = document.getElementById("plus").style.background = colorPick;
        

    }
    if(key.keyCode=="219"){
        two = document.getElementById("slash").style.background = colorPick;
        

    }
    if(key.keyCode=="8"){
        two = document.getElementById("backspace").style.background = colorPick;
        
        
    }
    if(key.keyCode=="9"){
        two = document.getElementById("tab").style.background = colorPick;
        

    }
    if(key.keyCode=="81"){
        two = document.getElementById("q").style.background = colorPick;
        

    }
    if(key.keyCode=="87"){
        two = document.getElementById("w").style.background = colorPick;
        

    }
    if(key.keyCode=="69"){
        two = document.getElementById("e").style.background = colorPick;
        

    }
    if(key.keyCode=="82"){
        two = document.getElementById("r").style.background = colorPick;
        

    }
    if(key.keyCode=="84"){
        two = document.getElementById("t").style.background = colorPick;
        

    }
    if(key.keyCode=="89"){
        two = document.getElementById("y").style.background = colorPick;
        

    }
    if(key.keyCode=="85"){
        two = document.getElementById("u").style.background = colorPick;
        

    }
    if(key.keyCode=="73"){
        two = document.getElementById("i").style.background = colorPick;
        

    }
    if(key.keyCode=="79"){
        two = document.getElementById("o").style.background = colorPick;
        

    }
    if(key.keyCode=="80"){
        two = document.getElementById("p").style.background = colorPick;
        

    }
    if(key.keyCode=="221"){
        two = document.getElementById("å").style.background = colorPick;
        

    }
    if(key.keyCode=="186"){
        two = document.getElementById("up").style.background = colorPick;
        

    }
    if(key.keyCode=="20"){
        two = document.getElementById("caps").style.background = colorPick;
        

    }
    if(key.keyCode=="65"){
        two = document.getElementById("a").style.background = colorPick;
        

    }
    if(key.keyCode=="83"){
        two = document.getElementById("s").style.background = colorPick;
        

    }
    if(key.keyCode=="68"){
        two = document.getElementById("d").style.background = colorPick;
        

    }
    if(key.keyCode=="69"){
        two = document.getElementById("e").style.background = colorPick;
        

    }
    if(key.keyCode=="70"){
        two = document.getElementById("f").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="71"){
        two = document.getElementById("g").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="72"){
        two = document.getElementById("h").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="74"){
        two = document.getElementById("j").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="75"){
        two = document.getElementById("k").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="76"){
        two = document.getElementById("l").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="192"){
        two = document.getElementById("ø").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="222"){
        two = document.getElementById("æ").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="191"){
        two = document.getElementById("*").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="13"){
        two = document.getElementById("enter").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="16"){
        if(key.location==1){
            two = document.getElementById("l-shift").style.background=colorPick;
        }
        if(key.location==2){two = document.getElementById("r-shift").style.background=colorPick;}
        
        
        

    }    
    if(key.keyCode=="226"){
        two = document.getElementById("arrow").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="70"){
        two = document.getElementById("f").style.background=colorPick;
        
        

    }    

    if(key.keyCode=="90"){
        two = document.getElementById("z").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="88"){
        two = document.getElementById("x").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="67"){
        two = document.getElementById("c").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="86"){
        two = document.getElementById("v").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="66"){
        two = document.getElementById("b").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="78"){
        two = document.getElementById("n").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="77"){
        two = document.getElementById("m").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="188"){
        two = document.getElementById("comma").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="190"){
        two = document.getElementById("dot").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="189"){
        two = document.getElementById("-").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="17"){
        two = document.getElementById("l-ctrl").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="91"){
        two = document.getElementById("l-alt").style.background=colorPick;
        
        
        

    }    
    if(key.keyCode=="18"){
        two = document.getElementById("r-alt").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="32"){
        two = document.getElementById("space").style.background=colorPick;
        inputArray.push(document.getElementById("textarea").value.split(/[ ,]+/));
        compare();
        space++;
        
        

    }    
    if(key.keyCode=="88"){
        two = document.getElementById("x").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="18"){
        two = document.getElementById("win").style.background=colorPick;
        
        

    }    
    if(key.keyCode=="88"){
        two = document.getElementById("x").style.background=colorPick;
        
        

    }    

}
function reset(){
   for(let i = 0; i<=all.length;i++){
    all[i].style.background = "white";
   }
    
}
    


