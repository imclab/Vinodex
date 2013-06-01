jQuery.fn.valreset = function() {
	"use strict";
	$(this).find(".control-group").removeClass("error");
	$(this).find(".help-block").addClass("hide");
};

jQuery.fn.vallength = function() {
	"use strict";
	if($(this).val().trim().length === 0) {
		$(this).valerror();
		return null;
	} else {
		return $(this).val();
	}
};

jQuery.fn.valnumber = function() {
	"use strict";
	if($(this).val().trim().length === 0 || 
	isNaN($(this).val()) ||
	parseFloat($(this).val()) <= 0) {
		$(this).valerror();
		return null;
	} else {
		return $(this).val();
	}
};

jQuery.fn.valvintageyear = function() {
	"use strict";
	if($(this).val().trim().length === 0 && !$("#nv").prop("checked")) {
		$(this).valerror();
		return null;
	} else {
		return $(this).val();
	}
};

jQuery.fn.valemail = function() {
	"use strict";
	if($(this).val().indexOf("@") === -1) {
		$(this).valerror();
		return null;
	} else {
			return $(this).val();
	}
};

jQuery.fn.valpassword = function() {
	"use strict";
	if($(this).val().trim().length < 6) {
		$(this).valerror();
		return null;
	} else {
		return $(this).val();
	}
};

jQuery.fn.valselect = function() {
	"use strict";
	if($(this).val() === null) {
		$(this).valerror();
		return null;
	} else {
			return $(this).val();
	}
};

jQuery.fn.valrating = function() {
	"use strict";
	if($(this).find(".icon-star").length === 0) {
		$(this).valerror();
		return null;
	} else {
			return $(this).find(".icon-star").length;
	}
};

jQuery.fn.valerror = function() {
	"use strict";
	if($(this).parent().hasClass("input-append")) {
		$(this).parent().siblings(".help-block").removeClass("hide").parent().parent().addClass("error");
	} else {
		$(this).siblings(".help-block").removeClass("hide").parent().parent().addClass("error");
	}
};