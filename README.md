Sort of mimics how battle brothers does skills

I take some shortcuts, for example not every skill in bb had the ability to modify stats, and instead did so through a function (e.g. the background would return stat mods but the slash skill obviously wouldn't have access to that)

A lot of this is just using dict copies and @property decorators etc

Some things could be shifted slightly, e.g. the location of the allBackgrounds list creation would ideally be moved outside of that file and into a separate config file that creates all of the lists at once, this way other users would be able to have a file that gets executed to pump stuff into our background_dict but otherwise this is a reasonable 3am push