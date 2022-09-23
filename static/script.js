const days = document.querySelector(".days")
const btnSend = document.querySelector(".btn-send")
const userName = document.querySelector(".user-name")

days.addEventListener("click", (target)=> {
    if(target.originalTarget.tagName === "LI" && target.originalTarget.outerText !== ""){
        target.target.classList.toggle("active")
    }
})

btnSend.addEventListener("click", (target)=> {
    const name = userName.value
    let data = {};
    data["name"] = name


    fetch("/test", {
      method: "POST",
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(data)
    }).then(res => {
      console.log("Request complete! response:", res);
    });
    }
)