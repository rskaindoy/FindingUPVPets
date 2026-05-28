// search func
async function searchPet() {
    //get needed val
    const pet = document.getElementById("pet").value;
    const time = document.getElementById("time").value;

    try {
        //req to flask server
        const response = await fetch("/search-pet", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({          
                pet: pet,
                time: time
            })
        });
        //parse json to arr
        const data = await response.json();
        //for cases where there might still be leftovers from prev
        const resultsDiv = document.getElementById("results");
        resultsDiv.innerHTML = "";
        // If the data is empty
        if (!data || data.length === 0) {
            resultsDiv.innerHTML = "<p class='no-results'>No recent sightings found for this pet during that time frame.</p>";
            return;
        }
        // for printing out the results later
        let htmlContent = `
            <div class="results-wrapper">
                <h3>Ranked Sighting Locations</h3>
                <p class="results-subtitle">Showing results for <b>${pet}</b> during <b>${time}</b></p>
                <table class="results-table">
                    <thead>
                        <tr>
                            <th>Rank</th>
                            <th>Location</th>
                            <th>Likelihood</th>
                        </tr>
                    </thead>
                    <tbody>
        `;
        // data in table- loop through each location and percentage inside the sorted data array
        data.forEach(([location, percentage], index) => {
            const rankNumber = index + 1;

            htmlContent += `
                <tr class="${index === 0 ? 'top-result' : ''}">
                    <td class="rank-cell">${rankNumber}</td>
                    <td class="location-cell">${location}</td>
                    <td class="percentage-cell">${percentage}%</td>
                </tr>
            `;
        });

        htmlContent += `
                    </tbody>
                </table>
            </div>
        `;
        //inject
        resultsDiv.innerHTML = htmlContent;
        resultsDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });

    } catch (error) {
        console.error("Search error: ", error);
        document.getElementById("results").innerHTML = "<p class='no-results'>Error fetching results.</p>";
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


document.addEventListener("DOMContentLoaded", function () {
    const petSelect = document.getElementById("pet"); //pet selection
    if (!petSelect) return; //check if exist then return if not

    petSelect.addEventListener("change", function () {
        const preview = document.getElementById("petPreview");
        const selectedOption = this.options[this.selectedIndex];
        const petName = this.value;

        if (!petName) {
            preview.style.display = "none";
            return;
        }
        //get filename
        const imgPath = selectedOption.getAttribute("data-img");
        const img = document.getElementById("petImg");
        //create path if and show if image exist
        if (imgPath) {
            img.src = `/static/${imgPath}`;
            img.style.display = "block";
        } else {
            img.style.display = "none";
        }

        // get active option element  and  that thing's val
        document.getElementById("petName").textContent = petName;
        preview.style.display = "block";
    });
});