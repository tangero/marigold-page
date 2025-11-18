---
author: Marisa Aigen
category: bezpečnostní aktuali
companies:
- Microsoft
date: '2025-11-16 21:47:14'
description: Microsoft v listopadu 2025 vydal bezpečnostní aktualizace pro více než
  60 zranitelností, včetně aktivně zneužívaného zero-dayu CVE-2025-62215 a kritických
  chyb v grafické knihovně GDI+ a aplikaci Office.
importance: 4
layout: tech_news_article
original_title: Microsoft Patch Tuesday, November 2025 Edition
publishedAt: '2025-11-16T21:47:14+00:00'
slug: microsoft-patch-tuesday-november-2025-edition
source:
  emoji: 📰
  id: null
  name: Krebs on Security
title: Microsoft vydal nouzové bezpečnostní záplaty – řeší aktivně zneužívaný zero-day
  a kritické chyby v GDI+ a Office
url: https://krebsonsecurity.com/2025/11/microsoft-patch-tuesday-november-2025-edition/
---

## Souhrn
Microsoft vydal v rámci listopadového Patch Tuesday bezpečnostní aktualizace pro více než 60 zranitelností napříč svými produkty, včetně Windows, Office, SharePointu, SQL Serveru a dalších. Mezi nimi je alespoň jeden zero-day (CVE-2025-62215), který je již aktivně zneužíván, a kritická chyba v grafické knihovně GDI+ (CVE-2025-60274) s hodnocením CVSS 9,8.

## Klíčové body
- Zero-day CVE-2025-62215 je zneužíván v reálných útocích, ale vyžaduje předchozí přístup k zařízení.
- Kritická chyba CVE-2025-60274 v GDI+ ohrožuje tisíce aplikací, včetně Office a webových serverů zpracovávajících obrázky.
- Další vážná zranitelnost CVE-2025-62199 v Office umožňuje vzdálené spuštění kódu bez zvláštní interakce uživatele.
- Microsoft opravil také chybu bránící některým uživatelům Windows 10 využít prodlouženou podporu.
- Mezi zranitelné produkty patří i GitHub Copilot a Azure Monitor Agent.

## Podrobnosti
Nejvážnější hrozba měsíce pochází z grafické knihovny GDI+ (Graphics Device Interface Plus), která je součástí Windows a slouží ke zpracování 2D grafiky. Chyba CVE-2025-60274 umožňuje vzdálené spuštění kódu a má skóre CVSS 9,8 z 10. Tato knihovna je používána nejen Microsoft Office, ale i bezpočtem webových aplikací a serverů, které zpracovávají obrázky – například při nahrávání avatarů nebo náhledů. Bezpečnostní expert Ben McCarthy z firmy Immersive (specializující se na kybernetickou bezpečnost firemních sítí) varuje, že i přes Microsoftovo hodnocení „Exploitation Less Likely“ je riziko extrémně vysoké kvůli rozsahu použití GDI+.

Druhá závažná chyba, CVE-2025-62199 v Office, umožňuje útočníkovi spustit libovolný kód na cílovém systému s nízkou složitostí a bez potřeby zvláštních oprávnění. Podle Alexe Vovka, CEO společnosti Action1 (poskytovatele cloudového řešení pro správu a zabezpečení zařízení), jde o prioritní riziko pro podniky.

Zero-day CVE-2025-62215 je klasifikován jako „Important“, nikoli „Critical“, protože útočník potřebuje mít již nějaký přístup k systému – typicky jako součást pokročilého útočného řetězce. Přesto jej SANS Technology Institute označuje za potenciálně jednoduchý k využití díky podobnosti s dřívějšími chybami.

## Proč je to důležité
Tento měsíc přináší neobvykle vysokou koncentraci kritických zranitelností v jádru Windows a klíčových aplikacích. GDI+ je zastaralá, ale stále široce používaná komponenta – její zranitelnost může vést k masivním útokům na firemní i veřejné weby. Zároveň ukazuje, že i „méně kritické“ zero-day chyby mohou být využity v kombinaci s jinými technikami pro přetrvávání v systému. Pro správce IT a bezpečnostní týmy je nutné co nejdříve nasadit aktualizace, zejména na serverech zpracovávajících uživatelské soubory a v prostředích s Office.

---

[Číst původní článek](https://krebsonsecurity.com/2025/11/microsoft-patch-tuesday-november-2025-edition/)

**Zdroj:** 📰 Krebs on Security
