# Laravel Goto View Controller - Sublime Text 3

Based on predragnikolic's work, but added two lines in `LaravelGotoViewController.py` so that controllers in subfolders could be reached, too.

Those two lines are:

```python
        if '\\' in text:
            text = text.replace('\\', '/')
```
