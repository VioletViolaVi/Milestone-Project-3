function format(date) {
	if (typeof date == "string") {
		return date;
	} else {
		return "ERROR!";
	}
}

function yearRange(years) {
	if (typeof years == "number") {
		return years;
	} else {
		return "ERROR!";
	}
}

function firstDay(start) {
	if (typeof start == "number") {
		return start;
	} else {
		return "ERROR!";
	}
}

function i18n(done) {
	if (typeof done == "string") {
		return done;
	} else {
		return "ERROR!";
	}
}

function dist(length) {
	if (typeof length == "number") {
		return length;
	} else {
		return "ERROR!";
	}
}

function duration(speed) {
	if (typeof speed == "number") {
		return speed;
	} else {
		alert("ERROR!");
	}
}

function padding(spaces) {
	if (typeof spaces == "number") {
		return spaces;
	} else {
		alert("ERROR!");
	}
}

function numVisible(slides) {
	if (typeof slides == "number") {
		return slides;
	} else {
		alert("ERROR!");
	}
}