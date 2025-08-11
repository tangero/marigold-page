# Nastavení Cloudflare Pages pro Vibecoding.cz

## DŮLEŽITÉ: V Cloudflare Pages UI nastavit:

### 1. Základní nastavení
- **Framework preset:** Jekyll (MUSÍ BÝT VYBRÁNO!)
- **Build command:** `jekyll build --config _config_vibecoding.yml && cp vibecoding-index.html _site/index.html`
- **Build output directory:** `_site`
- **Root directory:** (ponech prázdné)

### 2. Environment Variables
Přidej tyto proměnné prostředí:
- `JEKYLL_ENV` = `production`
- `RUBY_VERSION` = `3.0.0`

### 3. Pokud stále nefunguje
Zkus změnit Framework preset na "None" a použij tento build command:
```
gem install bundler && bundle install && bundle exec jekyll build --config _config_vibecoding.yml && cp vibecoding-index.html _site/index.html
```

### 4. Alternativa - přes npm script
Pokud Cloudflare trvá na detekci Python projektu, můžeme přidat package.json:
```json
{
  "name": "vibecoding",
  "scripts": {
    "build": "bundle install && bundle exec jekyll build --config _config_vibecoding.yml && cp vibecoding-index.html _site/index.html"
  }
}
```
A pak použít build command: `npm run build`

### 5. Deploy přes GitHub Actions (nejspolehlivější)
Pokud Cloudflare Pages build selhává, použij GitHub Actions pro build a Cloudflare pouze pro hosting.