# Project structure

The Django version of Bober consists of multiple sub-applications:
  - bober - a django shim over the old, deprecated PHP version
  - bober\_paper\_submissions - a small application allowing teachers to enter the results by hand
  - bober\_si - contains school registration, diploma generation and any other customization needed by the slovenian development team.
  - bober\_simple\_competition - the core Bebras competition functionality
  - bober\_tasks - an application for writing simple multiple choice questions which can be imported into bebras\_simple\_competition
  - code\_based\_auth - an over-engineered, probably insecure but highly customizable authentication system based on multi-part codes which may contain hashes which may someday in the future be used to build a completely distributed world-scale Bebras competition
  - popup\_modelviews - generic model views allowing the editing, creation and deletion of related models similar to the ones used the django admin interface with the option of displaying the objects either embedded or in a popup
