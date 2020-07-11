# Customization


For details about standard mkdocs options, see [MkDocs Configuration](http://www.mkdocs.org/user-guide/configuration/).

In addition, the Windmill theme supports a few additional options, which may be
listed under the `extra:` key of `mkdocs.yml`.

## Extra configuration options

`extra.logo`: Path to a logo to include in the top bar next to the site name.

`extra.version`: Version number to include right under the site name.

`extra.article_nav_top`: Set to `false` to hide the Previous/Next navigation buttons above article contents.

`extra.article_nav_bottom`: Set to `false` to hide the Previous/Next navigation buttons below article contents.

`extra.history_buttons`: Include back/forward buttons in the top bar. This is
  useful when the documentation site is included into a bare browser, e.g. into
  an Electron-based application.

`extra.css.main_color`: Sets the main theme color of the site. This should be a somewhat dark color as it is also used for links.

`extra.css.gray`: Sets the gray tone used for some borders.

`extra.css.lighter_gray`: Sets the gray tone used for various backgrounds.

`extra.nav_info`: This defines the custom links above the table of contents. It is a list of objects with the following fields:
- `type`: This indicates the to what you link by using the given value as a Fontawesome icon. Possible values include `github`, `twitter`, `facebook`, `slack` and a lot more!
- `title`: This sets the text that is being displayed
- `url`: Sets the links href
