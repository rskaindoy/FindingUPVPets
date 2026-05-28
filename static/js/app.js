// search func
async function searchPet() {

    const pet = document.getElementById("pet").value;
    const time = document.getElementById("time").value;

    try {
        const response = await fetch("/search-pet", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({          
                pet: pet
            })
        });

        const data = await response.json();

        console.log(data);

        const resultsDiv = document.getElementById("results");
        resultsDiv.innerHTML = "";

        // logic to show results here; expected data from backend: ranked list of tuples (location, score) 

    } catch (error) {
        console.error("Search error: ", error);
        document.getElementById("results").innerHTML = "<p>Error fetching results.</p>";
    }
    
}


// report func
async function submitReport() {

    const pet = document.getElementById("selected-pet-name").value;
    const location = document.getElementById("location").value;
    const time = document.querySelector('input[name="timeRange"]:checked');

    if (!pet || !pet.value) {
        alert("Select a pet.");
        return;
    }
    if (!location || location === "-- Select a Spot --") {
        alert("Select a location");
        return;
    }
    if (!time) {
        alert("Select a time range.");
        return;
    }

    const response = await fetch("/submit-report", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            pet: pet,
            location: location,
            time: time
        })
    });

    const data = await response.json();

    alert(data.message);
}

