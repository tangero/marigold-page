# Nastavení Cloudflare Pages pro vibecoding.cz

## Build nastavení

### Framework preset
- **Jekyll** (vybrat z nabídky)

### Build command
```bash
bundle exec jekyll build --config _config_vibecoding.yml
```

### Build output directory
```
_site
```

### Root directory
- Ponechat prázdné

## Environment variables

```
JEKYLL_ENV = production
RUBY_VERSION = 3.2.0
```

## Branch deployments

- **Production branch**: main
- **Preview branches**: Enable all non-production branches

## Důležité poznámky

1. Projekt používá Jekyll 4.3.3 s Ruby
2. Konfigurace pro vibecoding.cz je v souboru `_config_vibecoding.yml`
3. Gemfile a Gemfile.lock jsou v kořenovém adresáři
4. Build vytváří výstup do adresáře `_site`

## Alternativní build command (pokud by byl problém)

Pokud by základní build command nefungoval, můžete použít:

```bash
gem install bundler && bundle install && bundle exec jekyll build --config _config_vibecoding.yml
```

## Řešení problémů

### Chyba "Could not locate Gemfile"
- Ujistěte se, že je Root directory prázdné
- Zkontrolujte, že jsou Gemfile a Gemfile.lock v repozitáři

### Chyba s Jekyll verzí
- Cloudflare Pages by mělo automaticky detekovat verzi z Gemfile
- Pokud ne, přidejte environment variable: `RUBY_VERSION = 3.0.0`