$.widget("ui.writer", {
	_init: function() {
		var widget = this;
		var $widget = this.element;
		
		// This sets up the scope for "this" inside changeWriting() properly.
		$widget.click(function(e) {
			widget.changeWriting(e);
		});
	},
	
	changeWriting: function(e) {
		var message = this._getMessage();
		this.element.text(message);
	},
	
	_getMessage: function() {
		return "Hey there";
	}
});