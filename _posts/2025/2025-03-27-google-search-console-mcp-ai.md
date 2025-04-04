---
audio_url: null
author: Patrick Zandl
categories:
- MCP
- Google
layout: post
post_excerpt: Jak lépe zpracovávat podklady, které generuje Google Search Console
  a jak jim lépe rozumět pomocí AI? Integrovat Search Consoli pomocí Model Communication
  Protocol.
summary_points:
- MCP propojuje AI asistenty s externími nástroji, například Google Search Console.
- Integrace GSC a MCP automatizuje SEO analýzu a reporting webových stránek.
- Implementace vyžaduje Google Cloud projekt, aktivované GSC API a MCP server.
- Konektor umožňuje vlastní časové rozsahy, filtry a agregaci dat z GSC.
thumbnail: https://www.m3estrategia.com/wp-content/uploads/2020/03/<a href='/google/' class='keyword-link'>google</a>-search-console-m3.jpg
title: Propojení Google Search Console s MCP - Komplexní průvodce
---

Model Communication Protocol ([MCP](/ai/mcp/)) představuje inovativní způsob, jak propojit AI asistenty s externími službami a nástroji. Google Search Console (GSC) je neocenitelný nástroj pro SEO analýzu a monitoring webových stránek. Propojení těchto dvou technologií otevírá vývojářům a SEO specialistům nové možnosti automatizace a efektivní práce s daty o výkonu webových stránek.

