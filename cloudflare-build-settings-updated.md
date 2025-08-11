# Aktualizované nastavení Cloudflare Pages

## Nastavení v Cloudflare UI:

### Build configuration
- **Build command:** `./simple-build.sh`
- **Build output directory:** `_site`
- **Root directory:** (prázdné)

### Environment variables
- `LC_ALL` = `C.UTF-8`
- `JEKYLL_ENV` = `production`

### Framework preset
- `None` nebo `Jekyll` (zkus oba)

## Alternativní build commands k testování:

1. **Nejjednodušší:**
   ```
   mkdir -p _site && echo "<h1>Test</h1>" > _site/index.html
   ```

2. **S Jekyll:**
   ```
   bundle install && bundle exec jekyll build --config _config_vibecoding.yml || (mkdir -p _site && echo "<h1>Fallback</h1>" > _site/index.html)
   ```

3. **Přes npm:**
   ```
   npm run build
   ```

## Debug informace:
Pokud ani simple-build.sh nefunguje, zkus nejjednodušší build command výše jako test.