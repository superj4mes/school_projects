function sortelements(event){
    let opt = this.options[this.selectedIndex]
    let datatype = opt.value
    let sorttype = opt.getAttribute('data-sorttype')
    sort(datatype,sorttype)
}

function sort(datatype, sorttype){
    var body = document.getElementById('sortbody');
    var divs = [];
    let elemsforsort= []; 
    let attr = "";
    if(datatype === "date"){
        attr = "data-time";
    }
    else if(datatype === 'str'){
        attr= 'data-str';
    }
    elems = document.querySelectorAll('[' + attr + ']');
    for(let i=0; i<elems.length; ++i){
        if(datatype === 'date'){ 
            elemsforsort.push({container:elems[i], date:new Date(elems[i].getAttribute(attr))});
        }
        else if(datatype === 'str'){ 
            elemsforsort.push({container:elems[i].closest(".sortparent"), str:elems[i].innerHTML.toString().toLowerCase()});
        }
    }
    if(elemsforsort.length == 0){return;}
    const sorted = sortbytype(elemsforsort, datatype, sorttype);
    console.log(sorted);
    for(let j = 0; j < sorted.length; ++j){
        body.appendChild(sorted[j].container);
    }
}

function sortbytype(elems, datatype, sorttype){
    if(datatype === 'date'){
        if(sorttype === 'asc'){
            elems.sort((a,b) => a.date - b.date)
        }
        else{
            elems.sort((a,b) => b.date - a.date)
        }

    }
    else if(datatype === 'str'){
        if(sorttype === 'asc'){
            elems.sort(function(a,b){  return a.str > b.str ? 1 : -1})  ;
        }
        else{
            elems.sort(function(a,b){  return a.str > b.str ? -1 : 1})  ;
        }
    }
    return elems;
}
