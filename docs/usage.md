# CustomMill theme

## Features

- Clean navigation for large documentation projects
- Retains the state of the menu across page transitions
- Versatile search with term highlighting in a quick search and on its own page
- Supports syntax highlighting within pages
- Deep nesting of pages in folders

## Improvements over Windmill

- Customizable colors!
- Customizable links in the navigation menu
- A lot of small stylistic and design fixes
- Better search result listing
- Bootstrap 5 and no more jQuery

## Installation

Install the CustomMill theme using `pip`:

``` sh
pip install mkdocs-custommill
```

To install and get started with `mkdocs`, follow [MkDocs documentation](http://www.mkdocs.org/#installation).

## Usage

To use the CustomMill theme installed via `pip`, add this to your `mkdocs.yml`:

``` yaml
theme: 'custommill'
```

If you cloned CustomMill from GitHub:

``` yaml
theme:
  name: null
  custom_dir: '{INSTALL_DIR}/mkdocs_windmill'
  # Copy settings from mkdocs_theme.yml, which is ignored by custom_dir themes.
  static_templates: [404.html, index.html, css/base.css]
  home: home
  search_index_only: true
  include_search_page: true
  main_color: '#bb0000'
  gray: '#e0e0e0'
  lighter_gray: '#eeeeee'
```

!!! warning
	Note that it's important to set a `home` page that will be shown as the front page. Specify the path to this page without the `.md` extension.

	Additionally, since CustomMill generates it's own `index.html` file **you are not allowed to use `index.md`** as a top level file.

	I suggest naming your landing page related to the content, like `usage.md` in these documents or `home.md` in more general scenarios.

See [Customization](customization.md) for a few extra configuration options
supported by the CustomMill theme.
