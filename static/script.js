const days = document.querySelector(".calendar-container")
const addAvailability = document.querySelector(".user-availability")
const clearAvailability = document.querySelector(".clear-user-availability")
const userName = document.querySelector(".user-name")

days.addEventListener("click", (target)=> {
    target.preventDefault();
    if(target.originalTarget.tagName === "LI" && target.originalTarget.outerText !== "" && target.originalTarget.parentElement.className === "days"){
        target.target.classList.toggle("active")
    }
})

addAvailability.addEventListener("click", (target)=> {
  const name = userName.value  
  if (name !==""){
    let data = {};
    const availableDays = Array.from(document.querySelectorAll(".active"));
    if (availableDays.length == 0) return;
    data["data"] = availableDays.map((element)=>{
      return `${element.dataset.day}/${element.dataset.month}/${element.dataset.year}`;
    })
    data["name"] = name;
    fetch("/add", {
      method: "POST",
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(data)
    }).then(res => {
      location.reload();
    });
    }
})

clearAvailability.addEventListener("click", (target)=>{
const name = userName.value;
  if (name !==""){
    const data = {"name": name};
    fetch("/clear", {
      method: "POST",
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(data)
    }).then(res => {
      location.reload();
    });
    }
})