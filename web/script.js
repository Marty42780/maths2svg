const default_point_names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AI", "AJ", "AK", "AL", "AM", "AN", "AO", "AP", "AQ", "AR", "AS", "AT", "AU", "AV", "AW", "AX", "AY", "AZ", "BA", "BB", "BC", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BK", "BL", "BM", "BN", "BO", "BP", "BQ", "BR", "BS", "BT", "BU", "BV", "BW", "BX", "BY", "BZ", "CA", "CB", "CC", "CD", "CE", "CF", "CG", "CH", "CI", "CJ", "CK", "CL", "CM", "CN", "CO", "CP", "CQ", "CR", "CS", "CT", "CU", "CV", "CW", "CX", "CY", "CZ", "DA", "DB", "DC", "DD", "DE", "DF", "DG", "DH", "DI", "DJ", "DK", "DL", "DM", "DN", "DO", "DP", "DQ", "DR", "DS", "DT", "DU", "DV", "DW", "DX", "DY", "DZ", "EA", "EB", "EC", "ED", "EE", "EF", "EG", "EH", "EI", "EJ", "EK", "EL", "EM", "EN", "EO", "EP", "EQ", "ER", "ES", "ET", "EU", "EV", "EW", "EX", "EY", "EZ", "FA", "FB", "FC", "FD", "FE", "FF", "FG", "FH", "FI", "FJ", "FK", "FL", "FM", "FN", "FO", "FP", "FQ", "FR", "FS", "FT", "FU", "FV", "FW", "FX", "FY", "FZ", "GA", "GB", "GC", "GD", "GE", "GF", "GG", "GH", "GI", "GJ", "GK", "GL", "GM", "GN", "GO", "GP", "GQ", "GR", "GS", "GT", "GU", "GV", "GW", "GX", "GY", "GZ", "HA", "HB", "HC", "HD", "HE", "HF", "HG", "HH", "HI", "HJ", "HK", "HL", "HM", "HN", "HO", "HP", "HQ", "HR", "HS", "HT", "HU", "HV", "HW", "HX", "HY", "HZ", "IA", "IB", "IC", "ID", "IE", "IF", "IG", "IH", "II", "IJ", "IK", "IL", "IM", "IN", "IO", "IP", "IQ", "IR", "IS", "IT", "IU", "IV", "IW", "IX", "IY", "IZ"];

function generate() {
    // Part to get fileType
    let fileType = "'" + document.querySelector("input[name=\"image-type\"]:checked").value + "'";
    // Part to get graphInputs
    let points_informations = document.querySelector("#points-information").children;
    let temp_default_point_names = default_point_names;
    let graphInputs = "";
    for (let i = 2; i < points_informations.length; i += 2) {
        if (points_informations[i].value == "") {
            points_informations[i].value = temp_default_point_names[0]; temp_default_point_names.shift();
        };
        let list_of_the_points_they_are_linked_to = points_informations[i + 1].value.split(", ");
        let string_the_points_they_are_linked_to = "";
        if (list_of_the_points_they_are_linked_to[0] != "") {
            for (let i = 0; i < list_of_the_points_they_are_linked_to.length; i++) {
                string_the_points_they_are_linked_to += "\"" + list_of_the_points_they_are_linked_to[i] + "\",";
            };
        };
        graphInputs += "\"" + points_informations[i].value + "\":[" + string_the_points_they_are_linked_to + "],";
    };
    // Part to get label
    if (document.querySelector("#label").checked == true) { 
        label = "True"; 
    } else { 
        label = "False"; 
    };
    // Part to get labelCapitalized
    if (document.querySelector("#label-capitalize").checked == true) { 
        labelCapitalize = "True"; 
    } else { 
        labelCapitalize = "False"; 
    };
    // Part to get mainColor
    mainColor = document.querySelector("#mainColorSelector").value
    // Part to get mainColor
    bgColor = document.querySelector("#backgroundColorSelector")


    // Part to generate url
    url = "/image?fileType=" + fileType + "&graphInputs=" + graphInputs;

    document.querySelector("#generated-image").src = url;
    document.getElementById("result").style.display = "flex";
    // TODO: Set href of show / download button here
};




function init_nb_of_points() {
    let nb_of_point_input = document.querySelector('#nb_of_point');
    let grid_of_points = document.querySelector("#points-information");
    nb_of_point_input.addEventListener('change', (event) => { update_nb_of_points() });
    update_nb_of_points();
};
function update_nb_of_points() {
    let nb_of_point_input = document.querySelector('#nb_of_point');
    let grid_of_points = document.querySelector("#points-information");
    if (nb_of_point_input.value >= 2) {
        if ((grid_of_points.childElementCount - 2) / 2 < nb_of_point_input.value) {
            grid_of_points.insertAdjacentHTML('beforeEnd', `<input type="text" name="name-of-point" id="name-of-point" placeholder="A"/><input type="text" name="points-they-are-linked-to" id="points-they-are-linked-to" placeholder="A, B, C, ..." />`.repeat(nb_of_point_input.value - ((grid_of_points.childElementCount - 2) / 2)));
        } else if ((grid_of_points.childElementCount - 2) / 2 > nb_of_point_input.value) {
            let dif = (grid_of_points.childElementCount - 2) / 2 - nb_of_point_input.value;
            for (let i = 0; i < dif; i++) {
                grid_of_points.removeChild(grid_of_points.lastChild); // Remove name input
                grid_of_points.removeChild(grid_of_points.lastChild); // Remove Point they are linked to input
            };
        };
    };
};