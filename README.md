# Laravel goto view controller - Sublime Text 3

This plugin lets you easily jump to a blade view or a controller.
If the blade file for the given view doesn't exis, it will be created.

![Example](/img/showcase.gif)

## Installation 

* Clone this repository to `sublime-text-3/Packages` folder.
* Add this keybinding. 

```json
{ 
	"keys": ["f12"], "command": "laravel_goto_view_controller", 
	"args": {
  		"fallback_command": "goto_definition",
	},
	"context": [{"key": "selector", "operator": "equal", "operand": "source.php"} ]
}
```

You can assign the same keybinding you use for goto definition. Just specify the `fallback_command` in the `args` section of the keybinding, with one of these values:
* `"goto_definition"` - This is the default value.
* `"lsp_symbol_definition"` - If you use [LSP](https://github.com/tomv564/LSP).

* Done. :wink:
