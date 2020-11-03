# ImageDown
[WIP] Google Images full-photo downloader

**Not need ChromeDriver installion. It will be installed automatically..**

## 📦 Installation
```sh
pip install imagedown
```

## 🔷 Examples
**Google: **
```python
from ImageDown import ImageDown 

ig = ImageDown().Google('istanbul', 10)
ig.get_urls()
ig.download()
```

**Yandex: **
```python
from ImageDown import ImageDown 

ig = ImageDown().Yandex('istanbul', 10)
ig.get_urls()
ig.download()
```

## ☑️ To-Do
By time I do these, 1.0.0 will be ready.

- [X] Downloader
- [X] Yandex
- [ ] More exception, More choice, stability.

## 💻 Contributors
[@Quiec](https://t.me/Fusuf)

## License
GPLV3