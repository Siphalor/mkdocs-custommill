# CustomMill theme

## About

CustomMill theme focuses on clean usable navigation for large documentation projects. It retains the state of the menu of pages and folders across page transitions, by keeping navigation to an iframe.

It also implements a versatile search, featuring term highlighting, and both a quick dropdown and a full-page option that allows the user to come back to search results.

Within pages, it uses the default mkdocs theme, including syntax highlighting.

One of the key features is the support of deep nesting of pages into folders.

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

Note that it's important for there to set a `home` page that will be shown as front page. Specify the path to this page without the `.md` extension.

See [Customization](customization.md) for a few extra configuration options
supported by the CustomMill theme.
