
String.prototype.trim = function() {
	return this.replace(/^\s+|\s+$/g,"");
}
String.prototype.ltrim = function() {
	return this.replace(/^\s+/,"");
}
String.prototype.rtrim = function() {
	return this.replace(/\s+$/,"");
}

function formFieldsCheck(formName) {
	if (isDOM) {
		var str = "";
		var allOk = true;
		var elementName = '';
		var focused = false;
		var badfield = false;
		var elements = document.forms[formName].getElementsByTagName('input');
		for(var i = 0; i < elements.length; i++) {
			var mandatoryField = elements.item(i).getAttribute('mandatoryfield');
			var preg_mask = elements.item(i).getAttribute('preg_mask');
			badfield = false;
			if (preg_mask != null) {
				evalstr = "myRe = " + preg_mask + ";";
				eval(evalstr);

			}
			if (elements.item(i).type != 'text') continue;
			elements.item(i).style.background = "none";
			elements.item(i).value = elements.item(i).value.trim();
			var value = elements.item(i).value.trim();
			if (((preg_mask != null) && (value!='') && !myRe.test(value))){
				badfield = true;
			}
			if (mandatoryField != null &&  value == '') {
				badfield = true;
			}
			if (badfield) {
				allOk = false;
				elements.item(i).style.background = "#FA8080";
				if (elementName == '') elementName = elements.item(i).getAttribute('name');
			}

		}
		elements = document.forms[formName].getElementsByTagName('textarea');
		for(var i = 0; i < elements.length; i++) {
			var mandatoryField = elements.item(i).getAttribute('mandatoryfield');
			if (mandatoryField != null) {
				elements.item(i).style.background = "none";
				var value = elements.item(i).value;
				if (value == '') {
					allOk = false;
					elements.item(i).style.background = "#FA8080";
					if (elementName == '') elementName = elements.item(i).getAttribute('name');
				}
			}
		}

		if (allOk == false) {
			alert("Error!\n" +str);
			document.forms[formName].elements[elementName].focus();
			return false;
		} else return true;
	} else return true;
}