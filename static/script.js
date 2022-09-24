const days = document.querySelector(".calendar-container")
const addAvailability = document.querySelector(".user-availability")


const userName = document.querySelector(".user-name")

days.addEventListener("click", (target)=> {
    target.preventDefault();
    if(target.originalTarget.tagName === "LI" && target.originalTarget.outerText !== "" && target.originalTarget.parentElement.className === "days"){
        target.target.classList.toggle("active")

      console.log(target.target.textContent)
      const data = {"data": target.target.textContent}
      fetch("/test", {
      method: "POST",
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(data)
    }).then(res => {
      console.log("Request complete! response:", res);
    });
    }



})

addAvailability.addEventListener("click", (target)=> {
  const name = userName.value  
  if (name !==""){
    const name = userName.value
    let data = {};
    const availableDays = Array.from(document.querySelectorAll(".active"))


    data["data"] = availableDays.map((element)=>{
      return [element.dataset.day, element.dataset.month , element.dataset.year]
    })
    data["name"] = name
    fetch("/test", {
      method: "POST",
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(data)
    }).then(res => {
      console.log("Request complete! response:", res);
    });
    }
}
)
