Later
=====

A command-line issue tracker for a lazy developer

This fork is modified to fit wenli's workflow. You may prefer the upstream versions:
`qznc/later <https://github.com/qznc/later>`_
, 
`ongspxm/later <https://github.com/ongspxm/later>`_
.

Differences between wenli and upstream
------------------------------------------

 * Remove "reporter" and "responsible" fields by default (for working alone)
 * Add "component" field, representing which part of the project the issue applies to.
 * Add "type" field, representing "bug", "feature", etc.
 * When printing issues, display component and type, and sort nicely, and show separators between components.
 * Store date when closing issues
 * ``later add "issue message" -e`` for direct editing when adding an issue
 * Support searching multi-value keys (e.g. tags)
 * Configurable key aliases (e.g. let "comp" match "component")
 * ``later search`` performs full text regular expression search
 * ``later list all`` shows all issues, not just closed issues.
 * ``later`` defaults to ``later list`` instead of ``later help``.
 * More verbose output after execution of various commands

Usage
-----

There is no website or release version, yet.
Clone the github repository git://github.com/wenli0114/later.git
and use the ``later`` executable.
Start with ``later help``.

Default config available in ``config`` (found in same directory as
the ``later`` executable.

Philosophy
----------

Reread the tag line above!
It is the essence of the philosophy behind this tool.
More precisely:

 1. This is primarily **command-line**. The web is secondary.
 2. "**A** developer" means big project management is out of scope.
 3. Lots of shortcuts and deferring for **lazy** devs like me.
 4. End users, managers and translators should use something else.

