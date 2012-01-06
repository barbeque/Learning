$.widget("ui.writer", {
	_init: function() {
		var widget = this;
		var $widget = this.element;
		$widget.disableSelection();
		var toggled = false;
		
		// This sets up the scope for "this" inside changeWriting() properly.
		$widget.click(function(e) {
			widget.changeWriting(e);
		});
	},
	
	changeWriting: function(e) {
		var message = this._getMessage();
		this.toggled = !this.toggled;
		this.element.text(message);
	},
	
	_getMessage: function() {
		if(this.toggled) {
			return "Goodbye, then";
		}
		else {
			return "Hey there";
		}
	}
});