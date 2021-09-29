
function requestJsonKiruna(date) {
    try {
            $.ajax({
            type: 'GET',
            url: `https://sheets.googleapis.com/v4/spreadsheets/1UPl5omRAHA6uMnlC--p_tKvYLEYgyrpn7ZJjtdvupoI/values/B11:C17?key=AIzaSyAEcN2gPi9-UMllfIveKJydPZTrmKjJFKY`,
            success: function (response) {
                document.getElementById('liveOpeningHours').innerHTML = getTimeMsg(FormatKirunaResponse(response), date);
            } 
        });
        //const response = fetch(`https://sheets.googleapis.com/v4/spreadsheets/1UPl5omRAHA6uMnlC--p_tKvYLEYgyrpn7ZJjtdvupoI/values/B11:C17?key=AIzaSyAEcN2gPi9-UMllfIveKJydPZTrmKjJFKY`);
        //data = response.json();
    } catch (e) {
        console.error("Error: " + e);
    }
}

function FormatKirunaResponse(data){
    let openHoursKiruna = [];
    try {
        openHoursKiruna = [
            [parseInt(data.values[6][0]), parseInt(data.values[6][1])],
            [parseInt(data.values[0][0]), parseInt(data.values[0][1])],
            [parseInt(data.values[1][0]), parseInt(data.values[1][1])],
            [parseInt(data.values[2][0]), parseInt(data.values[2][1])],
            [parseInt(data.values[3][0]), parseInt(data.values[3][1])],
            [parseInt(data.values[4][0]), parseInt(data.values[4][1])],
            [parseInt(data.values[5][0]), parseInt(data.values[5][1])],
            [parseInt(data.values[6][0]), parseInt(data.values[6][1])]
        ]
        setTimesStatic('kiruna', openHoursKiruna);
    } catch (e) {
        console.error("Error formatting. Make sure no letters or signs are entered.");
    }
    return openHoursKiruna;
}

function requestJsonLulea(date) {
   try {
        $.ajax({
            type: 'GET',
            url: `https://sheets.googleapis.com/v4/spreadsheets/1UPl5omRAHA6uMnlC--p_tKvYLEYgyrpn7ZJjtdvupoI/values/B21:C27?key=AIzaSyAEcN2gPi9-UMllfIveKJydPZTrmKjJFKY`,
            success: function (response) {
                document.getElementById('liveOpeningHours').innerHTML = getTimeMsg(FormatLuleaResponse(response), date);
            }
        });  
    } catch (e) {
        console.error("Error: " + e);
    }
}

function FormatLuleaResponse(data){
    let openHoursLulea = [];
    try {
        openHoursLulea = [
            [parseInt(data.values[6][0]), parseInt(data.values[6][1])],
            [parseInt(data.values[0][0]), parseInt(data.values[0][1])],
            [parseInt(data.values[1][0]), parseInt(data.values[1][1])],
            [parseInt(data.values[2][0]), parseInt(data.values[2][1])],
            [parseInt(data.values[3][0]), parseInt(data.values[3][1])],
            [parseInt(data.values[4][0]), parseInt(data.values[4][1])],
            [parseInt(data.values[5][0]), parseInt(data.values[5][1])],
            [parseInt(data.values[6][0]), parseInt(data.values[6][1])]
        ]
        setTimesStatic('lulea', openHoursLulea);
    } catch (e) {
        console.error("Error formatting. Make sure no letters or signs are entered.");
    }
    return openHoursLulea;
}
