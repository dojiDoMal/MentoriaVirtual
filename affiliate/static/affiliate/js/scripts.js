const root = document.querySelector(".root");
const bg = document.querySelector(".background");
const descriptionTab = document.querySelector("#description-tab");
const profileTab = document.querySelector("#profile-tab");
const evaluationsTab = document.querySelector("#evaluations-tab");
const test = document.getElementsByTagName('label')
const filterForm = document.querySelector("#category-form");
const positions = [];


if(filterForm){
  newChild = '<option value="" selected="">Todas As Categorias</option>'
  scdChild = filterForm.getElementsByTagName('div')[2];
  scdChild.removeChild(scdChild.firstElementChild);
  filterForm.querySelector('select').firstElementChild.innerHTML = newChild;
  filterForm.getElementsByTagName('div')[2].firstElementChild.classList.add('custom-select')
}

if(bg){
  bg.style.top = -480 + "px";
}

if(root){
  root.addEventListener("mousemove", e => {
    var y = -(e.pageY + bg.offsetTop)/40;
    positions.push({y});
    if (positions.length > 2)
      positions.splice(0, 1);
      
    const current = positions.reduce((acc, e) => { acc.y += e.y; return acc }, { y: 0 });
    current.y /= positions.length;
    
    bg.style.transform = `translateY(${current.y}px)`;
  });
}

if(descriptionTab){
descriptionTab.addEventListener("click", e => {
  e.preventDefault();
  activate(descriptionTab, profileTab, evaluationsTab);
  activateAndShow(
    document.querySelector('#description'),
    document.querySelector("#profile"),
    document.querySelector("#evaluations"),
  )
})
}

if(profileTab){
profileTab.addEventListener("click", e => {
  e.preventDefault();
  activate(profileTab, descriptionTab, evaluationsTab);
  activateAndShow(
    document.querySelector("#profile"),
    document.querySelector('#description'),
    document.querySelector("#evaluations"),
  )
})
}

if(evaluationsTab){
evaluationsTab.addEventListener("click", e=> {
  e.preventDefault();
  activate(evaluationsTab, descriptionTab, profileTab);
  activateAndShow(
    document.querySelector("#evaluations"),
    document.querySelector("#profile"),
    document.querySelector('#description'),
  )
})
}

/** Insere a classe 'active' no elemento passado como primeiro argumento e remove a mesma classe dos outros elementos restantes*/
function activate(...args) {
  args.forEach((arg, index) => {
    if(index == 0){
      arg.classList.add('active');
    } else{
      arg.classList.remove('active');
    }
  });
}

function activateAndShow(...args) {
  args.forEach((arg, index) => {
    if(index == 0){
      arg.classList.add('show');
      arg.classList.add('active');
    } else{
      arg.classList.remove('show');
      arg.classList.remove('active');
    }
  });
}

var x, i, j, l, ll, selElmnt, a, b, c;
/* Look for any elements with the class "custom-select": */
x = document.getElementsByClassName("custom-select");
l = x.length;
for (i = 0; i < l; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  ll = selElmnt.length;
  /* For each element, create a new DIV that will act as the selected item: */
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  /* For each element, create a new DIV that will contain the option list: */
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < ll; j++) {
    /* For each option in the original select element,
    create a new DIV that will act as an option item: */
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function(e) {
        /* When an item is clicked, update the original select box,
        and the selected item: */
        var y, i, k, s, h, sl, yl;
        s = this.parentNode.parentNode.getElementsByTagName("select")[0];
        sl = s.length;
        h = this.parentNode.previousSibling;
        for (i = 0; i < sl; i++) {
          if (s.options[i].innerHTML == this.innerHTML) {
            s.selectedIndex = i;
            h.innerHTML = this.innerHTML;
            y = this.parentNode.getElementsByClassName("same-as-selected");
            yl = y.length;
            for (k = 0; k < yl; k++) {
              y[k].removeAttribute("class");
            }
            this.setAttribute("class", "same-as-selected");
            break;
          }
        }
        h.click();
        this.closest('form').submit()
    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function(e) {
    /* When the select box is clicked, close any other select boxes,
    and open/close the current select box: */
    e.stopPropagation();
    closeAllSelect(this);
    this.nextSibling.classList.toggle("select-hide");
    this.classList.toggle("select-arrow-active");
    console.log(this.firstElementChild)
    
  });
}

function closeAllSelect(elmnt) {
  /* A function that will close all select boxes in the document,
  except the current select box: */
  var x, y, i, xl, yl, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  xl = x.length;
  yl = y.length;
  for (i = 0; i < yl; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < xl; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}

/* If the user clicks anywhere outside the select box,
then close all select boxes: */
document.addEventListener("click", closeAllSelect);