Tento průvodce vám ukáže, jak implementovat integraci mezi Google Search Console a [MCP](/ai/mcp/) pomocí otevřeného řešení dostupného na [GitHubu od AminForou](https://github.com/AminForou/mcp-gsc). Díky této integraci budete moci:

- Získávat data z Google Search Console přímo ve vašem AI asistentovi
- Analyzovat výkon webových stránek bez nutnosti přepínat mezi aplikacemi
- Automatizovat reporting a monitoring klíčových SEO metrik
- Implementovat datově řízené úpravy obsahu a SEO strategie

## Požadavky pro úspěšnou integraci

Před začátkem integrace se ujistěte, že máte připraveno:

1. **Google Search Console účet** s přístupem k webovým stránkám, které chcete monitorovat
2. **Google Cloud projekt** s povoleným Google Search Console API
3. **MCP server** (například Zapier MCP)
4. **Cursor** nebo jiného AI asistenta podporujícího MCP
5. **Node.js** (verze 14 nebo novější) pro spuštění GSC konektoru
6. **Git** pro klonování repozitáře

## 1. Příprava Google Cloud projektu a API přístupu

### Vytvoření a konfigurace projektu v Google Cloud

1. Přejděte na [Google Cloud Console](https://console.cloud.<a href='/google/' class='keyword-link'>google</a>.com/)
2. Vytvořte nový projekt nebo vyberte existující
3. V navigačním menu vyberte "APIs & Services" > "Library"
4. Vyhledejte "Google Search Console API" a aktivujte jej
5. Přejděte do sekce "Credentials" a vytvořte nové OAuth 2.0 přihlašovací údaje:
   - Typ aplikace: Web application
   - Název: MCP GSC Integration
   - Autorizované přesměrovací URI: `http://localhost:3000/oauth2callback`
6. Stáhněte vygenerovaný JSON soubor s přihlašovacími údaji

## 2. Instalace MCP GSC konektoru

```bash
# Klonování repozitáře
git clone https://github.com/AminForou/mcp-gsc.git
cd mcp-gsc

# Instalace závislostí
npm install

# Kopírování konfiguračního souboru
cp config.example.json config.json
```

## 3. Konfigurace MCP GSC konektoru

Otevřete soubor `config.json` a upravte následující hodnoty:

```json
{
  "port": 3000,
  "auth": {
    "clientId": "YOUR_CLIENT_ID",
    "clientSecret": "YOUR_CLIENT_SECRET",
    "redirectUri": "http://localhost:3000/oauth2callback"
  },
  "sites": [
    "https://www.vasestranka.cz"
  ],
  "mcpEndpoint": "https://actions.zapier.com/mcp/YOUR_MCP_ID/sse"
}
```

Nahraďte:
- `YOUR_CLIENT_ID` a `YOUR_CLIENT_SECRET` hodnotami z vašeho Google Cloud projektu
- `https://www.vasestranka.cz` URL adresou vaší webové stránky registrované v Google Search Console
- `YOUR_MCP_ID` vaším unikátním identifikátorem ze Zapier MCP

## 4. Autorizace Google Search Console API

Spusťte aplikaci a dokončete autorizační proces:

```bash
npm start
```

1. Při prvním spuštění se v konzoli zobrazí autorizační URL
2. Otevřete URL ve webovém prohlížeči
3. Přihlaste se ke Google účtu a udělte přístup k Search Console API
4. Po úspěšné autorizaci budete přesměrováni zpět na lokální server
5. V konzoli by se mělo zobrazit potvrzení úspěšné autorizace
6. Autorizační [token](/ai/tokeny-versus-slova/) bude automaticky uložen pro budoucí použití

## 5. Propojení s MCP serverem (Zapier)

### Nastavení v Zapier MCP

1. Přejděte na [Zapier MCP stránku](https://zapier.com/mcp)
2. Klikněte na "Get Started" a zkopírujte svou unikátní MCP URL
3. Klikněte na "Edit MCP Actions" a vytvořte novou akci
4. Pojmenujte akci "Google Search Console Data"
5. Nastavte parametry akce:
   - `site`: URL webu (STRING)
   - `dateRange`: Rozsah dat (STRING: "last7days", "last30days", "last3months")
   - `dimensions`: Dimenze dat (STRING: "query", "page", "country", "device")

### Integrace do Cursor (nebo jiného AI asistenta)

1. Otevřete Cursor a přejděte do Settings > MCP > Add New MCP
2. Vložte MCP URL ze Zapier pod název "Google Search Console MCP"
3. Uložte nastavení

## 6. Používání GSC dat v AI asistentovi

Po úspěšné integraci můžete začít využívat data z Google Search Console přímo ve vašem AI asistentovi. Zde jsou příklady typických dotazů:

### Základní dotazy na výkon webu

```
Ukaž mi výkon mého webu z Google Search Console za posledních 30 dní.
```

### Analýza konkrétních klíčových slov

```
Jaké jsou moje nejúspěšnější klíčová slova podle počtu kliknutí za poslední týden?
```

### Identifikace problémových stránek

```
Které stránky mají vysoký počet zobrazení, ale nízkou míru prokliku?
```

### Analýza trendů

```
Porovnej výkon mého webu v mobilních zařízeních oproti desktopům za poslední 3 měsíce.
```

## 7. Rozšířené funkce

MCP GSC konektor nabízí několik pokročilých funkcí, které můžete využít:

### Vlastní časové rozsahy

Kromě předdefinovaných rozsahů můžete použít vlastní časové období:

```json
{
  "startDate": "2025-01-01",
  "endDate": "2025-03-26"
}
```

### Filtry dat

Filtrování dat podle specifických kritérií:

```json
{
  "filters": [
    {
      "dimension": "page",
      "operator": "contains",
      "expression": "/blog/"
    }
  ]
}
```

### Agregace a transformace dat

Konektor umožňuje základní agregaci a transformaci dat:

```json
{
  "aggregation": "sum",
  "groupBy": "query"
}
```

## 8. Řešení problémů

### Problém: Autorizační chyba

**Řešení:** Ujistěte se, že máte správně nakonfigurované přesměrovací URI v Google Cloud Console. Pokud problém přetrvává, smažte soubor `[token](/ai/tokeny-versus-slova/).json` a proveďte autorizaci znovu.

### Problém: Žádná data nejsou dostupná

**Řešení:** Ověřte, že webová stránka je správně registrována v Google Search Console a že máte dostatečná oprávnění. Některé nově přidané stránky nemusí mít okamžitě dostupná data.

### Problém: MCP nepřijímá požadavky

**Řešení:** Zkontrolujte, zda je MCP server spuštěn a dostupný. Ujistěte se, že adresa v `config.json` odpovídá vaší unikátní MCP URL.

## 9. Zabezpečení a best practices

Při práci s GSC API a MCP dbejte na následující bezpečnostní opatření:

1. **Nikdy nesdílejte** své OAuth přihlašovací údaje nebo tokeny
2. Pravidelně **obnovujte přístupové tokeny**
3. Používejte pouze **nezbytná oprávnění** pro vaši aplikaci
4. **Omezujte rozsah požadavků** na API, abyste předešli dosažení limitů
5. Implementujte **rate limiting** pro ochranu před zahlcením API

## Závěr

Propojení Google Search Console s MCP otevírá nové možnosti pro automatizaci SEO analýz a datově řízených rozhodnutí. Díky této integraci získáváte přímý přístup k cenným datům o výkonu vašich webových stránek přímo ve vašem AI asistentovi, což vám umožňuje efektivněji pracovat a činit informovaná rozhodnutí.

Pro nejnovější aktualizace a vylepšení sledujte [oficiální GitHub repozitář](https://github.com/AminForou/mcp-gsc) a zapojte se do komunity přispěvatelů, kteří pomáhají toto řešení dále rozvíjet.

---

*Poznámka: Tento průvodce vychází z dokumentace dostupné k březnu 2025. Některé funkce se mohou měnit s novými aktualizacemi Google Search Console API nebo MCP protokolu.*